import { AppHeader } from "@/components/layout/app-header";
import { ChapterCard } from "@/components/cards/chapter-card";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { ArrowLeft, BookOpen, TrendingUp, Upload } from "lucide-react";
import { motion } from "framer-motion";
import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import contentData from "@/data";
import { ExamUpload } from "@/components/ExamUpload";
import { ContentReview } from "@/components/ContentReview";
import { aiContentStore, type AIGeneratedChapter } from "@/lib/ai-content-store";
import type { GeneratedContent } from "@/lib/azure-openai";

export default function SubjectDetail() {
  const { subjectId } = useParams();
  const { user, language, gradeLevel, getSubjectProgress, setCurrentSubject, _hasHydrated } = useStore();
  const t = useTranslations(language);
  const navigate = useNavigate();

  // AI exam upload state
  const [showUpload, setShowUpload] = useState(false);
  const [generatedContent, setGeneratedContent] = useState<GeneratedContent | null>(null);
  const [aiChapters, setAIChapters] = useState<AIGeneratedChapter[]>([]);

  useEffect(() => {
    // Wait for store to hydrate before checking authentication
    if (_hasHydrated && !user) {
      navigate('/login');
      return;
    }
    if (user && subjectId) {
      setCurrentSubject(subjectId);
    }
  }, [user, _hasHydrated, subjectId, navigate, setCurrentSubject]);

  // Load AI-generated chapters
  useEffect(() => {
    if (_hasHydrated && user && subjectId) {
      const chapters = aiContentStore.getChapters(user.id, subjectId);
      setAIChapters(chapters);
      console.log('Loaded AI chapters:', chapters.length, 'for user:', user.id, 'subject:', subjectId);
    }
  }, [_hasHydrated, user, subjectId]);

  if (!user || !subjectId) return null;

  const subject = contentData.subjects.find(s => s.id === subjectId);

  if (!subject) {
    return (
      <div className="min-h-screen bg-background">
        <AppHeader />
        <main className="container mx-auto px-4 py-8 text-center">
          <h1 className="text-2xl font-bold mb-4">Subject not found</h1>
          <Button onClick={() => navigate('/subjects')}>
            Back to Subjects
          </Button>
        </main>
      </div>
    );
  }

  // Filter chapters by selected grade level
  const filteredChapters = subject.chapters.filter(chapter => chapter.gradeLevel === gradeLevel);

  // Combine with AI-generated chapters for the same grade
  const aiChaptersForGrade = aiChapters.filter(ch => ch.gradeLevel === gradeLevel);
  const allChapters = [...filteredChapters, ...aiChaptersForGrade];

  const progress = getSubjectProgress(subjectId);
  const totalChapters = allChapters.length;
  const completedChapters = progress.filter(p =>
    p.completed && allChapters.some(ch => ch.id === p.chapterId)
  ).length;
  const progressPercentage = totalChapters > 0 ? (completedChapters / totalChapters) * 100 : 0;

  const title = language === 'zh' && subject.title_zh ? subject.title_zh : subject.title;
  const description = language === 'zh' && subject.description_zh ? subject.description_zh : subject.description;

  return (
    <div className="min-h-screen bg-background">
      <AppHeader />

      <main className="container mx-auto px-4 py-8">
        {/* Back Button */}
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.3 }}
          className="mb-6"
        >
          <Button
            variant="ghost"
            onClick={() => navigate('/subjects')}
            className="mb-4"
          >
            <ArrowLeft className="mr-2 h-4 w-4" />
            Back to Subjects
          </Button>
        </motion.div>

        {/* Subject Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="mb-8"
        >
          <Card className="lesson-card bg-gradient-to-br from-primary-soft/10 to-accent-soft/10">
            <CardHeader>
              <div className="flex items-start justify-between">
                <div className="flex items-center space-x-4">
                  <div className="flex h-16 w-16 items-center justify-center rounded-xl bg-primary text-primary-foreground">
                    <BookOpen className="h-8 w-8" />
                  </div>
                  <div>
                    <CardTitle className="text-3xl font-bold mb-2">{title}</CardTitle>
                    <CardDescription className="text-lg">
                      {description}
                    </CardDescription>
                  </div>
                </div>
                <div className="text-right">
                  <div className="text-2xl font-bold text-primary">
                    {Math.round(progressPercentage)}%
                  </div>
                  <div className="text-sm text-muted-foreground">
                    {t.completed}
                  </div>
                </div>
              </div>
            </CardHeader>
          </Card>
        </motion.div>

        {/* Upload Exam Button */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.1 }}
          className="mb-6"
        >
          <Button
            onClick={() => setShowUpload(true)}
            className="w-full sm:w-auto bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700"
          >
            <Upload className="mr-2 h-4 w-4" />
            {language === 'zh' ? '上传试卷' : 'Upload Exam Paper'}
          </Button>
          <p className="text-sm text-muted-foreground mt-2">
            {language === 'zh'
              ? 'AI 将分析试卷并创建学习内容'
              : 'AI will analyze your exam and create lesson content'}
          </p>
        </motion.div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Chapters Grid */}
          <div className="lg:col-span-2">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
            >
              <h2 className="text-2xl font-semibold mb-6">{t.chapters}</h2>
              {allChapters.length === 0 ? (
                <Card className="p-8 text-center">
                  <p className="text-muted-foreground">
                    {language === 'zh'
                      ? '此级别目前没有可用的章节。'
                      : 'No chapters available for this grade level yet.'}
                  </p>
                </Card>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {allChapters.map((chapter, index) => (
                    <ChapterCard
                      key={chapter.id}
                      chapter={chapter}
                      subjectId={subjectId}
                      index={index}
                      isAIGenerated={'isAIGenerated' in chapter && chapter.isAIGenerated}
                    />
                  ))}
                </div>
              )}
            </motion.div>
          </div>

          {/* Sidebar */}
          <div className="space-y-6">
            {/* Progress Summary */}
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6, delay: 0.3 }}
            >
              <h2 className="text-2xl font-semibold mb-6">{t.yourProgress}</h2>
              <Card className="lesson-card">
                <CardContent className="space-y-4 pt-6">
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-muted-foreground">{t.chaptersCompleted}</span>
                    <span className="font-medium">{completedChapters}/{totalChapters}</span>
                  </div>
                  <div className="w-full bg-muted rounded-full h-2">
                    <div
                      className="bg-primary h-2 rounded-full transition-all duration-300"
                      style={{ width: `${progressPercentage}%` }}
                    />
                  </div>
                  <div className="text-center">
                    <span className="text-2xl font-bold text-primary">
                      {Math.round(progressPercentage)}%
                    </span>
                    <p className="text-sm text-muted-foreground">Overall Progress</p>
                  </div>
                </CardContent>
              </Card>
            </motion.div>

            {/* Study Tips */}
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6, delay: 0.4 }}
            >
              <Card className="lesson-card bg-gradient-to-br from-accent-soft/50 to-primary-soft/50">
                <CardHeader>
                  <CardTitle>Study Tips</CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="text-sm space-y-2">
                    <li className="flex items-start">
                      <span className="text-accent mr-2">•</span>
                      {language === 'zh'
                        ? "完成课程后立即做练习以巩固学习"
                        : "Complete exercises immediately after lessons to reinforce learning"
                      }
                    </li>
                    <li className="flex items-start">
                      <span className="text-accent mr-2">•</span>
                      {language === 'zh'
                        ? "如果遇到困难，不要犹豫使用提示"
                        : "Don't hesitate to use hints if you're stuck"
                      }
                    </li>
                    <li className="flex items-start">
                      <span className="text-accent mr-2">•</span>
                      {language === 'zh'
                        ? "定期复习之前的章节以保持记忆"
                        : "Review previous chapters regularly to maintain retention"
                      }
                    </li>
                  </ul>
                </CardContent>
              </Card>
            </motion.div>
          </div>
        </div>

        {/* Upload Exam Modal - only show if no generated content */}
        {showUpload && !generatedContent && (
          <ExamUpload
            subject={subjectId}
            subjectTitle={title}
            gradeLevel={gradeLevel}
            onContentGenerated={(content) => {
              setShowUpload(false);
              // Small delay to ensure Upload modal is unmounted before Review modal renders
              setTimeout(() => {
                setGeneratedContent(content);
              }, 100);
            }}
            onClose={() => setShowUpload(false)}
          />
        )}

        {/* Content Review Modal - only show if there's generated content */}
        {generatedContent && !showUpload && (
          <ContentReview
            content={generatedContent}
            onSave={(content) => {
              // Save to AI content store
              console.log('Saving AI chapter:', content.chapterId, 'for user:', user.id, 'subject:', subjectId);
              const saved = aiContentStore.saveChapter(user.id, subjectId, content);
              console.log('Saved AI chapter:', saved);
              setAIChapters([...aiChapters, saved]);
              setGeneratedContent(null);

              // Show success message
              alert(language === 'zh' ? '章节已保存！' : 'Chapter saved successfully!');
            }}
            onCancel={() => setGeneratedContent(null)}
          />
        )}
      </main>
    </div>
  );
}