import { useState, useEffect } from "react";
import { useParams, useNavigate, useSearchParams } from "react-router-dom";
import { AppHeader } from "@/components/layout/app-header";
import { LessonPlayer } from "@/components/lesson/lesson-player";
import { ExercisePlayer } from "@/components/exercises/exercise-player";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Badge } from "@/components/ui/badge";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { ArrowLeft, BookOpen, PenTool, Trophy, Clock, RotateCcw, X } from "lucide-react";
import { motion } from "framer-motion";
import contentData from "@/data/content.json";
import { useToast } from "@/hooks/use-toast";

export default function ChapterView() {
  const { subjectId, chapterId } = useParams();
  const navigate = useNavigate();
  const [searchParams, setSearchParams] = useSearchParams();
  const { user, language, getChapterProgress, updateProgress } = useStore();
  const t = useTranslations(language);
  const { toast } = useToast();

  const isReviewMode = searchParams.get('mode') === 'review';
  
  const [activeTab, setActiveTab] = useState<"lesson" | "exercises">("lesson");
  const [startTime, setStartTime] = useState<number>(Date.now());

  useEffect(() => {
    if (!user) {
      navigate('/login');
      return;
    }
    setStartTime(Date.now());
  }, [user, navigate]);

  if (!user || !subjectId || !chapterId) return null;

  const subject = contentData.subjects.find(s => s.id === subjectId);
  const chapter = subject?.chapters.find(c => c.id === chapterId);
  
  if (!subject || !chapter) {
    return (
      <div className="min-h-screen bg-background">
        <AppHeader />
        <main className="container mx-auto px-4 py-8 text-center">
          <h1 className="text-2xl font-bold mb-4">Chapter not found</h1>
          <Button onClick={() => navigate(`/subjects/${subjectId}`)}>
            Back to Subject
          </Button>
        </main>
      </div>
    );
  }

  const progress = getChapterProgress(subjectId, chapterId);
  const completedSections = progress?.sectionsCompleted || [];
  const completedExercises = progress?.exercisesCompleted || [];
  const exerciseScores = progress?.exerciseScores || {};
  
  const title = language === 'zh' && chapter.title_zh ? chapter.title_zh : chapter.title;
  const description = language === 'zh' && chapter.description_zh ? chapter.description_zh : chapter.description;
  const objectives = language === 'zh' && chapter.objectives_zh ? chapter.objectives_zh : chapter.objectives;

  const handleLessonComplete = () => {
    // In review mode, don't update progress
    if (isReviewMode) {
      toast({
        title: t.reviewCompleted || "📚 Lesson Reviewed!",
        description: t.reviewLessonDesc || "Keep practicing to reinforce your learning.",
      });
      setActiveTab("exercises");
      return;
    }

    const timeSpent = Math.floor((Date.now() - startTime) / 60000); // in minutes

    updateProgress({
      subjectId,
      chapterId,
      sectionsCompleted: chapter.sections.map(s => s.id),
      exercisesCompleted: progress?.exercisesCompleted || [],
      exerciseScores: progress?.exerciseScores || {},
      totalTimeSpent: (progress?.totalTimeSpent || 0) + timeSpent,
      lastAccessed: new Date().toISOString(),
    });

    toast({
      title: "🎉 Lesson Completed!",
      description: "Great job! Now try the exercises to reinforce your learning.",
    });

    setActiveTab("exercises");
  };

  const handleExerciseComplete = (scores: Record<string, number>) => {
    const timeSpent = Math.floor((Date.now() - startTime) / 60000);
    const allCompleted = chapter.exercises.every(e => scores[e.id] !== undefined);
    const averageScore = Object.values(scores).reduce((a, b) => a + b, 0) / Object.values(scores).length;

    // In review mode, show different message and don't update completion
    if (isReviewMode) {
      toast({
        title: averageScore >= 80 ? "🏆 Excellent Review!" : averageScore >= 60 ? "👍 Good Review!" : "💪 Keep Practicing!",
        description: `${t.reviewCompleted || 'Review completed!'} You scored ${Math.round(averageScore)}%.`,
      });
      return;
    }

    updateProgress({
      subjectId,
      chapterId,
      sectionsCompleted: progress?.sectionsCompleted || [],
      exercisesCompleted: Object.keys(scores),
      exerciseScores: { ...exerciseScores, ...scores },
      totalTimeSpent: (progress?.totalTimeSpent || 0) + timeSpent,
      lastAccessed: new Date().toISOString(),
      completed: allCompleted && completedSections.length === chapter.sections.length,
    });

    toast({
      title: averageScore >= 80 ? "🏆 Excellent!" : averageScore >= 60 ? "👍 Good job!" : "💪 Keep practicing!",
      description: `You scored ${Math.round(averageScore)}% on the exercises.`,
    });

    if (allCompleted) {
      // Navigate to next chapter or back to subject
      const currentChapterIndex = subject.chapters.findIndex(c => c.id === chapterId);
      if (currentChapterIndex < subject.chapters.length - 1) {
        const nextChapter = subject.chapters[currentChapterIndex + 1];
        navigate(`/subjects/${subjectId}/${nextChapter.id}`);
      } else {
        navigate(`/subjects/${subjectId}`);
      }
    }
  };

  const handleExitReviewMode = () => {
    searchParams.delete('mode');
    setSearchParams(searchParams);
  };

  const lessonProgress = (completedSections.length / chapter.sections.length) * 100;
  const exerciseProgress = (completedExercises.length / chapter.exercises.length) * 100;

  return (
    <div className="min-h-screen bg-background">
      <AppHeader />

      <main className="container mx-auto px-4 py-8">
        {/* Review Mode Banner */}
        {isReviewMode && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            className="mb-4 flex items-center justify-between bg-primary/10 border border-primary/20 rounded-lg px-4 py-3"
          >
            <div className="flex items-center space-x-2">
              <RotateCcw className="h-5 w-5 text-primary" />
              <div>
                <p className="font-medium text-primary">{t.reviewMode || 'Review Mode'}</p>
                <p className="text-sm text-muted-foreground">
                  {t.reviewModeDesc || 'Practice exercises to reinforce your learning. Progress won\'t affect completion status.'}
                </p>
              </div>
            </div>
            <Button
              variant="ghost"
              size="sm"
              onClick={handleExitReviewMode}
              className="text-primary hover:text-primary/80"
            >
              <X className="h-4 w-4 mr-1" />
              {t.exitReview || 'Exit Review'}
            </Button>
          </motion.div>
        )}

        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="mb-8"
        >
          <Button
            variant="ghost"
            onClick={() => navigate(`/subjects/${subjectId}`)}
            className="mb-4"
          >
            <ArrowLeft className="mr-2 h-4 w-4" />
            Back to {language === 'zh' && subject.title_zh ? subject.title_zh : subject.title}
          </Button>

          <Card className="lesson-card bg-gradient-to-br from-primary-soft/10 to-accent-soft/10">
            <CardHeader>
              <div className="flex items-start justify-between">
                <div>
                  <CardTitle className="text-2xl font-bold mb-2">{title}</CardTitle>
                  <CardDescription className="text-base">{description}</CardDescription>
                  
                  {/* Learning Objectives */}
                  <div className="mt-4">
                    <h4 className="text-sm font-medium text-foreground mb-2">{t.objectives}:</h4>
                    <ul className="text-sm text-muted-foreground space-y-1">
                      {objectives.map((objective, i) => (
                        <li key={i} className="flex items-start">
                          <span className="text-primary mr-2">✓</span>
                          <span>{objective}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
                
                {/* Progress Stats */}
                <div className="text-right space-y-2">
                  <Badge variant="outline" className="text-sm">
                    <BookOpen className="mr-1 h-3 w-3" />
                    {Math.round(lessonProgress)}% Lessons
                  </Badge>
                  <Badge variant="outline" className="text-sm">
                    <PenTool className="mr-1 h-3 w-3" />
                    {Math.round(exerciseProgress)}% Exercises
                  </Badge>
                  {progress?.totalTimeSpent && (
                    <Badge variant="secondary" className="text-sm">
                      <Clock className="mr-1 h-3 w-3" />
                      {progress.totalTimeSpent} min
                    </Badge>
                  )}
                </div>
              </div>
            </CardHeader>
          </Card>
        </motion.div>

        {/* Content Tabs */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
        >
          <Tabs value={activeTab} onValueChange={(v) => setActiveTab(v as "lesson" | "exercises")} className="space-y-6">
            <TabsList className="grid w-full max-w-md mx-auto grid-cols-2">
              <TabsTrigger value="lesson" className="flex items-center space-x-2">
                <BookOpen className="h-4 w-4" />
                <span>{t.lesson}</span>
                {lessonProgress === 100 && <Trophy className="h-3 w-3 text-success" />}
              </TabsTrigger>
              <TabsTrigger
                value="exercises"
                className="flex items-center space-x-2"
                disabled={!isReviewMode && completedSections.length === 0}
              >
                <PenTool className="h-4 w-4" />
                <span>{t.exercise}</span>
                {exerciseProgress === 100 && <Trophy className="h-3 w-3 text-success" />}
              </TabsTrigger>
            </TabsList>

            <TabsContent value="lesson" className="space-y-6">
              <LessonPlayer
                sections={chapter.sections}
                onComplete={handleLessonComplete}
                chapterId={chapterId}
                subjectId={subjectId}
              />
            </TabsContent>

            <TabsContent value="exercises" className="space-y-6">
              {(completedSections.length > 0 || isReviewMode) ? (
                <ExercisePlayer
                  exercises={chapter.exercises}
                  onComplete={handleExerciseComplete}
                  chapterId={chapterId}
                  subjectId={subjectId}
                  previousScores={exerciseScores}
                  isReviewMode={isReviewMode}
                />
              ) : (
                <Card className="text-center py-12">
                  <CardContent>
                    <BookOpen className="h-12 w-12 mx-auto text-muted-foreground mb-4" />
                    <h3 className="text-lg font-semibold mb-2">Complete the lesson first</h3>
                    <p className="text-muted-foreground mb-4">
                      You need to complete the lesson before attempting exercises.
                    </p>
                    <Button onClick={() => setActiveTab("lesson")} className="btn-primary">
                      Go to Lesson
                    </Button>
                  </CardContent>
                </Card>
              )}
            </TabsContent>
          </Tabs>
        </motion.div>
      </main>
    </div>
  );
}



