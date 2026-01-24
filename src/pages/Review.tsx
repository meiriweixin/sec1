import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { AppHeader } from "@/components/layout/app-header";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from "@/components/ui/dialog";
import { useStore, ReviewStatus } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { azureOpenAIService } from "@/lib/azure-openai";
import { ArrowLeft, BookOpen, CheckCircle2, Eye, Sparkles, Loader2, XCircle, AlertCircle } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import contentData from "@/data";

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
  pairs?: { left: string; right: string; left_zh?: string; right_zh?: string }[];
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

export default function Review() {
  const { subjectId, chapterId } = useParams();
  const navigate = useNavigate();
  const {
    user,
    language,
    _hasHydrated,
    gradeLevel,
    getWrongAnswers,
    getWrongAnswerStatus,
    setWrongAnswerStatus,
    getChapterProgress
  } = useStore();
  const t = useTranslations(language);

  const [selectedExercise, setSelectedExercise] = useState<Exercise | null>(null);
  const [similarQuestions, setSimilarQuestions] = useState<SimilarQuestion[]>([]);
  const [isGenerating, setIsGenerating] = useState(false);
  const [generationError, setGenerationError] = useState<string | null>(null);
  const [showSimilarModal, setShowSimilarModal] = useState(false);
  const [practiceAnswers, setPracticeAnswers] = useState<Record<string, number | string | null>>({});
  const [practiceResults, setPracticeResults] = useState<Record<string, boolean>>({});

  useEffect(() => {
    if (_hasHydrated && !user) {
      navigate('/login');
    }
  }, [user, _hasHydrated, navigate]);

  if (!user || !subjectId || !chapterId) return null;

  // Find subject and chapter
  const subject = contentData.subjects.find(s => s.id === subjectId);
  const chapter = subject?.chapters.find(c => c.id === chapterId);

  if (!subject || !chapter) {
    return (
      <div className="min-h-screen bg-background">
        <AppHeader />
        <main className="container mx-auto px-4 py-8">
          <p className="text-muted-foreground">{t.error}</p>
        </main>
      </div>
    );
  }

  // Get wrong answers for this chapter
  const wrongAnswerIds = getWrongAnswers(subjectId, chapterId);
  const wrongExercises = (chapter.exercises as Exercise[]).filter(
    ex => wrongAnswerIds.includes(ex.id)
  );

  const chapterProgress = getChapterProgress(subjectId, chapterId);
  const subjectTitle = language === 'zh' && subject.title_zh ? subject.title_zh : subject.title;
  const chapterTitle = language === 'zh' && chapter.title_zh ? chapter.title_zh : chapter.title;

  const handleMarkStatus = (exerciseId: string, status: ReviewStatus) => {
    setWrongAnswerStatus(subjectId, chapterId, exerciseId, status);
  };

  const getStatusForExercise = (exerciseId: string): ReviewStatus | null => {
    return getWrongAnswerStatus(subjectId, chapterId, exerciseId);
  };

  const handleGenerateSimilar = async (exercise: Exercise) => {
    setSelectedExercise(exercise);
    setSimilarQuestions([]);
    setPracticeAnswers({});
    setPracticeResults({});
    setGenerationError(null);
    setShowSimilarModal(true);

    if (!azureOpenAIService.isConfigured()) {
      setGenerationError(t.aiNotConfigured);
      return;
    }

    setIsGenerating(true);

    try {
      const prompt = language === 'zh' && exercise.prompt_zh ? exercise.prompt_zh : exercise.prompt;
      const choices = language === 'zh' && exercise.choices_zh ? exercise.choices_zh : exercise.choices;
      const explanation = language === 'zh' && exercise.explanation_zh ? exercise.explanation_zh : exercise.explanation;

      const questions = await azureOpenAIService.generateSimilarQuestions(
        {
          prompt,
          type: exercise.type,
          choices,
          answer: exercise.answer,
          explanation
        },
        subject.title,
        gradeLevel,
        3
      );

      setSimilarQuestions(questions);
    } catch (error) {
      console.error('Error generating similar questions:', error);
      setGenerationError(error instanceof Error ? error.message : 'Failed to generate questions');
    } finally {
      setIsGenerating(false);
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

  const getScoreForExercise = (exerciseId: string): number => {
    return chapterProgress?.exerciseScores?.[exerciseId] ?? 0;
  };

  return (
    <div className="min-h-screen bg-background">
      <AppHeader />

      <main className="container mx-auto px-4 py-8">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.3 }}
          className="mb-8"
        >
          <Button
            variant="ghost"
            onClick={() => navigate(`/subjects/${subjectId}/${chapterId}`)}
            className="mb-4"
          >
            <ArrowLeft className="mr-2 h-4 w-4" />
            {t.backToChapter}
          </Button>

          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold flex items-center gap-3">
                <BookOpen className="h-8 w-8 text-primary" />
                {t.wrongAnswers}
              </h1>
              <p className="text-muted-foreground mt-2">
                {subjectTitle} • {chapterTitle}
              </p>
              <p className="text-sm text-muted-foreground mt-1">
                {t.reviewWrongAnswers}
              </p>
            </div>
            <Badge variant="outline" className="text-lg px-4 py-2">
              {wrongExercises.length} {language === 'zh' ? '道错题' : 'wrong answers'}
            </Badge>
          </div>
        </motion.div>

        {/* Wrong Answers List */}
        {wrongExercises.length === 0 ? (
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.3 }}
          >
            <Card className="text-center py-12">
              <CardContent>
                <CheckCircle2 className="h-16 w-16 text-success mx-auto mb-4" />
                <h2 className="text-2xl font-semibold mb-2">{t.noWrongAnswers}</h2>
                <p className="text-muted-foreground">{t.allCorrect}</p>
                <Button
                  className="mt-6"
                  onClick={() => navigate(`/subjects/${subjectId}/${chapterId}`)}
                >
                  {t.backToChapter}
                </Button>
              </CardContent>
            </Card>
          </motion.div>
        ) : (
          <div className="space-y-6">
            <AnimatePresence>
              {wrongExercises.map((exercise, index) => {
                const status = getStatusForExercise(exercise.id);
                const score = getScoreForExercise(exercise.id);
                const prompt = language === 'zh' && exercise.prompt_zh ? exercise.prompt_zh : exercise.prompt;
                const explanation = language === 'zh' && exercise.explanation_zh ? exercise.explanation_zh : exercise.explanation;

                return (
                  <motion.div
                    key={exercise.id}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -20 }}
                    transition={{ duration: 0.3, delay: index * 0.05 }}
                  >
                    <Card className={`lesson-card ${status === 'understood' ? 'border-success/50 bg-success/5' : status === 'reviewing' ? 'border-warning/50 bg-warning/5' : ''}`}>
                      <CardHeader>
                        <div className="flex items-start justify-between">
                          <div className="flex-1">
                            <div className="flex items-center gap-3 mb-2">
                              <Badge variant="secondary">
                                {t.question} {index + 1}
                              </Badge>
                              <Badge variant="outline" className={score >= 60 ? 'text-warning' : 'text-destructive'}>
                                {score}%
                              </Badge>
                              {status === 'reviewing' && (
                                <Badge variant="outline" className="text-warning border-warning">
                                  <Eye className="h-3 w-3 mr-1" />
                                  {t.reviewing}
                                </Badge>
                              )}
                              {status === 'understood' && (
                                <Badge variant="outline" className="text-success border-success">
                                  <CheckCircle2 className="h-3 w-3 mr-1" />
                                  {t.understood}
                                </Badge>
                              )}
                            </div>
                            <div className="prose prose-sm max-w-none dark:prose-invert">
                              <ReactMarkdown
                                remarkPlugins={[remarkGfm, remarkMath]}
                                rehypePlugins={[rehypeKatex]}
                              >
                                {prompt}
                              </ReactMarkdown>
                            </div>
                          </div>
                        </div>
                      </CardHeader>
                      <CardContent className="space-y-4">
                        {/* Explanation */}
                        {explanation && (
                          <div className="p-4 bg-muted/50 rounded-lg">
                            <p className="font-medium text-sm mb-2">{t.explanation}</p>
                            <div className="text-sm text-muted-foreground prose prose-sm max-w-none dark:prose-invert">
                              <ReactMarkdown
                                remarkPlugins={[remarkGfm, remarkMath]}
                                rehypePlugins={[rehypeKatex]}
                              >
                                {explanation}
                              </ReactMarkdown>
                            </div>
                          </div>
                        )}

                        {/* Action Buttons */}
                        <div className="flex flex-wrap gap-3">
                          <Button
                            variant={status === 'reviewing' ? 'default' : 'outline'}
                            size="sm"
                            onClick={() => handleMarkStatus(exercise.id, 'reviewing')}
                            className="gap-2"
                          >
                            <Eye className="h-4 w-4" />
                            {t.markReviewing}
                          </Button>
                          <Button
                            variant={status === 'understood' ? 'default' : 'outline'}
                            size="sm"
                            onClick={() => handleMarkStatus(exercise.id, 'understood')}
                            className="gap-2"
                          >
                            <CheckCircle2 className="h-4 w-4" />
                            {t.markUnderstood}
                          </Button>
                          <Button
                            variant="outline"
                            size="sm"
                            onClick={() => handleGenerateSimilar(exercise)}
                            className="gap-2 border-primary text-primary hover:bg-primary/10"
                          >
                            <Sparkles className="h-4 w-4" />
                            {t.similarQuestions}
                          </Button>
                        </div>
                      </CardContent>
                    </Card>
                  </motion.div>
                );
              })}
            </AnimatePresence>
          </div>
        )}
      </main>

      {/* Similar Questions Modal */}
      <Dialog open={showSimilarModal} onOpenChange={setShowSimilarModal}>
        <DialogContent className="max-w-3xl max-h-[80vh] overflow-y-auto">
          <DialogHeader>
            <DialogTitle className="flex items-center gap-2">
              <Sparkles className="h-5 w-5 text-primary" />
              {t.similarQuestions}
            </DialogTitle>
            <DialogDescription>
              {t.generateSimilar}
            </DialogDescription>
          </DialogHeader>

          <div className="space-y-6 mt-4">
            {/* Original Question */}
            {selectedExercise && (
              <div className="p-4 bg-muted/50 rounded-lg">
                <p className="font-medium text-sm mb-2">{t.originalQuestion}</p>
                <div className="text-sm prose prose-sm max-w-none dark:prose-invert">
                  <ReactMarkdown
                    remarkPlugins={[remarkGfm, remarkMath]}
                    rehypePlugins={[rehypeKatex]}
                  >
                    {language === 'zh' && selectedExercise.prompt_zh
                      ? selectedExercise.prompt_zh
                      : selectedExercise.prompt}
                  </ReactMarkdown>
                </div>
              </div>
            )}

            {/* Loading State */}
            {isGenerating && (
              <div className="flex items-center justify-center py-12">
                <Loader2 className="h-8 w-8 animate-spin text-primary mr-3" />
                <span className="text-muted-foreground">{t.generatingSimilar}</span>
              </div>
            )}

            {/* Error State */}
            {generationError && (
              <div className="flex items-center gap-3 p-4 bg-destructive/10 border border-destructive/20 rounded-lg">
                <AlertCircle className="h-5 w-5 text-destructive" />
                <p className="text-destructive">{generationError}</p>
              </div>
            )}

            {/* Similar Questions */}
            {similarQuestions.length > 0 && (
              <div className="space-y-4">
                <h3 className="font-semibold">{t.practiceMore}</h3>
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
                              ? <CheckCircle2 className="h-5 w-5 text-success" />
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
                                className={`w-full text-left p-3 rounded-lg border transition-colors ${hasAnswered
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
              {t.close}
            </Button>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}
