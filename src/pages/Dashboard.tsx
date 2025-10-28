import { AppHeader } from "@/components/layout/app-header";
import { SubjectCard } from "@/components/cards/subject-card";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { TrendingUp, Clock, Award, ArrowRight } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { useEffect } from "react";
import contentData from "@/data/content.json";

export default function Dashboard() {
  const { user, language, gradeLevel, progress, _hasHydrated } = useStore();
  const t = useTranslations(language);
  const navigate = useNavigate();

  useEffect(() => {
    // Wait for store to hydrate before checking authentication
    if (_hasHydrated && !user) {
      navigate('/login');
    }
  }, [user, _hasHydrated, navigate]);

  if (!user) return null;

  const subjects = contentData.subjects;

  // Filter chapters by selected grade level
  const totalChapters = subjects.reduce((acc, subject) => {
    const gradeChapters = subject.chapters.filter(ch => ch.gradeLevel === gradeLevel);
    return acc + gradeChapters.length;
  }, 0);

  // Only count completed chapters for current grade level
  const completedChapters = progress.filter(p => {
    const subject = subjects.find(s => s.id === p.subjectId);
    const chapter = subject?.chapters.find(ch => ch.id === p.chapterId);
    return p.completed && chapter?.gradeLevel === gradeLevel;
  }).length;
  const totalTimeSpent = progress.reduce((acc, p) => acc + (p.totalTimeSpent || 0), 0);
  const recentActivity = progress
    .sort((a, b) => new Date(b.lastAccessed).getTime() - new Date(a.lastAccessed).getTime())
    .slice(0, 3);

  const formatTime = (minutes: number) => {
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    if (hours > 0) {
      return `${hours}h ${mins}m`;
    }
    return `${mins}m`;
  };

  return (
    <div className="min-h-screen bg-background">
      <AppHeader />
      
      <main className="container mx-auto px-4 py-8">
        {/* Welcome Section */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="mb-8"
        >
          <h1 className="text-3xl font-bold mb-2">
            {language === 'zh' ? `欢迎回来，${user.name}！` : `Welcome back, ${user.name}!`}
          </h1>
          <p className="text-muted-foreground">
            {t.welcomeMessage}
          </p>
        </motion.div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main Content */}
          <div className="lg:col-span-2 space-y-8">
            {/* Subjects Grid */}
            <section>
              <div className="flex items-center justify-between mb-6">
                <div>
                  <h2 className="text-2xl font-semibold">{t.subjects}</h2>
                  <p className="text-sm text-muted-foreground mt-1">
                    {gradeLevel === 'sec1' && (language === 'zh' ? '中一' : 'Secondary 1')}
                    {gradeLevel === 'sec2' && (language === 'zh' ? '中二' : 'Secondary 2')}
                    {gradeLevel === 'sec3' && (language === 'zh' ? '中三' : 'Secondary 3')}
                    {gradeLevel === 'sec4' && (language === 'zh' ? '中四' : 'Secondary 4')}
                    {gradeLevel === 'jc1' && 'JC 1'}
                    {gradeLevel === 'jc2' && 'JC 2'}
                  </p>
                </div>
                <Button
                  variant="outline"
                  onClick={() => navigate('/subjects')}
                >
                  View All
                  <ArrowRight className="ml-2 h-4 w-4" />
                </Button>
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {subjects.map((subject, index) => (
                  <motion.div
                    key={subject.id}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.3, delay: index * 0.1 }}
                  >
                    <SubjectCard subject={subject} />
                  </motion.div>
                ))}
              </div>
            </section>

            {/* Recent Activity */}
            {recentActivity.length > 0 && (
              <section>
                <h2 className="text-2xl font-semibold mb-6">{t.recentActivity}</h2>
                <div className="space-y-3">
                  {recentActivity.map((activity) => {
                    const subject = subjects.find(s => s.id === activity.subjectId);
                    const chapter = subject?.chapters.find(c => c.id === activity.chapterId);
                    
                    if (!subject || !chapter) return null;
                    
                    const title = language === 'zh' && chapter.title_zh ? chapter.title_zh : chapter.title;
                    const subjectTitle = language === 'zh' && subject.title_zh ? subject.title_zh : subject.title;
                    
                    return (
                      <motion.div
                        key={`${activity.subjectId}-${activity.chapterId}`}
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ duration: 0.3 }}
                      >
                        <Card className="lesson-card card-hover">
                          <CardContent className="p-4">
                            <div className="flex items-center justify-between">
                              <div>
                                <h3 className="font-medium">{title}</h3>
                                <p className="text-sm text-muted-foreground">{subjectTitle}</p>
                              </div>
                              <div className="text-right">
                                <Button
                                  variant="outline"
                                  size="sm"
                                  onClick={() => navigate(`/subjects/${activity.subjectId}/${activity.chapterId}`)}
                                >
                                  {t.continueWhere}
                                </Button>
                              </div>
                            </div>
                          </CardContent>
                        </Card>
                      </motion.div>
                    );
                  })}
                </div>
              </section>
            )}
          </div>

          {/* Sidebar */}
          <div className="space-y-6">
            {/* Progress Stats */}
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
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
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-muted-foreground">{t.timeSpent}</span>
                    <span className="font-medium">{formatTime(totalTimeSpent)}</span>
                  </div>
                  <Button
                    onClick={() => navigate('/progress')}
                    className="w-full"
                    variant="outline"
                  >
                    {t.progress}
                  </Button>
                </CardContent>
              </Card>
            </motion.div>

            {/* Quick Actions */}
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6, delay: 0.3 }}
            >
              <Card className="lesson-card">
                <CardHeader>
                  <CardTitle className="flex items-center space-x-2">
                    <Award className="h-5 w-5 text-accent" />
                    <span>Quick Start</span>
                  </CardTitle>
                  <CardDescription>
                    {t.chooseSubject}
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-2">
                    {subjects.map((subject) => (
                      <Button
                        key={subject.id}
                        onClick={() => navigate(`/subjects/${subject.id}`)}
                        variant="outline"
                        className="w-full justify-start"
                      >
                        {language === 'zh' && subject.title_zh ? subject.title_zh : subject.title}
                        <ArrowRight className="ml-auto h-4 w-4" />
                      </Button>
                    ))}
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
              <Card className="lesson-card bg-gradient-to-br from-accent-soft to-primary-soft">
                <CardHeader>
                  <CardTitle className="flex items-center space-x-2">
                    <Clock className="h-5 w-5 text-accent" />
                    <span>Study Tip</span>
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-sm">
                    {language === 'zh' 
                      ? "每天学习20-30分钟比一次性学习几个小时更有效。保持一致性是成功的关键！"
                      : "Studying 20-30 minutes daily is more effective than cramming for hours. Consistency is key to success!"
                    }
                  </p>
                </CardContent>
              </Card>
            </motion.div>
          </div>
        </div>
      </main>
    </div>
  );
}