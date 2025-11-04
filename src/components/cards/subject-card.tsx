import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ProgressRing } from "@/components/ui/progress-ring";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { BookOpen, TrendingUp, Brain, Sparkles } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";

interface Subject {
  id: string;
  title: string;
  title_zh?: string;
  description: string;
  description_zh?: string;
  color: string;
  chapters: any[];
  isAIPlayground?: boolean;
}

interface SubjectCardProps {
  subject: Subject;
}

export function SubjectCard({ subject }: SubjectCardProps) {
  const { user, language, gradeLevel, getSubjectProgress, allUsersAIProgress } = useStore();
  const t = useTranslations(language);
  const navigate = useNavigate();

  // Special handling for AI Playground
  if (subject.isAIPlayground) {
    const aiModulesCount = 10; // Total AI modules
    const userId = user?.id;
    const userAIProgress = userId ? (allUsersAIProgress[userId] || {}) : {};
    const completedAI = Object.values(userAIProgress).filter(p => p.done).length;
    const aiProgressPercentage = aiModulesCount > 0 ? (completedAI / aiModulesCount) * 100 : 0;

    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3 }}
        whileHover={{ y: -4 }}
        className="h-full"
      >
        <Card className="lesson-card card-hover h-full bg-gradient-to-br from-purple-100 via-pink-100 to-blue-100 dark:from-purple-950/30 dark:via-pink-950/30 dark:to-blue-950/30 border-2 border-purple-300 dark:border-purple-700">
          <CardHeader className="pb-4">
            <div className="flex items-start justify-between">
              <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-purple-600 to-pink-600 text-white">
                <Brain className="h-6 w-6" />
              </div>
              <ProgressRing 
                progress={aiProgressPercentage} 
                size={50} 
                showPercentage 
                className="text-purple-600"
              />
            </div>
            <CardTitle className="text-xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
              {language === 'zh' && subject.title_zh ? subject.title_zh : subject.title}
            </CardTitle>
            <CardDescription className="text-sm text-gray-700 dark:text-gray-300">
              {language === 'zh' && subject.description_zh ? subject.description_zh : subject.description}
            </CardDescription>
          </CardHeader>
          
          <CardContent className="pt-0">
            <div className="space-y-4">
              <div className="flex items-center space-x-4 text-sm">
                <div className="flex items-center space-x-1">
                  <Sparkles className="h-4 w-4 text-purple-600" />
                  <span className="text-gray-600 dark:text-gray-400">
                    {completedAI}/{aiModulesCount} Modules
                  </span>
                </div>
              </div>
              
              <Button
                onClick={() => navigate('/ai')}
                className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white"
              >
                {completedAI > 0 ? 'Continue Learning' : 'Start Exploring'}
              </Button>
            </div>
          </CardContent>
        </Card>
      </motion.div>
    );
  }
  
  // Filter chapters by selected grade level
  const gradeChapters = subject.chapters.filter(ch => ch.gradeLevel === gradeLevel);
  const totalChapters = gradeChapters.length;

  const progress = getSubjectProgress(subject.id);
  // Only count completed chapters for current grade level
  const completedChapters = progress.filter(p => {
    const chapter = subject.chapters.find(ch => ch.id === p.chapterId);
    return p.completed && chapter?.gradeLevel === gradeLevel;
  }).length;
  const progressPercentage = totalChapters > 0 ? Math.min(100, (completedChapters / totalChapters) * 100) : 0;
  
  const title = language === 'zh' && subject.title_zh ? subject.title_zh : subject.title;
  const description = language === 'zh' && subject.description_zh ? subject.description_zh : subject.description;

  const getColorClasses = (color: string) => {
    switch (color) {
      case 'primary':
        return {
          icon: 'text-primary',
          gradient: 'from-primary/10 to-primary-soft',
          button: 'btn-primary'
        };
      case 'accent':
        return {
          icon: 'text-accent',
          gradient: 'from-accent/10 to-accent-soft',
          button: 'btn-accent'
        };
      default:
        return {
          icon: 'text-primary',
          gradient: 'from-primary/10 to-primary-soft',
          button: 'btn-primary'
        };
    }
  };

  const colors = getColorClasses(subject.color);

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      whileHover={{ y: -4 }}
      className="h-full"
    >
      <Card className={`lesson-card card-hover h-full bg-gradient-to-br ${colors.gradient}`}>
        <CardHeader className="pb-4">
          <div className="flex items-start justify-between">
            <div className={`flex h-12 w-12 items-center justify-center rounded-xl bg-background/80 ${colors.icon}`}>
              <BookOpen className="h-6 w-6" />
            </div>
            <ProgressRing 
              progress={progressPercentage} 
              size={50} 
              showPercentage 
              className={colors.icon}
            />
          </div>
          <CardTitle className="text-xl font-bold">{title}</CardTitle>
          <CardDescription className="text-sm text-muted-foreground">
            {description}
          </CardDescription>
        </CardHeader>
        
        <CardContent className="pt-0">
          <div className="space-y-4">
            {/* Progress stats */}
            <div className="flex items-center space-x-4 text-sm">
              <div className="flex items-center space-x-1">
                <TrendingUp className="h-4 w-4 text-muted-foreground" />
                <span className="text-muted-foreground">
                  {completedChapters}/{totalChapters} {t.chapters}
                </span>
              </div>
            </div>
            
            {/* Action button */}
            <Button
              onClick={() => navigate(`/subjects/${subject.id}`)}
              className={`w-full ${colors.button}`}
            >
              {completedChapters > 0 ? t.continueChapter : t.startLearning}
            </Button>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  );
}