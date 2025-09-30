import { AppHeader } from "@/components/layout/app-header";
import { ChapterCard } from "@/components/cards/chapter-card";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { ArrowLeft, BookOpen, TrendingUp } from "lucide-react";
import { motion } from "framer-motion";
import { useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import contentData from "@/data/content.json";

export default function SubjectDetail() {
  const { subjectId } = useParams();
  const { user, language, getSubjectProgress, setCurrentSubject } = useStore();
  const t = useTranslations(language);
  const navigate = useNavigate();

  useEffect(() => {
    if (!user) {
      navigate('/login');
      return;
    }
    if (subjectId) {
      setCurrentSubject(subjectId);
    }
  }, [user, subjectId, navigate, setCurrentSubject]);

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

  const progress = getSubjectProgress(subjectId);
  const totalChapters = subject.chapters.length;
  const completedChapters = progress.filter(p => p.completed).length;
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

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Chapters Grid */}
          <div className="lg:col-span-2">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
            >
              <h2 className="text-2xl font-semibold mb-6">{t.chapters}</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {subject.chapters.map((chapter, index) => (
                  <ChapterCard
                    key={chapter.id}
                    chapter={chapter}
                    subjectId={subjectId}
                    index={index}
                  />
                ))}
              </div>
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
              <Card className="lesson-card">
                <CardHeader>
                  <CardTitle className="flex items-center space-x-2">
                    <TrendingUp className="h-5 w-5 text-primary" />
                    <span>{t.yourProgress}</span>
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
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
      </main>
    </div>
  );
}