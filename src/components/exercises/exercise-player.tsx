import { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from "@/components/ui/dialog";
import { useStore, VoteDifficulty } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { azureOpenAIService } from "@/lib/azure-openai";
import { ChevronLeft, ChevronRight, CheckCircle, XCircle, HelpCircle, ThumbsUp, Flame, AlertTriangle, Sparkles, Loader2, AlertCircle } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { MCQExercise } from "./mcq-exercise";
import { ShortAnswerExercise } from "./short-answer-exercise";
import { DragOrderExercise } from "./drag-order-exercise";
import { MatchingExercise } from "./matching-exercise";
import confetti from "canvas-confetti";
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

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

interface SimilarQuestion {
  id: string;
  type: 'mcq' | 'multi' | 'short';
  prompt: string;
  prompt_zh: string;
  choices?: string[];
  choices_zh?: string[];
  answer: number | string;
  explanation: string;
  explanation_zh: string;
}

interface ExercisePlayerProps {
  exercises: Exercise[];
  onComplete: (scores: Record<string, number>) => void;
  chapterId: string;
  subjectId: string;
  gradeLevel?: string;
  previousScores?: Record<string, number>;
}

export function ExercisePlayer({
  exercises,
  onComplete,
  chapterId,
  subjectId,
  gradeLevel,
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
  const { language, voteExercise, getExerciseVote } = useStore();
  const t = useTranslations(language);

  // Similar Questions state
  const [showSimilarModal, setShowSimilarModal] = useState(false);
  const [similarQuestions, setSimilarQuestions] = useState<SimilarQuestion[]>([]);
  const [isGeneratingSimilar, setIsGeneratingSimilar] = useState(false);
  const [similarError, setSimilarError] = useState<string | null>(null);
  const [practiceAnswers, setPracticeAnswers] = useState<Record<string, number | string | null>>({});
  const [practiceResults, setPracticeResults] = useState<Record<string, boolean>>({});

  // Update URL when exercise changes
  useEffect(() => {
    setSearchParams({ exercise: currentExercise.toString() }, { replace: true });
  }, [currentExercise, setSearchParams]);

  const exercise = exercises[currentExercise];
  const isLastExercise = currentExercise === exercises.length - 1;
  const isFirstExercise = currentExercise === 0;

  // Get current vote for this exercise (must be after exercise is defined)
  const currentVote = getExerciseVote(subjectId, chapterId, exercise?.id || '');

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

  const handleVote = (vote: VoteDifficulty) => {
    if (exercise) {
      voteExercise(subjectId, chapterId, exercise.id, vote);
    }
  };

  const handleGenerateSimilar = async () => {
    if (!exercise) return;

    setSimilarQuestions([]);
    setPracticeAnswers({});
    setPracticeResults({});
    setSimilarError(null);
    setShowSimilarModal(true);

    if (!azureOpenAIService.isConfigured()) {
      setSimilarError(t.aiNotConfigured || 'AI is not configured. Please set up Azure OpenAI.');
      return;
    }

    setIsGeneratingSimilar(true);

    try {
      const questions = await azureOpenAIService.generateSimilarQuestions(
        {
          prompt: language === 'zh' && exercise.prompt_zh ? exercise.prompt_zh : exercise.prompt,
          type: exercise.type,
          choices: language === 'zh' && exercise.choices_zh ? exercise.choices_zh : exercise.choices,
          answer: exercise.answer,
          explanation: language === 'zh' && exercise.explanation_zh ? exercise.explanation_zh : exercise.explanation
        },
        subjectId,
        gradeLevel,
        3
      );

      setSimilarQuestions(questions);
    } catch (error) {
      console.error('Error generating similar questions:', error);
      setSimilarError(error instanceof Error ? error.message : 'Failed to generate questions');
    } finally {
      setIsGeneratingSimilar(false);
    }
  };

  const handlePracticeAnswer = (questionId: string, answer: number | string) => {
    setPracticeAnswers(prev => ({ ...prev, [questionId]: answer }));

    const question = similarQuestions.find(q => q.id === questionId);
    if (question) {
      const isCorrect = question.answer === answer;
      setPracticeResults(prev => ({ ...prev, [questionId]: isCorrect }));
    }
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
      subjectId,
      gradeLevel,
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
              {/* Title and Vote Buttons Row */}
              <div className="flex items-center justify-between mb-3">
                <CardTitle className="text-xl">
                  {t.question} {currentExercise + 1}
                </CardTitle>

                <div className="flex items-center gap-2">
                  <span className="text-sm text-muted-foreground">
                    {language === 'zh' ? '难度评价：' : 'Rate difficulty:'}
                  </span>
                  <Button
                    variant={currentVote === 'easy' ? 'default' : 'outline'}
                    size="sm"
                    onClick={() => handleVote('easy')}
                    className="gap-1.5"
                  >
                    <ThumbsUp className="h-4 w-4" />
                    {language === 'zh' ? '简单' : 'Easy'}
                  </Button>
                  <Button
                    variant={currentVote === 'hard' ? 'default' : 'outline'}
                    size="sm"
                    onClick={() => handleVote('hard')}
                    className="gap-1.5"
                  >
                    <Flame className="h-4 w-4" />
                    {language === 'zh' ? '困难' : 'Hard'}
                  </Button>
                  <Button
                    variant={currentVote === 'issue' ? 'default' : 'outline'}
                    size="sm"
                    onClick={() => handleVote('issue')}
                    className="gap-1.5"
                  >
                    <AlertTriangle className="h-4 w-4" />
                    {language === 'zh' ? '有问题' : 'Issue'}
                  </Button>
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

              {/* Question Prompt */}
              <div className="text-base text-foreground prose prose-sm max-w-none dark:prose-invert">
                <ReactMarkdown
                  remarkPlugins={[remarkGfm, remarkMath]}
                  rehypePlugins={[rehypeKatex]}
                >
                  {prompt}
                </ReactMarkdown>
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
                    <div className="flex-1">
                      <p className="font-medium text-sm mb-1">{t.hint}</p>
                      <div className="text-sm text-muted-foreground prose prose-sm max-w-none dark:prose-invert">
                        <ReactMarkdown
                          remarkPlugins={[remarkGfm, remarkMath]}
                          rehypePlugins={[rehypeKatex]}
                        >
                          {hint}
                        </ReactMarkdown>
                      </div>
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
                    <div className="flex-1">
                      <p className="font-medium text-sm mb-1">{t.explanation}</p>
                      <div className="text-sm text-muted-foreground prose prose-sm max-w-none dark:prose-invert">
                        <ReactMarkdown
                          remarkPlugins={[remarkGfm, remarkMath]}
                          rehypePlugins={[rehypeKatex]}
                        >
                          {explanation}
                        </ReactMarkdown>
                      </div>
                    </div>
                  </div>
                </motion.div>
              )}

              {/* Similar Questions Button - shows after answering */}
              {scores[exercise.id] !== undefined && (
                <motion.div
                  initial={{ opacity: 0, y: -10 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="flex justify-center pt-2"
                >
                  <Button
                    variant="outline"
                    onClick={handleGenerateSimilar}
                    className="gap-2 border-primary text-primary hover:bg-primary/10"
                  >
                    <Sparkles className="h-4 w-4" />
                    {t.similarQuestions || 'Similar Questions'}
                  </Button>
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

      {/* Similar Questions Modal */}
      <Dialog open={showSimilarModal} onOpenChange={setShowSimilarModal}>
        <DialogContent className="max-w-3xl max-h-[80vh] overflow-y-auto">
          <DialogHeader>
            <DialogTitle className="flex items-center gap-2">
              <Sparkles className="h-5 w-5 text-primary" />
              {t.similarQuestions || 'Similar Questions'}
            </DialogTitle>
            <DialogDescription>
              {t.generateSimilar || 'Practice with similar questions to reinforce your learning'}
            </DialogDescription>
          </DialogHeader>

          <div className="space-y-6 mt-4">
            {/* Original Question */}
            {exercise && (
              <div className="p-4 bg-muted/50 rounded-lg">
                <p className="font-medium text-sm mb-2">{t.originalQuestion || 'Original Question'}</p>
                <div className="text-sm prose prose-sm max-w-none dark:prose-invert">
                  <ReactMarkdown
                    remarkPlugins={[remarkGfm, remarkMath]}
                    rehypePlugins={[rehypeKatex]}
                  >
                    {prompt}
                  </ReactMarkdown>
                </div>
              </div>
            )}

            {/* Loading State */}
            {isGeneratingSimilar && (
              <div className="flex items-center justify-center py-12">
                <Loader2 className="h-8 w-8 animate-spin text-primary mr-3" />
                <span className="text-muted-foreground">{t.generatingSimilar || 'Generating similar questions...'}</span>
              </div>
            )}

            {/* Error State */}
            {similarError && (
              <div className="flex items-center gap-3 p-4 bg-destructive/10 border border-destructive/20 rounded-lg">
                <AlertCircle className="h-5 w-5 text-destructive" />
                <p className="text-destructive">{similarError}</p>
              </div>
            )}

            {/* Similar Questions */}
            {similarQuestions.length > 0 && (
              <div className="space-y-4">
                <h3 className="font-semibold">{t.practiceMore || 'Practice More'}</h3>
                {similarQuestions.map((question, index) => {
                  const questionPrompt = language === 'zh' ? question.prompt_zh : question.prompt;
                  const questionChoices = language === 'zh' ? question.choices_zh : question.choices;
                  const questionExplanation = language === 'zh' ? question.explanation_zh : question.explanation;
                  const hasAnswered = practiceAnswers[question.id] !== undefined;
                  const isCorrect = practiceResults[question.id];

                  return (
                    <Card key={question.id} className={`${hasAnswered ? (isCorrect ? 'border-success/50' : 'border-destructive/50') : ''}`}>
                      <CardHeader>
                        <CardTitle className="text-base flex items-center gap-2">
                          {t.question} {index + 1}
                          {hasAnswered && (
                            isCorrect
                              ? <CheckCircle className="h-5 w-5 text-success" />
                              : <XCircle className="h-5 w-5 text-destructive" />
                          )}
                        </CardTitle>
                        <div className="prose prose-sm max-w-none dark:prose-invert">
                          <ReactMarkdown
                            remarkPlugins={[remarkGfm, remarkMath]}
                            rehypePlugins={[rehypeKatex]}
                          >
                            {questionPrompt}
                          </ReactMarkdown>
                        </div>
                      </CardHeader>
                      <CardContent className="space-y-3">
                        {/* MCQ Choices */}
                        {question.type === 'mcq' && questionChoices && (
                          <div className="space-y-2">
                            {questionChoices.map((choice, choiceIndex) => (
                              <button
                                key={choiceIndex}
                                onClick={() => handlePracticeAnswer(question.id, choiceIndex)}
                                disabled={hasAnswered}
                                className={`w-full text-left p-3 rounded-lg border transition-colors ${
                                  hasAnswered
                                    ? choiceIndex === question.answer
                                      ? 'bg-success/20 border-success'
                                      : practiceAnswers[question.id] === choiceIndex
                                      ? 'bg-destructive/20 border-destructive'
                                      : 'bg-muted/50'
                                    : 'hover:bg-muted/50 cursor-pointer'
                                }`}
                              >
                                <div className="flex items-center gap-2">
                                  <span className="font-medium">
                                    {String.fromCharCode(65 + choiceIndex)}.
                                  </span>
                                  <span>{choice}</span>
                                </div>
                              </button>
                            ))}
                          </div>
                        )}

                        {/* Explanation after answering */}
                        {hasAnswered && questionExplanation && (
                          <motion.div
                            initial={{ opacity: 0, y: -10 }}
                            animate={{ opacity: 1, y: 0 }}
                            className={`p-4 rounded-lg ${isCorrect ? 'bg-success/10 border border-success/20' : 'bg-destructive/10 border border-destructive/20'}`}
                          >
                            <p className="font-medium text-sm mb-2">{t.explanation}</p>
                            <div className="text-sm prose prose-sm max-w-none dark:prose-invert">
                              <ReactMarkdown
                                remarkPlugins={[remarkGfm, remarkMath]}
                                rehypePlugins={[rehypeKatex]}
                              >
                                {questionExplanation}
                              </ReactMarkdown>
                            </div>
                          </motion.div>
                        )}
                      </CardContent>
                    </Card>
                  );
                })}
              </div>
            )}
          </div>

          <div className="flex justify-end mt-4">
            <Button variant="outline" onClick={() => setShowSimilarModal(false)}>
              {t.close || 'Close'}
            </Button>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}



