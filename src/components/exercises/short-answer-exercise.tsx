import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { motion } from "framer-motion";
import { CheckCircle, XCircle, Sparkles, Loader2, Lightbulb, TrendingUp } from "lucide-react";
import { evaluateHumanitiesAnswer, shouldUseAIEvaluation } from "@/lib/azure-humanities-evaluator";

interface ShortAnswerExerciseProps {
  exercise: {
    id: string;
    type: "short";
    prompt: string;
    prompt_zh?: string;
    answer: string;
    answer_zh?: string;
    validator?: string;
    hint?: string;
    hint_zh?: string;
    explanation?: string;
    explanation_zh?: string;
    sampleAnswers?: string[];
    acceptableAnswers?: string[];
  };
  onAnswer: (isCorrect: boolean, userAnswer: string) => void;
  showHint: boolean;
  showExplanation: boolean;
  attempts: number;
  previousScore?: number;
  subjectId?: string;
  gradeLevel?: string;
}

export function ShortAnswerExercise({
  exercise,
  onAnswer,
  showHint,
  showExplanation,
  attempts,
  previousScore,
  subjectId,
  gradeLevel
}: ShortAnswerExerciseProps) {
  const { language } = useStore();
  const t = useTranslations(language);

  const [userAnswer, setUserAnswer] = useState("");
  const [hasSubmitted, setHasSubmitted] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  const [isEvaluatingAI, setIsEvaluatingAI] = useState(false);
  const [aiFeedback, setAIFeedback] = useState<{
    score: number;
    isCorrect: boolean;
    level?: 1 | 2;
    feedback: string;
    feedback_zh?: string;
    strengths?: string[];
    improvements?: string[];
  } | null>(null);

  const correctAnswer = language === 'zh' && exercise.answer_zh ? exercise.answer_zh : exercise.answer;

  /**
   * Normalize answer for flexible matching
   * Handles: Unicode subscripts/superscripts, whitespace, symbols, punctuation, articles
   */
  const normalizeAnswer = (text: string): string => {
    return text
      .trim()
      .toLowerCase()
      // Unicode subscripts (₀-₉) to normal numbers
      .replace(/[₀-₉]/g, (c) => String.fromCharCode(c.charCodeAt(0) - 0x2080 + 0x30))
      // Unicode superscripts (⁰-⁹) to normal numbers
      .replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹]/g, (c) => {
        const map: Record<string, string> = {
          '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
          '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'
        };
        return map[c] || c;
      })
      // Symbol normalization
      .replace(/×/g, '*')
      .replace(/÷/g, '/')
      // Whitespace normalization
      .replace(/\s+/g, ' ')
      .replace(/\s*([,/\-+])\s*/g, '$1')
      // Remove trailing punctuation only
      .replace(/[.,;:!?'"]+$/, '')
      // Remove common articles
      .replace(/\b(the|a|an)\b/g, '')
      .trim();
  };

  /**
   * Smart validation with flexible matching
   * Allows reasonable formatting variations while maintaining correctness
   * Enhanced for Humanities-style answers (essays, explanations)
   */
  const validateAnswerSmart = (input: string, correct: string): boolean => {
    const normInput = normalizeAnswer(input);
    const normCorrect = normalizeAnswer(correct);

    // Exact match after normalization
    if (normInput === normCorrect) return true;

    // Single-word flexibility
    const inputWords = normInput.split(' ').filter(w => w.length > 0);
    const correctWords = normCorrect.split(' ').filter(w => w.length > 0);

    // If correct answer is single word, check if it appears in input
    if (correctWords.length === 1 && inputWords.includes(correctWords[0])) return true;

    // If input is single word, check if it matches any word in correct answer
    if (inputWords.length === 1 && correctWords.includes(inputWords[0])) return true;

    // Check if all words in correct answer appear in input (order doesn't matter)
    if (correctWords.every(word => inputWords.includes(word))) return true;

    // === ENHANCED MATCHING FOR LONGER ANSWERS ===

    // Remove common stop words for comparison
    const stopWords = ['is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
      'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must',
      'shall', 'can', 'need', 'dare', 'ought', 'used', 'to', 'of', 'in', 'for', 'on',
      'with', 'at', 'by', 'from', 'as', 'into', 'through', 'during', 'before', 'after',
      'above', 'below', 'between', 'under', 'again', 'further', 'then', 'once', 'here',
      'there', 'when', 'where', 'why', 'how', 'all', 'each', 'few', 'more', 'most',
      'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than',
      'too', 'very', 'just', 'and', 'but', 'if', 'or', 'because', 'until', 'while',
      'that', 'which', 'who', 'whom', 'this', 'these', 'those', 'it', 'its'];

    const getKeyWords = (words: string[]) =>
      words.filter(w => w.length > 2 && !stopWords.includes(w));

    const inputKeyWords = getKeyWords(inputWords);
    const correctKeyWords = getKeyWords(correctWords);

    // For longer answers (3+ key words), check if enough key words match
    if (correctKeyWords.length >= 3) {
      const matchingKeyWords = correctKeyWords.filter(word =>
        inputKeyWords.some(inputWord =>
          inputWord === word ||
          inputWord.includes(word) ||
          word.includes(inputWord) ||
          // Allow for slight typos (1-2 char difference for words > 4 chars)
          (word.length > 4 && inputWord.length > 4 &&
           levenshteinDistance(word, inputWord) <= 2)
        )
      );

      // Accept if 60%+ of key words match (more lenient for essays)
      const matchRatio = matchingKeyWords.length / correctKeyWords.length;
      if (matchRatio >= 0.6) return true;
    }

    // Check if input contains the main concept (first 2-3 key words)
    if (correctKeyWords.length >= 2) {
      const mainConcepts = correctKeyWords.slice(0, 3);
      const conceptsFound = mainConcepts.filter(concept =>
        inputKeyWords.some(word => word.includes(concept) || concept.includes(word))
      );
      if (conceptsFound.length >= Math.ceil(mainConcepts.length * 0.6)) return true;
    }

    // Substring match for short answers embedded in longer responses
    if (normCorrect.length <= 30 && normInput.includes(normCorrect)) return true;
    if (normInput.length <= 30 && normCorrect.includes(normInput)) return true;

    return false;
  };

  /**
   * Calculate Levenshtein distance between two strings
   * Used for typo tolerance in smart validation
   */
  const levenshteinDistance = (str1: string, str2: string): number => {
    const m = str1.length;
    const n = str2.length;
    const dp: number[][] = Array(m + 1).fill(null).map(() => Array(n + 1).fill(0));

    for (let i = 0; i <= m; i++) dp[i][0] = i;
    for (let j = 0; j <= n; j++) dp[0][j] = j;

    for (let i = 1; i <= m; i++) {
      for (let j = 1; j <= n; j++) {
        if (str1[i - 1] === str2[j - 1]) {
          dp[i][j] = dp[i - 1][j - 1];
        } else {
          dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
        }
      }
    }
    return dp[m][n];
  };

  const validateAnswer = (input: string): boolean => {
    const normalizedInput = input.trim().toLowerCase();
    const normalizedCorrect = correctAnswer.trim().toLowerCase();

    switch (exercise.validator) {
      case "numeric":
        // For numeric answers, parse and compare numbers with tolerance
        const inputNum = parseFloat(normalizedInput);
        const correctNum = parseFloat(normalizedCorrect);
        return !isNaN(inputNum) && !isNaN(correctNum) && Math.abs(inputNum - correctNum) < 0.001;

      case "fraction":
        // For fractions, accept different formats (e.g., "1/5" or "0.2")
        if (normalizedInput === normalizedCorrect) return true;

        // Try to evaluate as fraction
        if (normalizedInput.includes("/")) {
          const [num, den] = normalizedInput.split("/").map(n => parseFloat(n.trim()));
          if (!isNaN(num) && !isNaN(den) && den !== 0) {
            const inputValue = num / den;

            // Check if correct answer is also a fraction
            if (normalizedCorrect.includes("/")) {
              const [correctNum, correctDen] = normalizedCorrect.split("/").map(n => parseFloat(n.trim()));
              const correctValue = correctNum / correctDen;
              return Math.abs(inputValue - correctValue) < 0.001;
            } else {
              // Compare with decimal
              const correctValue = parseFloat(normalizedCorrect);
              return Math.abs(inputValue - correctValue) < 0.001;
            }
          }
        }
        return false;

      case "exact":
      case "strict":
        // Strict case-insensitive exact match only (for exercises requiring exact formatting)
        return normalizedInput === normalizedCorrect;

      case "smart":
        // Smart flexible matching (new recommended default)
        return validateAnswerSmart(input, correctAnswer);

      default:
        // Default: Use smart validation for maximum flexibility
        // This handles Unicode normalization, whitespace, punctuation, etc.
        return validateAnswerSmart(input, correctAnswer);
    }
  };

  const handleSubmit = async () => {
    // Check if this subject should use AI evaluation
    const useAI = subjectId && shouldUseAIEvaluation(subjectId, 'short');

    if (useAI) {
      // Use AI evaluation for humanities subjects
      setIsEvaluatingAI(true);
      try {
        const result = await evaluateHumanitiesAnswer({
          subject: subjectId!,
          questionType: 'short',
          prompt: exercise.prompt,
          prompt_zh: exercise.prompt_zh,
          studentAnswer: userAnswer,
          modelAnswer: correctAnswer,
          sampleAnswers: exercise.sampleAnswers || exercise.acceptableAnswers,
          gradeLevel: gradeLevel,
          language: language
        });

        setAIFeedback(result);
        setIsCorrect(result.isCorrect);
        setHasSubmitted(true);
        setIsEvaluatingAI(false);
        onAnswer(result.isCorrect, userAnswer);
      } catch (error) {
        console.error('AI evaluation failed, falling back to keyword matching:', error);
        setIsEvaluatingAI(false);
        // Fallback to traditional validation
        const isAnswerCorrect = validateAnswer(userAnswer);
        setIsCorrect(isAnswerCorrect);
        setHasSubmitted(true);
        onAnswer(isAnswerCorrect, userAnswer);
      }
    } else {
      // Use traditional validation for STEM subjects
      const isAnswerCorrect = validateAnswer(userAnswer);
      setIsCorrect(isAnswerCorrect);
      setHasSubmitted(true);
      onAnswer(isAnswerCorrect, userAnswer);
    }
  };

  const handleRetry = () => {
    setUserAnswer("");
    setHasSubmitted(false);
    setIsCorrect(false);
    setAIFeedback(null);
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      if (userAnswer.trim() && !hasSubmitted) {
        handleSubmit();
      }
    }
  };

  const isLongAnswer = exercise.prompt.length > 100 || correctAnswer.length > 50;

  return (
    <div className="space-y-4">
      {/* Previous attempt indicator */}
      {previousScore !== undefined && (
        <div className="text-sm text-muted-foreground">
          Previous score: {previousScore}%
        </div>
      )}

      {/* Answer Input */}
      <div className="space-y-2">
        {isLongAnswer ? (
          <Textarea
            value={userAnswer}
            onChange={(e) => setUserAnswer(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Type your answer here..."
            disabled={hasSubmitted}
            className={`min-h-[100px] ${
              hasSubmitted
                ? isCorrect
                  ? "border-success bg-success-soft/30"
                  : "border-destructive bg-destructive/5"
                : ""
            }`}
          />
        ) : (
          <Input
            value={userAnswer}
            onChange={(e) => setUserAnswer(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Type your answer here..."
            disabled={hasSubmitted}
            className={`text-lg ${
              hasSubmitted
                ? isCorrect
                  ? "border-success bg-success-soft/30"
                  : "border-destructive bg-destructive/5"
                : ""
            }`}
          />
        )}
      </div>

      {/* Feedback */}
      {hasSubmitted && (
        <motion.div
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          className="space-y-3"
        >
          <div className="flex items-center space-x-2">
            {isCorrect ? (
              <>
                <CheckCircle className="h-5 w-5 text-success" />
                <span className="font-medium text-success">{t.correct}</span>
                {aiFeedback && (
                  <span className="text-xs text-muted-foreground ml-2">
                    ({aiFeedback.score}% • {aiFeedback.level && `Level ${aiFeedback.level}`})
                  </span>
                )}
              </>
            ) : (
              <>
                <XCircle className="h-5 w-5 text-destructive" />
                <span className="font-medium text-destructive">{t.incorrect}</span>
                {aiFeedback && (
                  <span className="text-xs text-muted-foreground ml-2">
                    ({aiFeedback.score}%)
                  </span>
                )}
              </>
            )}
          </div>

          {/* AI Feedback */}
          {aiFeedback && (
            <div className="space-y-3">
              {/* AI Evaluation Badge */}
              <div className="flex items-center gap-2 text-xs text-purple-600 dark:text-purple-400">
                <Sparkles className="h-4 w-4" />
                <span>AI-Powered Evaluation</span>
              </div>

              {/* Feedback Message */}
              <div className="p-3 bg-blue-50 dark:bg-blue-950/20 rounded-lg border border-blue-200 dark:border-blue-800">
                <p className="text-sm text-blue-900 dark:text-blue-100">
                  {language === 'zh' && aiFeedback.feedback_zh ? aiFeedback.feedback_zh : aiFeedback.feedback}
                </p>
              </div>

              {/* Strengths */}
              {aiFeedback.strengths && aiFeedback.strengths.length > 0 && (
                <div className="p-3 bg-green-50 dark:bg-green-950/20 rounded-lg border border-green-200 dark:border-green-800">
                  <div className="flex items-center gap-2 mb-2">
                    <TrendingUp className="h-4 w-4 text-green-600" />
                    <p className="text-sm font-medium text-green-900 dark:text-green-100">
                      {language === 'zh' ? '优点' : 'Strengths'}
                    </p>
                  </div>
                  <ul className="space-y-1 text-sm text-green-800 dark:text-green-200">
                    {aiFeedback.strengths.map((strength, idx) => (
                      <li key={idx} className="flex items-start gap-2">
                        <span className="text-green-600">✓</span>
                        <span>{strength}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Improvements */}
              {aiFeedback.improvements && aiFeedback.improvements.length > 0 && (
                <div className="p-3 bg-orange-50 dark:bg-orange-950/20 rounded-lg border border-orange-200 dark:border-orange-800">
                  <div className="flex items-center gap-2 mb-2">
                    <Lightbulb className="h-4 w-4 text-orange-600" />
                    <p className="text-sm font-medium text-orange-900 dark:text-orange-100">
                      {language === 'zh' ? '改进建议' : 'Areas for Improvement'}
                    </p>
                  </div>
                  <ul className="space-y-1 text-sm text-orange-800 dark:text-orange-200">
                    {aiFeedback.improvements.map((improvement, idx) => (
                      <li key={idx} className="flex items-start gap-2">
                        <span className="text-orange-600">•</span>
                        <span>{improvement}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}

          {/* Traditional Feedback (for non-AI or when AI fails) */}
          {!isCorrect && !aiFeedback && (
            <div className="p-3 bg-muted rounded-lg">
              <p className="text-sm font-medium mb-1">Correct answer:</p>
              <p className="text-sm text-foreground font-mono">{correctAnswer}</p>
              {userAnswer && (
                <>
                  <p className="text-sm font-medium mt-2 mb-1">Your answer:</p>
                  <p className="text-sm text-muted-foreground font-mono">{userAnswer}</p>
                </>
              )}
            </div>
          )}
        </motion.div>
      )}

      {/* Action Buttons */}
      <div className="flex space-x-2 pt-4">
        {!hasSubmitted ? (
          <Button
            onClick={handleSubmit}
            disabled={!userAnswer.trim() || isEvaluatingAI}
            className="btn-primary"
          >
            {isEvaluatingAI ? (
              <>
                <Loader2 className="h-4 w-4 mr-2 animate-spin" />
                {language === 'zh' ? 'AI评估中...' : 'AI Evaluating...'}
              </>
            ) : (
              t.submit
            )}
          </Button>
        ) : (
          <>
            {!isCorrect && attempts < 3 && (
              <Button onClick={handleRetry} variant="outline">
                {t.tryAgain}
              </Button>
            )}
          </>
        )}
      </div>
    </div>
  );
}



