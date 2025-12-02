import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { motion } from "framer-motion";
import { CheckCircle, XCircle } from "lucide-react";

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
  };
  onAnswer: (isCorrect: boolean, userAnswer: string) => void;
  showHint: boolean;
  showExplanation: boolean;
  attempts: number;
  previousScore?: number;
}

export function ShortAnswerExercise({ 
  exercise, 
  onAnswer, 
  showHint, 
  showExplanation,
  attempts,
  previousScore
}: ShortAnswerExerciseProps) {
  const { language } = useStore();
  const t = useTranslations(language);
  
  const [userAnswer, setUserAnswer] = useState("");
  const [hasSubmitted, setHasSubmitted] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

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

    return false;
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

  const handleSubmit = () => {
    const isAnswerCorrect = validateAnswer(userAnswer);
    
    setIsCorrect(isAnswerCorrect);
    setHasSubmitted(true);
    onAnswer(isAnswerCorrect, userAnswer);
  };

  const handleRetry = () => {
    setUserAnswer("");
    setHasSubmitted(false);
    setIsCorrect(false);
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
          className="space-y-2"
        >
          <div className="flex items-center space-x-2">
            {isCorrect ? (
              <>
                <CheckCircle className="h-5 w-5 text-success" />
                <span className="font-medium text-success">{t.correct}</span>
              </>
            ) : (
              <>
                <XCircle className="h-5 w-5 text-destructive" />
                <span className="font-medium text-destructive">{t.incorrect}</span>
              </>
            )}
          </div>
          
          {!isCorrect && (
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
            disabled={!userAnswer.trim()}
            className="btn-primary"
          >
            {t.submit}
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



