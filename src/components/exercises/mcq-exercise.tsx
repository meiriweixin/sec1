import { useState } from "react";
import { Button } from "@/components/ui/button";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Checkbox } from "@/components/ui/checkbox";
import { Label } from "@/components/ui/label";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { motion } from "framer-motion";
import { CheckCircle, XCircle } from "lucide-react";
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

interface MCQExerciseProps {
  exercise: {
    id: string;
    type: "mcq" | "multi";
    prompt: string;
    prompt_zh?: string;
    choices?: string[];
    choices_zh?: string[];
    answer: number | number[];
    hint?: string;
    hint_zh?: string;
    explanation?: string;
    explanation_zh?: string;
  };
  onAnswer: (isCorrect: boolean, userAnswer: any) => void;
  showHint: boolean;
  showExplanation: boolean;
  attempts: number;
  previousScore?: number;
}

export function MCQExercise({ 
  exercise, 
  onAnswer, 
  showHint, 
  showExplanation,
  attempts,
  previousScore
}: MCQExerciseProps) {
  const { language } = useStore();
  const t = useTranslations(language);
  
  const [selectedAnswer, setSelectedAnswer] = useState<string>("");
  const [selectedMultiple, setSelectedMultiple] = useState<number[]>([]);
  const [hasSubmitted, setHasSubmitted] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const choices = language === 'zh' && exercise.choices_zh ? exercise.choices_zh : exercise.choices || [];
  const isMultiChoice = exercise.type === "multi";

  const handleSubmit = () => {
    if (isMultiChoice) {
      const correctAnswers = Array.isArray(exercise.answer) ? exercise.answer : [exercise.answer];
      const isAnswerCorrect = 
        selectedMultiple.length === correctAnswers.length &&
        selectedMultiple.every(ans => correctAnswers.includes(ans));
      
      setIsCorrect(isAnswerCorrect);
      setHasSubmitted(true);
      onAnswer(isAnswerCorrect, selectedMultiple);
    } else {
      const userAnswerIndex = parseInt(selectedAnswer);
      const isAnswerCorrect = userAnswerIndex === exercise.answer;
      
      setIsCorrect(isAnswerCorrect);
      setHasSubmitted(true);
      onAnswer(isAnswerCorrect, userAnswerIndex);
    }
  };

  const handleRetry = () => {
    setSelectedAnswer("");
    setSelectedMultiple([]);
    setHasSubmitted(false);
    setIsCorrect(false);
  };

  const handleMultipleChange = (index: number, checked: boolean) => {
    if (checked) {
      setSelectedMultiple([...selectedMultiple, index]);
    } else {
      setSelectedMultiple(selectedMultiple.filter(i => i !== index));
    }
  };

  const getChoiceStyle = (index: number) => {
    if (!hasSubmitted) return "";
    
    const correctAnswers = Array.isArray(exercise.answer) ? exercise.answer : [exercise.answer];
    const isThisCorrect = correctAnswers.includes(index);
    const isThisSelected = isMultiChoice 
      ? selectedMultiple.includes(index) 
      : parseInt(selectedAnswer) === index;

    if (isThisCorrect) {
      return "border-success bg-success-soft";
    } else if (isThisSelected && !isThisCorrect) {
      return "border-destructive bg-destructive/5";
    }
    return "";
  };

  const getChoiceIcon = (index: number) => {
    if (!hasSubmitted) return null;
    
    const correctAnswers = Array.isArray(exercise.answer) ? exercise.answer : [exercise.answer];
    const isThisCorrect = correctAnswers.includes(index);
    const isThisSelected = isMultiChoice 
      ? selectedMultiple.includes(index) 
      : parseInt(selectedAnswer) === index;

    if (isThisCorrect) {
      return <CheckCircle className="h-4 w-4 text-success" />;
    } else if (isThisSelected && !isThisCorrect) {
      return <XCircle className="h-4 w-4 text-destructive" />;
    }
    return null;
  };

  return (
    <div className="space-y-4">
      {/* Previous attempt indicator */}
      {previousScore !== undefined && (
        <div className="text-sm text-muted-foreground">
          Previous score: {previousScore}%
        </div>
      )}

      {/* Choices */}
      {isMultiChoice ? (
        <div className="space-y-3">
          <p className="text-sm text-muted-foreground mb-2">Select all that apply:</p>
          {choices.map((choice, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 }}
              className={`flex items-center space-x-3 p-4 rounded-lg border transition-all ${
                getChoiceStyle(index) || "border-border hover:bg-muted/50"
              } ${hasSubmitted ? "cursor-default" : "cursor-pointer"}`}
              onClick={() => !hasSubmitted && handleMultipleChange(index, !selectedMultiple.includes(index))}
            >
              <Checkbox
                checked={selectedMultiple.includes(index)}
                disabled={hasSubmitted}
                onCheckedChange={(checked) => handleMultipleChange(index, checked as boolean)}
              />
              <div className="flex-1 cursor-pointer prose prose-sm max-w-none dark:prose-invert">
                <ReactMarkdown
                  remarkPlugins={[remarkGfm, remarkMath]}
                  rehypePlugins={[rehypeKatex]}
                  components={{
                    p: ({ children }) => <span>{children}</span>
                  }}
                >
                  {choice}
                </ReactMarkdown>
              </div>
              {getChoiceIcon(index)}
            </motion.div>
          ))}
        </div>
      ) : (
        <RadioGroup 
          value={selectedAnswer} 
          onValueChange={setSelectedAnswer}
          disabled={hasSubmitted}
        >
          <div className="space-y-3">
            {choices.map((choice, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.1 }}
              >
                <Label
                  htmlFor={`choice-${index}`}
                  className={`flex items-center space-x-3 p-4 rounded-lg border transition-all cursor-pointer ${
                    getChoiceStyle(index) || "border-border hover:bg-muted/50"
                  } ${hasSubmitted ? "cursor-default" : ""}`}
                >
                  <RadioGroupItem value={index.toString()} id={`choice-${index}`} />
                  <div className="flex-1 prose prose-sm max-w-none dark:prose-invert">
                    <ReactMarkdown
                      remarkPlugins={[remarkGfm, remarkMath]}
                      rehypePlugins={[rehypeKatex]}
                      components={{
                        p: ({ children }) => <span>{children}</span>
                      }}
                    >
                      {choice}
                    </ReactMarkdown>
                  </div>
                  {getChoiceIcon(index)}
                </Label>
              </motion.div>
            ))}
          </div>
        </RadioGroup>
      )}

      {/* Action Buttons */}
      <div className="flex space-x-2 pt-4">
        {!hasSubmitted ? (
          <Button
            onClick={handleSubmit}
            disabled={isMultiChoice ? selectedMultiple.length === 0 : !selectedAnswer}
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
            {isCorrect && (
              <motion.div
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                className="flex items-center space-x-2 text-success"
              >
                <CheckCircle className="h-5 w-5" />
                <span className="font-medium">{t.correct}</span>
              </motion.div>
            )}
          </>
        )}
      </div>
    </div>
  );
}



