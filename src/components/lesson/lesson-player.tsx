import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { ChevronLeft, ChevronRight, PlayCircle } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { NumberLineReveal } from "@/components/animations/number-line-reveal";
import { TileCombine } from "@/components/animations/tile-combine";
import { ParticlesInStates } from "@/components/animations/particles-in-states";

interface Section {
  id: string;
  type: "text" | "math" | "animation" | "image" | "video";
  title: string;
  title_zh?: string;
  content: string;
  content_zh?: string;
  explanation?: string;
  explanation_zh?: string;
  props?: any;
}

interface LessonPlayerProps {
  sections: Section[];
  onComplete: () => void;
  chapterId: string;
  subjectId: string;
}

export function LessonPlayer({ sections, onComplete, chapterId, subjectId }: LessonPlayerProps) {
  const [currentSection, setCurrentSection] = useState(0);
  const { language, updateProgress } = useStore();
  const t = useTranslations(language);

  const section = sections[currentSection];
  const isLastSection = currentSection === sections.length - 1;
  const isFirstSection = currentSection === 0;

  const title = language === 'zh' && section?.title_zh ? section.title_zh : section?.title;
  const content = language === 'zh' && section?.content_zh ? section.content_zh : section?.content;
  const explanation = language === 'zh' && section?.explanation_zh ? section.explanation_zh : section?.explanation;

  const handleNext = () => {
    if (isLastSection) {
      // Mark lesson as completed
      updateProgress({
        subjectId,
        chapterId,
        sectionsCompleted: sections.map(s => s.id),
      });
      onComplete();
    } else {
      setCurrentSection(prev => prev + 1);
    }
  };

  const handlePrevious = () => {
    if (!isFirstSection) {
      setCurrentSection(prev => prev - 1);
    }
  };

  const renderSectionContent = () => {
    if (!section) return null;

    switch (section.type) {
      case "text":
        return (
          <div className="prose prose-lg max-w-none">
            <p className="text-foreground leading-relaxed">{content}</p>
            {explanation && (
              <div className="mt-4 p-4 bg-muted/50 rounded-lg">
                <p className="text-sm text-muted-foreground">{explanation}</p>
              </div>
            )}
          </div>
        );

      case "math":
        return (
          <div className="text-center">
            <div className="bg-muted/30 p-6 rounded-lg border-2 border-dashed border-primary/30">
              <div className="text-2xl font-mono text-primary mb-4">
                {content}
              </div>
              {explanation && (
                <p className="text-sm text-muted-foreground">{explanation}</p>
              )}
            </div>
          </div>
        );

      case "animation":
        return renderAnimation();

      default:
        return <p className="text-muted-foreground">Content type not supported yet.</p>;
    }
  };

  const renderAnimation = () => {
    switch (section.content) {
      case "NumberLineReveal":
        return <NumberLineReveal {...section.props} />;
      case "TileCombine":
        return <TileCombine {...section.props} />;
      case "ParticlesInStates":
        return <ParticlesInStates {...section.props} />;
      default:
        return (
          <div className="text-center p-8 bg-muted/30 rounded-lg">
            <PlayCircle className="h-16 w-16 mx-auto text-primary mb-4" />
            <p className="text-muted-foreground">Animation: {section.content}</p>
          </div>
        );
    }
  };

  return (
    <div className="max-w-4xl mx-auto">
      {/* Progress bar */}
      <div className="mb-6">
        <div className="flex items-center justify-between mb-2">
          <span className="text-sm text-muted-foreground">
            {t.lesson} {currentSection + 1} of {sections.length}
          </span>
          <Badge variant="outline">
            {Math.round(((currentSection + 1) / sections.length) * 100)}%
          </Badge>
        </div>
        <div className="w-full bg-muted rounded-full h-2">
          <motion.div
            className="bg-primary h-2 rounded-full"
            initial={{ width: 0 }}
            animate={{ width: `${((currentSection + 1) / sections.length) * 100}%` }}
            transition={{ duration: 0.3 }}
          />
        </div>
      </div>

      {/* Section content */}
      <AnimatePresence mode="wait">
        <motion.div
          key={currentSection}
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: -20 }}
          transition={{ duration: 0.3 }}
        >
          <Card className="lesson-card mb-6">
            <CardHeader>
              <CardTitle className="text-2xl">{title}</CardTitle>
            </CardHeader>
            <CardContent className="space-y-6">
              {renderSectionContent()}
            </CardContent>
          </Card>
        </motion.div>
      </AnimatePresence>

      {/* Navigation */}
      <div className="flex items-center justify-between">
        <Button
          variant="outline"
          onClick={handlePrevious}
          disabled={isFirstSection}
        >
          <ChevronLeft className="mr-2 h-4 w-4" />
          {t.previousSection}
        </Button>

        <div className="flex space-x-2">
          {sections.map((_, index) => (
            <button
              key={index}
              onClick={() => setCurrentSection(index)}
              className={`w-3 h-3 rounded-full transition-colors ${
                index === currentSection
                  ? 'bg-primary'
                  : index < currentSection
                  ? 'bg-success'
                  : 'bg-muted'
              }`}
            />
          ))}
        </div>

        <Button onClick={handleNext} className="btn-primary">
          {isLastSection ? t.startExercises : t.nextSection}
          <ChevronRight className="ml-2 h-4 w-4" />
        </Button>
      </div>
    </div>
  );
}