import { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom";
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
import { EquationBalance } from "@/components/animations/equation-balance";
import { FractionVisual } from "@/components/animations/fraction-visual";
import { ForceMotion } from "@/components/animations/force-motion";
import ParabolaGraph from "@/components/animations/ParabolaGraph";
import LinearGraphInteractive from "@/components/animations/LinearGraphInteractive";
import OscillatingSpring from "@/components/animations/OscillatingSpring";
import ElectricFieldVisualizer from "@/components/animations/ElectricFieldVisualizer";
import ACWaveformVisualizer from "@/components/animations/ACWaveformVisualizer";
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

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
  const [searchParams, setSearchParams] = useSearchParams();

  // Get current section from URL params, default to 0
  const sectionParam = searchParams.get('section');
  const initialSection = sectionParam ? parseInt(sectionParam, 10) : 0;
  const validInitialSection = Math.max(0, Math.min(initialSection, sections.length - 1));

  const [currentSection, setCurrentSection] = useState(validInitialSection);
  const { language, updateProgress } = useStore();
  const t = useTranslations(language);

  // Update URL when section changes
  useEffect(() => {
    setSearchParams({ section: currentSection.toString() }, { replace: true });
  }, [currentSection, setSearchParams]);

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
          <div className="prose prose-lg max-w-none dark:prose-invert text-foreground">
            <ReactMarkdown
              remarkPlugins={[remarkGfm, remarkMath]}
              rehypePlugins={[rehypeKatex]}
              components={{
                p: ({ children }) => <p className="mb-4 leading-relaxed">{children}</p>,
                h1: ({ children }) => <h1 className="text-2xl font-bold mb-4 mt-6">{children}</h1>,
                h2: ({ children }) => <h2 className="text-xl font-bold mb-3 mt-5">{children}</h2>,
                h3: ({ children }) => <h3 className="text-lg font-bold mb-2 mt-4">{children}</h3>,
                strong: ({ children }) => <strong className="font-bold text-primary">{children}</strong>,
                ul: ({ children }) => <ul className="list-disc list-inside mb-4 space-y-2">{children}</ul>,
                ol: ({ children }) => <ol className="list-decimal list-inside mb-4 space-y-2">{children}</ol>,
                li: ({ children }) => <li className="ml-4">{children}</li>,
                table: ({ children }) => <table className="min-w-full border-collapse border border-border my-4">{children}</table>,
                thead: ({ children }) => <thead className="bg-muted">{children}</thead>,
                tbody: ({ children }) => <tbody>{children}</tbody>,
                tr: ({ children }) => <tr className="border-b border-border">{children}</tr>,
                th: ({ children }) => <th className="border border-border px-4 py-2 text-left font-semibold">{children}</th>,
                td: ({ children }) => <td className="border border-border px-4 py-2">{children}</td>,
                code: ({ children }) => <code className="bg-muted px-1.5 py-0.5 rounded text-sm font-mono">{children}</code>,
                pre: ({ children }) => <pre className="bg-muted p-4 rounded-lg overflow-x-auto my-4">{children}</pre>,
              }}
            >
              {content}
            </ReactMarkdown>
            {explanation && (
              <div className="mt-4 p-4 bg-muted/50 rounded-lg text-sm text-muted-foreground">
                <ReactMarkdown
                  remarkPlugins={[remarkGfm, remarkMath]}
                  rehypePlugins={[rehypeKatex]}
                >
                  {explanation}
                </ReactMarkdown>
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
                <div className="text-sm text-muted-foreground text-left">
                  <ReactMarkdown
                    remarkPlugins={[remarkGfm, remarkMath]}
                    rehypePlugins={[rehypeKatex]}
                    components={{
                      p: ({ children }) => <p className="mb-3">{children}</p>,
                      strong: ({ children }) => <strong className="font-bold text-primary">{children}</strong>,
                    }}
                  >
                    {explanation}
                  </ReactMarkdown>
                </div>
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
      case "EquationBalance":
        return <EquationBalance {...section.props} />;
      case "FractionVisual":
        return <FractionVisual {...section.props} />;
      case "ForceMotion":
        return <ForceMotion {...section.props} />;
      case "ParabolaGraph":
        return <ParabolaGraph {...section.props} />;
      case "LinearGraphInteractive":
        return <LinearGraphInteractive {...section.props} />;
      case "OscillatingSpring":
        return <OscillatingSpring {...section.props} />;
      case "ElectricFieldVisualizer":
        return <ElectricFieldVisualizer {...section.props} />;
      case "ACWaveformVisualizer":
        return <ACWaveformVisualizer {...section.props} />;
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
              className={`w-3 h-3 rounded-full transition-colors ${index === currentSection
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