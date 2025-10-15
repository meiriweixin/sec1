import { useState } from "react";
import { Button } from "@/components/ui/button";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { motion, Reorder } from "framer-motion";
import { CheckCircle, XCircle, GripVertical } from "lucide-react";

interface DragOrderExerciseProps {
  exercise: {
    id: string;
    type: "drag-order";
    prompt: string;
    prompt_zh?: string;
    items?: string[];
    items_zh?: string[];
    answer: string[];
    answer_zh?: string[];
    hint?: string;
    hint_zh?: string;
    explanation?: string;
    explanation_zh?: string;
  };
  onAnswer: (isCorrect: boolean, userAnswer: string[]) => void;
  showHint: boolean;
  showExplanation: boolean;
  attempts: number;
  previousScore?: number;
}

export function DragOrderExercise({ 
  exercise, 
  onAnswer, 
  showHint, 
  showExplanation,
  attempts,
  previousScore
}: DragOrderExerciseProps) {
  const { language } = useStore();
  const t = useTranslations(language);
  
  // Get localized items and answer
  const items = language === 'zh' && exercise.items_zh ? exercise.items_zh : exercise.items || [];
  const correctOrder = language === 'zh' && exercise.answer_zh ? exercise.answer_zh : exercise.answer;
  
  // Initialize with shuffled items
  const [orderedItems, setOrderedItems] = useState<string[]>(() => {
    // Create a shuffled copy of items
    const shuffled = [...items];
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
  });
  
  const [hasSubmitted, setHasSubmitted] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const handleSubmit = () => {
    const isAnswerCorrect = orderedItems.every((item, index) => item === correctOrder[index]);
    
    setIsCorrect(isAnswerCorrect);
    setHasSubmitted(true);
    onAnswer(isAnswerCorrect, orderedItems);
  };

  const handleRetry = () => {
    // Reshuffle items
    const shuffled = [...items];
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    setOrderedItems(shuffled);
    setHasSubmitted(false);
    setIsCorrect(false);
  };

  const getItemStyle = (item: string, index: number) => {
    if (!hasSubmitted) return "";
    
    const isInCorrectPosition = item === correctOrder[index];
    if (isInCorrectPosition) {
      return "border-success bg-success-soft/30";
    } else {
      return "border-destructive bg-destructive/5";
    }
  };

  const getItemIcon = (item: string, index: number) => {
    if (!hasSubmitted) return null;
    
    const isInCorrectPosition = item === correctOrder[index];
    if (isInCorrectPosition) {
      return <CheckCircle className="h-4 w-4 text-success" />;
    } else {
      return <XCircle className="h-4 w-4 text-destructive" />;
    }
  };

  return (
    <div className="space-y-4">
      {/* Previous attempt indicator */}
      {previousScore !== undefined && (
        <div className="text-sm text-muted-foreground">
          Previous score: {previousScore}%
        </div>
      )}

      {/* Instructions */}
      <div className="text-sm text-muted-foreground">
        Drag and drop items to arrange them in the correct order
      </div>

      {/* Draggable Items */}
      <Reorder.Group 
        axis="y" 
        values={orderedItems} 
        onReorder={setOrderedItems}
        className="space-y-2"
      >
        {orderedItems.map((item, index) => (
          <Reorder.Item
            key={item}
            value={item}
            dragListener={!hasSubmitted}
            className={`${hasSubmitted ? "cursor-default" : "cursor-grab active:cursor-grabbing"}`}
          >
            <motion.div
              layout
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.05 }}
              className={`flex items-center space-x-3 p-4 rounded-lg border transition-all ${
                getItemStyle(item, index) || "border-border bg-card hover:bg-muted/50"
              }`}
            >
              {!hasSubmitted && (
                <GripVertical className="h-5 w-5 text-muted-foreground" />
              )}
              <div className="flex items-center justify-between flex-1">
                <div className="flex items-center space-x-3">
                  <span className="font-medium text-muted-foreground">
                    {index + 1}.
                  </span>
                  <span className="text-foreground">{item}</span>
                </div>
                {getItemIcon(item, index)}
              </div>
            </motion.div>
          </Reorder.Item>
        ))}
      </Reorder.Group>

      {/* Feedback */}
      {hasSubmitted && !isCorrect && (
        <motion.div
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          className="p-3 bg-muted rounded-lg"
        >
          <p className="text-sm font-medium mb-2">Correct order:</p>
          <ol className="list-decimal list-inside space-y-1">
            {correctOrder.map((item, index) => (
              <li key={index} className="text-sm text-foreground">
                {item}
              </li>
            ))}
          </ol>
        </motion.div>
      )}

      {/* Action Buttons */}
      <div className="flex space-x-2 pt-4">
        {!hasSubmitted ? (
          <Button
            onClick={handleSubmit}
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



