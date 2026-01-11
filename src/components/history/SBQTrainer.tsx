import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Textarea } from '@/components/ui/textarea';
import { AlertCircle, CheckCircle2, Lightbulb, BookOpen, Sparkles, Loader2, TrendingUp } from 'lucide-react';
import { useStore } from '@/lib/store';
import { useTranslations } from '@/lib/i18n';
import { evaluateHumanitiesAnswer } from '@/lib/azure-humanities-evaluator';

interface SBQExercise {
  id: string;
  type: 'sbq';
  subtype: string; // inference, utility, reliability, comparison
  difficulty: string;
  source: string;
  sourceText: string;
  sourceText_zh: string;
  prompt: string;
  prompt_zh: string;
  answer: string;
  sampleAnswers?: string[];
  scaffolding?: string[];
  markingCriteria?: {
    level2?: string;
    level1?: string;
  };
  explanation?: string;
  explanation_zh?: string;
  useAIEvaluation?: boolean;
}

interface SBQTrainerProps {
  exercise: SBQExercise;
  onAnswer: (correct: boolean, score: number) => void;
  showHint?: boolean;
}

export default function SBQTrainer({ exercise, onAnswer, showHint = false }: SBQTrainerProps) {
  const { language } = useStore();
  const t = useTranslations(language);

  const [userAnswer, setUserAnswer] = useState('');
  const [showFeedback, setShowFeedback] = useState(false);
  const [showONPC, setShowONPC] = useState(false);
  const [hintLevel, setHintLevel] = useState(0);
  const [isEvaluating, setIsEvaluating] = useState(false);
  const [aiFeedback, setAIFeedback] = useState<{
    score: number;
    isCorrect: boolean;
    level?: 1 | 2;
    feedback: string;
    feedback_zh?: string;
    strengths?: string[];
    improvements?: string[];
  } | null>(null);

  const sourceText = language === 'zh' ? exercise.sourceText_zh : exercise.sourceText;
  const prompt = language === 'zh' ? exercise.prompt_zh : exercise.prompt;
  const explanation = language === 'zh' ? (exercise.explanation_zh || exercise.explanation) : exercise.explanation;

  const handleSubmit = async () => {
    if (!userAnswer.trim()) {
      return;
    }

    setIsEvaluating(true);

    try {
      // Use AI evaluation for SBQ questions
      const result = await evaluateHumanitiesAnswer({
        subject: 'history',
        questionType: exercise.subtype.startsWith('sbq') ? exercise.subtype : `sbq-${exercise.subtype}`,
        prompt: prompt,
        prompt_zh: exercise.prompt_zh,
        studentAnswer: userAnswer,
        modelAnswer: exercise.answer,
        sampleAnswers: exercise.sampleAnswers,
        sourceText: sourceText,
        markingCriteria: exercise.markingCriteria,
        gradeLevel: 'sec1',
        language: language
      });

      setAIFeedback(result);
      setIsEvaluating(false);
      setShowFeedback(true);
      onAnswer(result.isCorrect, result.score);
    } catch (error) {
      console.error('AI evaluation failed:', error);
      setIsEvaluating(false);

      // Fallback to simple keyword matching if AI fails
      const keywords = exercise.answer.toLowerCase().split(' ').filter(w => w.length > 3);
      const userWords = userAnswer.toLowerCase();
      const matchCount = keywords.filter(keyword => userWords.includes(keyword)).length;
      const matchRatio = matchCount / keywords.length;

      let score = 0;
      let correct = false;

      if (matchRatio > 0.7) {
        score = 100;
        correct = true;
      } else if (matchRatio > 0.4) {
        score = 60;
        correct = false;
      } else {
        score = 30;
        correct = false;
      }

      setShowFeedback(true);
      onAnswer(correct, score);
    }
  };

  const handleNextHint = () => {
    if (exercise.scaffolding && hintLevel < exercise.scaffolding.length) {
      setHintLevel(hintLevel + 1);
    }
  };

  const getSubtypeLabel = (subtype: string) => {
    const labels: Record<string, { en: string; zh: string }> = {
      inference: { en: 'Inference', zh: '推断' },
      utility: { en: 'Utility', zh: '实用性' },
      reliability: { en: 'Reliability', zh: '可靠性' },
      comparison: { en: 'Comparison', zh: '比较' },
      analysis: { en: 'Analysis', zh: '分析' }
    };
    return labels[subtype]?.[language] || subtype;
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <BookOpen className="h-5 w-5 text-[#8B1538]" />
          <h3 className="text-lg font-semibold">
            {language === 'en' ? 'Source-Based Question' : '基于来源的问题'}
          </h3>
        </div>
        <div className="flex gap-2">
          <Badge variant="outline" className="border-[#8B1538] text-[#8B1538]">
            {getSubtypeLabel(exercise.subtype)}
          </Badge>
          <Badge variant="secondary">
            {exercise.difficulty === 'easy' ? (language === 'en' ? 'Easy' : '简单') :
             exercise.difficulty === 'medium' ? (language === 'en' ? 'Medium' : '中等') :
             (language === 'en' ? 'Hard' : '困难')}
          </Badge>
        </div>
      </div>

      {/* Source Display */}
      <Card className="border-[#8B1538]/20">
        <CardHeader className="bg-[#8B1538]/5">
          <CardTitle className="text-base flex items-center justify-between">
            <span>{language === 'en' ? 'Source:' : '来源：'} {exercise.source}</span>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setShowONPC(!showONPC)}
              className="text-xs"
            >
              {showONPC
                ? (language === 'en' ? 'Hide ONPC' : '隐藏ONPC')
                : (language === 'en' ? 'Show ONPC Analysis' : '显示ONPC分析')
              }
            </Button>
          </CardTitle>
        </CardHeader>
        <CardContent className="pt-4">
          <blockquote className="border-l-4 border-[#8B1538] pl-4 italic text-muted-foreground">
            {sourceText}
          </blockquote>

          {/* ONPC Framework (collapsible) */}
          {showONPC && (
            <div className="mt-4 p-4 bg-muted/50 rounded-lg space-y-2 text-sm">
              <div className="font-semibold text-[#8B1538]">
                {language === 'en' ? 'ONPC Framework:' : 'ONPC框架：'}
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div>
                  <span className="font-medium">
                    {language === 'en' ? 'O - Origin:' : 'O - 来源：'}
                  </span>
                  <span className="ml-2 text-muted-foreground">
                    {language === 'en' ? 'WHO wrote it, WHEN' : '谁写的，什么时候'}
                  </span>
                </div>
                <div>
                  <span className="font-medium">
                    {language === 'en' ? 'N - Nature:' : 'N - 性质：'}
                  </span>
                  <span className="ml-2 text-muted-foreground">
                    {language === 'en' ? 'TYPE of source' : '来源的类型'}
                  </span>
                </div>
                <div>
                  <span className="font-medium">
                    {language === 'en' ? 'P - Purpose:' : 'P - 目的：'}
                  </span>
                  <span className="ml-2 text-muted-foreground">
                    {language === 'en' ? 'WHY it was created' : '为什么创建'}
                  </span>
                </div>
                <div>
                  <span className="font-medium">
                    {language === 'en' ? 'C - Content:' : 'C - 内容：'}
                  </span>
                  <span className="ml-2 text-muted-foreground">
                    {language === 'en' ? 'WHAT it says' : '它说什么'}
                  </span>
                </div>
              </div>
            </div>
          )}
        </CardContent>
      </Card>

      {/* Question */}
      <Card>
        <CardContent className="pt-6">
          <p className="font-medium mb-4">{prompt}</p>

          {/* Scaffolding/Hints */}
          {showHint && exercise.scaffolding && exercise.scaffolding.length > 0 && (
            <div className="mb-4 p-4 bg-blue-50 dark:bg-blue-950/20 rounded-lg border border-blue-200 dark:border-blue-800">
              <div className="flex items-start gap-2">
                <Lightbulb className="h-5 w-5 text-blue-600 flex-shrink-0 mt-0.5" />
                <div className="space-y-2 flex-1">
                  <p className="font-medium text-blue-900 dark:text-blue-100">
                    {language === 'en' ? 'Hints:' : '提示：'}
                  </p>
                  <ul className="space-y-1 text-sm">
                    {exercise.scaffolding.slice(0, hintLevel).map((hint, idx) => (
                      <li key={idx} className="flex items-start gap-2">
                        <span className="text-blue-600">•</span>
                        <span>{hint}</span>
                      </li>
                    ))}
                  </ul>
                  {hintLevel < exercise.scaffolding.length && (
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={handleNextHint}
                      className="text-blue-600 hover:text-blue-700"
                    >
                      {language === 'en' ? 'Show next hint' : '显示下一个提示'}
                    </Button>
                  )}
                </div>
              </div>
            </div>
          )}

          {/* Answer Input */}
          <Textarea
            value={userAnswer}
            onChange={(e) => setUserAnswer(e.target.value)}
            placeholder={language === 'en'
              ? 'Type your answer here... (2-3 sentences)'
              : '在这里输入你的答案...（2-3句话）'}
            className="min-h-[120px] mb-4"
            disabled={showFeedback}
          />

          {/* Submit Button */}
          {!showFeedback && (
            <Button
              onClick={handleSubmit}
              disabled={!userAnswer.trim() || isEvaluating}
              className="w-full bg-[#8B1538] hover:bg-[#6B1028]"
            >
              {isEvaluating ? (
                <>
                  <Loader2 className="h-4 w-4 mr-2 animate-spin" />
                  {language === 'en' ? 'AI Evaluating...' : 'AI评估中...'}
                </>
              ) : (
                language === 'en' ? 'Submit Answer' : '提交答案'
              )}
            </Button>
          )}

          {/* Feedback */}
          {showFeedback && (
            <div className="space-y-4">
              {/* AI Evaluation Badge */}
              {aiFeedback && (
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2 text-xs text-purple-600 dark:text-purple-400">
                    <Sparkles className="h-4 w-4" />
                    <span>AI-Powered Evaluation</span>
                  </div>
                  <div className="text-sm font-medium">
                    Score: {aiFeedback.score}% {aiFeedback.level && `• Level ${aiFeedback.level}`}
                  </div>
                </div>
              )}

              {/* Your Answer */}
              <div className="flex items-start gap-3 p-4 rounded-lg bg-green-50 dark:bg-green-950/20 border border-green-200 dark:border-green-800">
                <CheckCircle2 className="h-5 w-5 text-green-600 flex-shrink-0 mt-0.5" />
                <div className="flex-1">
                  <p className="font-medium text-green-900 dark:text-green-100 mb-2">
                    {language === 'en' ? 'Your Answer:' : '你的答案：'}
                  </p>
                  <p className="text-sm text-green-800 dark:text-green-200 italic">
                    "{userAnswer}"
                  </p>
                </div>
              </div>

              {/* AI Feedback */}
              {aiFeedback && (
                <>
                  {/* Feedback Message */}
                  <div className="p-4 rounded-lg bg-blue-50 dark:bg-blue-950/20 border border-blue-200 dark:border-blue-800">
                    <p className="font-medium text-blue-900 dark:text-blue-100 mb-2">
                      {language === 'en' ? 'Feedback:' : '反馈：'}
                    </p>
                    <p className="text-sm text-blue-800 dark:text-blue-200">
                      {language === 'zh' && aiFeedback.feedback_zh ? aiFeedback.feedback_zh : aiFeedback.feedback}
                    </p>
                  </div>

                  {/* Strengths */}
                  {aiFeedback.strengths && aiFeedback.strengths.length > 0 && (
                    <div className="p-4 rounded-lg bg-green-50 dark:bg-green-950/20 border border-green-200 dark:border-green-800">
                      <div className="flex items-center gap-2 mb-3">
                        <TrendingUp className="h-4 w-4 text-green-600" />
                        <p className="font-medium text-green-900 dark:text-green-100">
                          {language === 'zh' ? '优点' : 'Strengths'}
                        </p>
                      </div>
                      <ul className="space-y-2 text-sm text-green-800 dark:text-green-200">
                        {aiFeedback.strengths.map((strength, idx) => (
                          <li key={idx} className="flex items-start gap-2">
                            <span className="text-green-600 mt-1">✓</span>
                            <span>{strength}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {/* Improvements */}
                  {aiFeedback.improvements && aiFeedback.improvements.length > 0 && (
                    <div className="p-4 rounded-lg bg-orange-50 dark:bg-orange-950/20 border border-orange-200 dark:border-orange-800">
                      <div className="flex items-center gap-2 mb-3">
                        <Lightbulb className="h-4 w-4 text-orange-600" />
                        <p className="font-medium text-orange-900 dark:text-orange-100">
                          {language === 'zh' ? '改进建议' : 'Areas for Improvement'}
                        </p>
                      </div>
                      <ul className="space-y-2 text-sm text-orange-800 dark:text-orange-200">
                        {aiFeedback.improvements.map((improvement, idx) => (
                          <li key={idx} className="flex items-start gap-2">
                            <span className="text-orange-600 mt-1">•</span>
                            <span>{improvement}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                </>
              )}

              {/* Sample Answer */}
              <div className="p-4 rounded-lg bg-blue-50 dark:bg-blue-950/20 border border-blue-200 dark:border-blue-800">
                <p className="font-medium text-blue-900 dark:text-blue-100 mb-2">
                  {language === 'en' ? 'Sample Answer:' : '示例答案：'}
                </p>
                <p className="text-sm text-blue-800 dark:text-blue-200">
                  {exercise.answer}
                </p>
              </div>

              {/* Detailed Explanation */}
              {explanation && (
                <div className="p-4 rounded-lg bg-muted/50 border">
                  <div className="flex items-center gap-2 mb-2">
                    <AlertCircle className="h-4 w-4 text-[#8B1538]" />
                    <p className="font-medium text-[#8B1538]">
                      {language === 'en' ? 'Detailed Explanation:' : '详细解释：'}
                    </p>
                  </div>
                  <div className="prose prose-sm max-w-none dark:prose-invert">
                    {explanation.split('\n\n').map((para, idx) => (
                      <p key={idx} className="mb-2 text-sm">{para}</p>
                    ))}
                  </div>
                </div>
              )}

              {/* Marking Criteria */}
              {exercise.markingCriteria && (
                <div className="p-4 rounded-lg bg-purple-50 dark:bg-purple-950/20 border border-purple-200 dark:border-purple-800 text-sm">
                  <p className="font-medium text-purple-900 dark:text-purple-100 mb-2">
                    {language === 'en' ? 'Marking Criteria:' : '评分标准：'}
                  </p>
                  <ul className="space-y-1 text-purple-800 dark:text-purple-200">
                    {exercise.markingCriteria.level2 && (
                      <li>✓ Level 2: {exercise.markingCriteria.level2}</li>
                    )}
                    {exercise.markingCriteria.level1 && (
                      <li>○ Level 1: {exercise.markingCriteria.level1}</li>
                    )}
                  </ul>
                </div>
              )}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
