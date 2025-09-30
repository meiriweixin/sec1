import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { ProgressRing } from "@/components/ui/progress-ring";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { Play, CheckCircle, Clock } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";

interface Chapter {
  id: string;
  title: string;
  title_zh?: string;
  description: string;
  description_zh?: string;
  objectives: string[];
  objectives_zh?: string[];
  sections: any[];
  exercises: any[];
}

interface ChapterCardProps {
  chapter: Chapter;
  subjectId: string;
  index: number;
}

export function ChapterCard({ chapter, subjectId, index }: ChapterCardProps) {
  const { language, getChapterProgress } = useStore();
  const t = useTranslations(language);
  const navigate = useNavigate();
  
  const progress = getChapterProgress(subjectId, chapter.id);
  const totalSections = chapter.sections.length;
  const totalExercises = chapter.exercises.length;
  const completedSections = progress?.sectionsCompleted.length || 0;
  const completedExercises = progress?.exercisesCompleted.length || 0;
  
  const sectionProgress = totalSections > 0 ? (completedSections / totalSections) * 100 : 0;
  const exerciseProgress = totalExercises > 0 ? (completedExercises / totalExercises) * 100 : 0;
  const overallProgress = ((sectionProgress + exerciseProgress) / 2);
  
  const title = language === 'zh' && chapter.title_zh ? chapter.title_zh : chapter.title;
  const description = language === 'zh' && chapter.description_zh ? chapter.description_zh : chapter.description;
  const objectives = language === 'zh' && chapter.objectives_zh ? chapter.objectives_zh : chapter.objectives;

  const getStatus = () => {
    if (progress?.completed) return 'completed';
    if (completedSections > 0 || completedExercises > 0) return 'inProgress';
    return 'notStarted';
  };

  const status = getStatus();

  const getStatusBadge = () => {
    switch (status) {
      case 'completed':
        return <Badge className="bg-success text-success-foreground">{t.completed}</Badge>;
      case 'inProgress':
        return <Badge className="bg-warning text-warning-foreground">{t.inProgress}</Badge>;
      default:
        return <Badge variant="secondary">{t.notStarted}</Badge>;
    }
  };

  const getStatusIcon = () => {
    switch (status) {
      case 'completed':
        return <CheckCircle className="h-5 w-5 text-success" />;
      case 'inProgress':
        return <Clock className="h-5 w-5 text-warning" />;
      default:
        return <Play className="h-5 w-5 text-primary" />;
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3, delay: index * 0.1 }}
      whileHover={{ y: -2 }}
      className="h-full"
    >
      <Card className="lesson-card card-hover h-full">
        <CardHeader className="pb-4">
          <div className="flex items-start justify-between">
            <div className="flex-1">
              <div className="flex items-center space-x-2 mb-2">
                {getStatusIcon()}
                {getStatusBadge()}
              </div>
              <CardTitle className="text-lg font-semibold mb-1">{title}</CardTitle>
              <CardDescription className="text-sm text-muted-foreground">
                {description}
              </CardDescription>
            </div>
            <ProgressRing 
              progress={overallProgress} 
              size={50} 
              showPercentage 
              className="text-primary ml-4"
            />
          </div>
        </CardHeader>
        
        <CardContent className="pt-0">
          <div className="space-y-4">
            {/* Learning objectives */}
            <div>
              <h4 className="text-sm font-medium text-foreground mb-2">{t.objectives}:</h4>
              <ul className="text-xs text-muted-foreground space-y-1">
                {objectives.slice(0, 3).map((objective, i) => (
                  <li key={i} className="flex items-start">
                    <span className="text-primary mr-2">•</span>
                    <span>{objective}</span>
                  </li>
                ))}
                {objectives.length > 3 && (
                  <li className="text-xs text-muted-foreground/60">
                    +{objectives.length - 3} more...
                  </li>
                )}
              </ul>
            </div>
            
            {/* Progress breakdown */}
            <div className="grid grid-cols-2 gap-2 text-xs">
              <div className="text-center p-2 bg-muted/50 rounded">
                <div className="font-medium">{completedSections}/{totalSections}</div>
                <div className="text-muted-foreground">Lessons</div>
              </div>
              <div className="text-center p-2 bg-muted/50 rounded">
                <div className="font-medium">{completedExercises}/{totalExercises}</div>
                <div className="text-muted-foreground">Exercises</div>
              </div>
            </div>
            
            {/* Action button */}
            <Button
              onClick={() => navigate(`/subjects/${subjectId}/${chapter.id}`)}
              className="w-full btn-primary"
            >
              {status === 'completed' ? 'Review' : status === 'inProgress' ? t.continueChapter : t.startChapter}
            </Button>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  );
}