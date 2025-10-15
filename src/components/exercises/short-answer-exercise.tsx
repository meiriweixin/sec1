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

  const validateAnswer = (input: string): boolean => {
    const normalizedInput = input.trim().toLowerCase();
    const normalizedCorrect = correctAnswer.trim().toLowerCase();

    switch (exercise.validator) {
      case "numeric":
        // For numeric answers, parse and compare numbers
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
        // Exact match required
        return normalizedInput === normalizedCorrect;
      
      default:
        // Default: case-insensitive match with some flexibility
        // Remove common punctuation and extra spaces
        const cleanInput = normalizedInput.replace(/[.,;:!?'"]/g, "").replace(/\s+/g, " ");
        const cleanCorrect = normalizedCorrect.replace(/[.,;:!?'"]/g, "").replace(/\s+/g, " ");
        
        // Check for exact match or if one contains the other (for single word answers)
        return cleanInput === cleanCorrect || 
               (cleanCorrect.split(" ").length === 1 && cleanInput.includes(cleanCorrect)) ||
               (cleanInput.split(" ").length === 1 && cleanCorrect.includes(cleanInput));
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



