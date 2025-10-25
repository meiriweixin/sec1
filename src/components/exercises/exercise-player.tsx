import { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { ChevronLeft, ChevronRight, CheckCircle, XCircle, HelpCircle } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { MCQExercise } from "./mcq-exercise";
import { ShortAnswerExercise } from "./short-answer-exercise";
import { DragOrderExercise } from "./drag-order-exercise";
import { MatchingExercise } from "./matching-exercise";
import confetti from "canvas-confetti";

interface Exercise {
  id: string;
  type: "mcq" | "short" | "drag-order" | "match" | "multi";
  prompt: string;
  prompt_zh?: string;
  choices?: string[];
  choices_zh?: string[];
  answer: any;
  answer_zh?: any;
  hint?: string;
  hint_zh?: string;
  explanation?: string;
  explanation_zh?: string;
  items?: string[];
  items_zh?: string[];
  pairs?: [string, string][];
  pairs_zh?: [string, string][];
  validator?: string;
}

interface ExercisePlayerProps {
  exercises: Exercise[];
  onComplete: (scores: Record<string, number>) => void;
  chapterId: string;
  subjectId: string;
  previousScores?: Record<string, number>;
}

export function ExercisePlayer({
  exercises,
  onComplete,
  chapterId,
  subjectId,
  previousScores = {}
}: ExercisePlayerProps) {
  const [searchParams, setSearchParams] = useSearchParams();

  // Get current exercise from URL params, default to 0
  const exerciseParam = searchParams.get('exercise');
  const initialExercise = exerciseParam ? parseInt(exerciseParam, 10) : 0;
  const validInitialExercise = Math.max(0, Math.min(initialExercise, exercises.length - 1));

  const [currentExercise, setCurrentExercise] = useState(validInitialExercise);
  const [scores, setScores] = useState<Record<string, number>>(previousScores);
  const [attempts, setAttempts] = useState<Record<string, number>>({});
  const [showHint, setShowHint] = useState(false);
  const [showExplanation, setShowExplanation] = useState(false);
  const { language } = useStore();
  const t = useTranslations(language);

  // Update URL when exercise changes
  useEffect(() => {
    setSearchParams({ exercise: currentExercise.toString() }, { replace: true });
  }, [currentExercise, setSearchParams]);

  const exercise = exercises[currentExercise];
  const isLastExercise = currentExercise === exercises.length - 1;
  const isFirstExercise = currentExercise === 0;

  const prompt = language === 'zh' && exercise?.prompt_zh ? exercise.prompt_zh : exercise?.prompt;
  const hint = language === 'zh' && exercise?.hint_zh ? exercise.hint_zh : exercise?.hint;
  const explanation = language === 'zh' && exercise?.explanation_zh ? exercise.explanation_zh : exercise?.explanation;

  const handleAnswer = (isCorrect: boolean, userAnswer?: any) => {
    const exerciseId = exercise.id;
    const attemptCount = (attempts[exerciseId] || 0) + 1;
    setAttempts({ ...attempts, [exerciseId]: attemptCount });

    if (isCorrect) {
      // Calculate score based on attempts (100% for first try, 80% for second, 60% for third+)
      const score = attemptCount === 1 ? 100 : attemptCount === 2 ? 80 : 60;
      setScores({ ...scores, [exerciseId]: score });
      setShowExplanation(true);
      
      // Celebration animation for perfect score
      if (score === 100) {
        confetti({
          particleCount: 100,
          spread: 70,
          origin: { y: 0.6 }
        });
      }
    } else {
      // Show hint after first failed attempt
      if (attemptCount === 1) {
        setShowHint(true);
      }
    }
  };

  const handleNext = () => {
    if (isLastExercise) {
      // Complete all exercises
      onComplete(scores);
    } else {
      setCurrentExercise(prev => prev + 1);
      setShowHint(false);
      setShowExplanation(false);
    }
  };

  const handlePrevious = () => {
    if (!isFirstExercise) {
      setCurrentExercise(prev => prev - 1);
      setShowHint(false);
      setShowExplanation(false);
    }
  };

  const handleSkip = () => {
    // Mark as 0 score and move to next
    setScores({ ...scores, [exercise.id]: 0 });
    handleNext();
  };

  const renderExercise = () => {
    if (!exercise) return null;

    const commonProps = {
      exercise,
      onAnswer: handleAnswer,
      showHint,
      showExplanation,
      attempts: attempts[exercise.id] || 0,
      previousScore: scores[exercise.id],
    };

    switch (exercise.type) {
      case "mcq":
      case "multi":
        return <MCQExercise {...commonProps} />;
      case "short":
        return <ShortAnswerExercise {...commonProps} />;
      case "drag-order":
        return <DragOrderExercise {...commonProps} />;
      case "match":
        return <MatchingExercise {...commonProps} />;
      default:
        return <p className="text-muted-foreground">Exercise type not supported yet.</p>;
    }
  };

  const completedCount = Object.keys(scores).length;
  const progressPercentage = (completedCount / exercises.length) * 100;
  const averageScore = completedCount > 0 
    ? Object.values(scores).reduce((a, b) => a + b, 0) / completedCount 
    : 0;

  return (
    <div className="max-w-4xl mx-auto">
      {/* Progress Header */}
      <div className="mb-6">
        <div className="flex items-center justify-between mb-2">
          <span className="text-sm text-muted-foreground">
            {t.exercise} {currentExercise + 1} of {exercises.length}
          </span>
          <div className="flex items-center space-x-2">
            <Badge variant="outline">
              {Math.round(averageScore)}% Average
            </Badge>
            <Badge variant={scores[exercise.id] ? "default" : "secondary"}>
              {scores[exercise.id] ? `${scores[exercise.id]}%` : "Not attempted"}
            </Badge>
          </div>
        </div>
        <Progress value={progressPercentage} className="h-2" />
      </div>

      {/* Exercise Content */}
      <AnimatePresence mode="wait">
        <motion.div
          key={currentExercise}
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: -20 }}
          transition={{ duration: 0.3 }}
        >
          <Card className="lesson-card mb-6">
            <CardHeader>
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <CardTitle className="text-xl mb-2">
                    {t.question} {currentExercise + 1}
                  </CardTitle>
                  <p className="text-base text-foreground">{prompt}</p>
                </div>
                {scores[exercise.id] !== undefined && (
                  <div className="ml-4">
                    {scores[exercise.id] >= 80 ? (
                      <CheckCircle className="h-6 w-6 text-success" />
                    ) : scores[exercise.id] >= 60 ? (
                      <CheckCircle className="h-6 w-6 text-warning" />
                    ) : (
                      <XCircle className="h-6 w-6 text-destructive" />
                    )}
                  </div>
                )}
              </div>
            </CardHeader>
            <CardContent className="space-y-6">
              {renderExercise()}
              
              {/* Hint Section */}
              {showHint && hint && (
                <motion.div
                  initial={{ opacity: 0, y: -10 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="p-4 bg-warning-soft rounded-lg border border-warning/20"
                >
                  <div className="flex items-start space-x-2">
                    <HelpCircle className="h-5 w-5 text-warning mt-0.5" />
                    <div>
                      <p className="font-medium text-sm mb-1">{t.hint}</p>
                      <p className="text-sm text-muted-foreground">{hint}</p>
                    </div>
                  </div>
                </motion.div>
              )}
              
              {/* Explanation Section */}
              {showExplanation && explanation && (
                <motion.div
                  initial={{ opacity: 0, y: -10 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="p-4 bg-success-soft rounded-lg border border-success/20"
                >
                  <div className="flex items-start space-x-2">
                    <CheckCircle className="h-5 w-5 text-success mt-0.5" />
                    <div>
                      <p className="font-medium text-sm mb-1">{t.explanation}</p>
                      <p className="text-sm text-muted-foreground">{explanation}</p>
                    </div>
                  </div>
                </motion.div>
              )}
            </CardContent>
          </Card>
        </motion.div>
      </AnimatePresence>

      {/* Navigation */}
      <div className="flex items-center justify-between">
        <Button
          variant="outline"
          onClick={handlePrevious}
          disabled={isFirstExercise}
        >
          <ChevronLeft className="mr-2 h-4 w-4" />
          {t.previous}
        </Button>

        <div className="flex space-x-2">
          {exercises.map((_, index) => (
            <button
              key={index}
              onClick={() => {
                setCurrentExercise(index);
                setShowHint(false);
                setShowExplanation(false);
              }}
              className={`w-3 h-3 rounded-full transition-colors ${
                index === currentExercise
                  ? 'bg-primary'
                  : scores[exercises[index].id] !== undefined
                  ? 'bg-success'
                  : 'bg-muted'
              }`}
            />
          ))}
        </div>

        <div className="flex space-x-2">
          {!scores[exercise.id] && (
            <Button
              variant="outline"
              onClick={handleSkip}
            >
              Skip
            </Button>
          )}
          <Button 
            onClick={handleNext} 
            className="btn-primary"
            disabled={!scores[exercise.id] && !isLastExercise}
          >
            {isLastExercise ? t.complete : t.next}
            <ChevronRight className="ml-2 h-4 w-4" />
          </Button>
        </div>
      </div>
    </div>
  );
}



