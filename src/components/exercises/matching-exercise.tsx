import { useState } from "react";
import { Button } from "@/components/ui/button";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { motion } from "framer-motion";
import { CheckCircle, XCircle, Link2 } from "lucide-react";

interface MatchPair {
  left: string;
  left_zh?: string;
  right: string;
  right_zh?: string;
}

interface MatchingExerciseProps {
  exercise: {
    id: string;
    type: "match";
    prompt: string;
    prompt_zh?: string;
    pairs?: MatchPair[];
    hint?: string;
    hint_zh?: string;
    explanation?: string;
    explanation_zh?: string;
  };
  onAnswer: (isCorrect: boolean, userAnswer: Record<string, string>) => void;
  showHint: boolean;
  showExplanation: boolean;
  attempts: number;
  previousScore?: number;
}

export function MatchingExercise({ 
  exercise, 
  onAnswer, 
  showHint, 
  showExplanation,
  attempts,
  previousScore
}: MatchingExerciseProps) {
  const { language } = useStore();
  const t = useTranslations(language);

  const pairs = exercise.pairs || [];

  // Extract left and right items based on language, shuffle right items
  const leftItems = pairs.map(p => language === 'zh' && p.left_zh ? p.left_zh : p.left);
  const rightItems = pairs.map(p => language === 'zh' && p.right_zh ? p.right_zh : p.right);
  const [shuffledRight] = useState(() => {
    const shuffled = [...rightItems];
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
  });
  
  const [connections, setConnections] = useState<Record<string, string>>({});
  const [selectedLeft, setSelectedLeft] = useState<string | null>(null);
  const [selectedRight, setSelectedRight] = useState<string | null>(null);
  const [hasSubmitted, setHasSubmitted] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const handleLeftClick = (item: string) => {
    if (hasSubmitted) return;
    
    if (selectedLeft === item) {
      setSelectedLeft(null);
    } else {
      setSelectedLeft(item);
      if (selectedRight) {
        // Make connection
        const newConnections = { ...connections, [item]: selectedRight };
        setConnections(newConnections);
        setSelectedLeft(null);
        setSelectedRight(null);
      }
    }
  };

  const handleRightClick = (item: string) => {
    if (hasSubmitted) return;
    
    if (selectedRight === item) {
      setSelectedRight(null);
    } else {
      setSelectedRight(item);
      if (selectedLeft) {
        // Make connection
        const newConnections = { ...connections, [selectedLeft]: item };
        setConnections(newConnections);
        setSelectedLeft(null);
        setSelectedRight(null);
      }
    }
  };

  const removeConnection = (leftItem: string) => {
    if (hasSubmitted) return;
    const newConnections = { ...connections };
    delete newConnections[leftItem];
    setConnections(newConnections);
  };

  const handleSubmit = () => {
    // Build correct connections map based on language
    const correctConnections: Record<string, string> = {};
    pairs.forEach(p => {
      const left = language === 'zh' && p.left_zh ? p.left_zh : p.left;
      const right = language === 'zh' && p.right_zh ? p.right_zh : p.right;
      correctConnections[left] = right;
    });

    const isAnswerCorrect =
      Object.keys(connections).length === pairs.length &&
      Object.entries(connections).every(([left, right]) => correctConnections[left] === right);

    setIsCorrect(isAnswerCorrect);
    setHasSubmitted(true);
    onAnswer(isAnswerCorrect, connections);
  };

  const handleRetry = () => {
    setConnections({});
    setSelectedLeft(null);
    setSelectedRight(null);
    setHasSubmitted(false);
    setIsCorrect(false);
  };

  const getItemStyle = (item: string, side: "left" | "right") => {
    if (hasSubmitted) {
      // Build correct connections map
      const correctConnections: Record<string, string> = {};
      pairs.forEach(p => {
        const left = language === 'zh' && p.left_zh ? p.left_zh : p.left;
        const right = language === 'zh' && p.right_zh ? p.right_zh : p.right;
        correctConnections[left] = right;
      });

      if (side === "left") {
        const userConnection = connections[item];
        const correctConnection = correctConnections[item];
        if (userConnection === correctConnection) {
          return "border-success bg-success-soft/30";
        } else if (userConnection) {
          return "border-destructive bg-destructive/5";
        }
      } else {
        // Check if this right item is correctly connected
        const leftItem = Object.keys(connections).find(k => connections[k] === item);
        if (leftItem && correctConnections[leftItem] === item) {
          return "border-success bg-success-soft/30";
        } else if (leftItem) {
          return "border-destructive bg-destructive/5";
        }
      }
    }
    
    // Selection states
    if ((side === "left" && selectedLeft === item) || (side === "right" && selectedRight === item)) {
      return "border-primary bg-primary/10";
    }
    
    // Connected state
    if (side === "left" && connections[item]) {
      return "border-accent bg-accent-soft/30";
    }
    if (side === "right" && Object.values(connections).includes(item)) {
      return "border-accent bg-accent-soft/30";
    }
    
    return "border-border hover:bg-muted/50";
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
        Click items on the left and right to match them
      </div>

      {/* Matching Interface */}
      <div className="grid grid-cols-2 gap-4">
        {/* Left Column */}
        <div className="space-y-2">
          {leftItems.map((item, index) => (
            <motion.div
              key={item}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.05 }}
              onClick={() => handleLeftClick(item)}
              className={`p-3 rounded-lg border transition-all cursor-pointer ${getItemStyle(item, "left")}`}
            >
              <div className="flex items-center justify-between">
                <span className="text-sm">{item}</span>
                {connections[item] && (
                  <div className="flex items-center space-x-1">
                    <Link2 className="h-3 w-3 text-accent" />
                    {!hasSubmitted && (
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          removeConnection(item);
                        }}
                        className="text-muted-foreground hover:text-destructive"
                      >
                        <XCircle className="h-3 w-3" />
                      </button>
                    )}
                  </div>
                )}
              </div>
            </motion.div>
          ))}
        </div>

        {/* Right Column */}
        <div className="space-y-2">
          {shuffledRight.map((item, index) => (
            <motion.div
              key={item}
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.05 }}
              onClick={() => handleRightClick(item)}
              className={`p-3 rounded-lg border transition-all cursor-pointer ${getItemStyle(item, "right")}`}
            >
              <div className="flex items-center justify-between">
                <span className="text-sm">{item}</span>
                {Object.values(connections).includes(item) && (
                  <Link2 className="h-3 w-3 text-accent" />
                )}
              </div>
            </motion.div>
          ))}
        </div>
      </div>

      {/* Current Connections Display */}
      {Object.keys(connections).length > 0 && !hasSubmitted && (
        <div className="p-3 bg-muted/50 rounded-lg">
          <p className="text-sm font-medium mb-2">Your matches:</p>
          <div className="space-y-1">
            {Object.entries(connections).map(([left, right]) => (
              <div key={left} className="text-sm text-muted-foreground">
                {left} → {right}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Feedback */}
      {hasSubmitted && !isCorrect && (
        <motion.div
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          className="p-3 bg-muted rounded-lg"
        >
          <p className="text-sm font-medium mb-2">Correct matches:</p>
          <div className="space-y-1">
            {pairs.map((pair, index) => {
              const left = language === 'zh' && pair.left_zh ? pair.left_zh : pair.left;
              const right = language === 'zh' && pair.right_zh ? pair.right_zh : pair.right;
              return (
                <div key={index} className="text-sm text-foreground">
                  {left} → {right}
                </div>
              );
            })}
          </div>
        </motion.div>
      )}

      {/* Action Buttons */}
      <div className="flex space-x-2 pt-4">
        {!hasSubmitted ? (
          <Button
            onClick={handleSubmit}
            disabled={Object.keys(connections).length !== pairs.length}
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



