import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ProgressRing } from "@/components/ui/progress-ring";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { BookOpen, TrendingUp } from "lucide-react";
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
}

interface SubjectCardProps {
  subject: Subject;
}

export function SubjectCard({ subject }: SubjectCardProps) {
  const { language, getSubjectProgress } = useStore();
  const t = useTranslations(language);
  const navigate = useNavigate();
  
  const progress = getSubjectProgress(subject.id);
  const totalChapters = subject.chapters.length;
  const completedChapters = progress.filter(p => p.completed).length;
  const progressPercentage = totalChapters > 0 ? (completedChapters / totalChapters) * 100 : 0;
  
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