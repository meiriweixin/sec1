import { AppHeader } from "@/components/layout/app-header";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { motion } from "framer-motion";
import { useEffect, useState, useRef } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import {
  ArrowLeft,
  Clock,
  Calculator,
  FileText,
  Printer,
  Download,
  Eye,
  EyeOff,
  CheckCircle
} from "lucide-react";
import html2pdf from "html2pdf.js";
import examsData from "@/data/exams.json";
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import remarkGfm from 'remark-gfm';

// Import exam content
import wa1Content from "@/data/exam-content/wa1.json";
import wa2Content from "@/data/exam-content/wa2.json";
import wa3Content from "@/data/exam-content/wa3.json";
import eoyP1Content from "@/data/exam-content/eoy-p1.json";
import eoyP2Content from "@/data/exam-content/eoy-p2.json";

// Import Science exam content
import scienceWa1Content from "@/data/exam-content/sec1-science-wa1.json";
import scienceWa2Content from "@/data/exam-content/sec1-science-wa2.json";
import scienceWa3Content from "@/data/exam-content/sec1-science-wa3.json";
import scienceEoyContent from "@/data/exam-content/sec1-science-eoy.json";

// Import History exam content
import historyWa1Content from "@/data/exam-content/sec1-history-wa1.json";
import historyWa2Content from "@/data/exam-content/sec1-history-wa2.json";
import historyWa3Content from "@/data/exam-content/sec1-history-wa3.json";
import historyEoyContent from "@/data/exam-content/sec1-history-eoy.json";

// Import Geography exam content
import geographyWa1Content from "@/data/exam-content/sec1-geography-wa1.json";
import geographyWa2Content from "@/data/exam-content/sec1-geography-wa2.json";
import geographyWa3Content from "@/data/exam-content/sec1-geography-wa3.json";
import geographyEoyContent from "@/data/exam-content/sec1-geography-eoy.json";

// Import English exam content
import englishWa1Content from "@/data/exam-content/sec1-english-wa1.json";
import englishWa2Content from "@/data/exam-content/sec1-english-wa2.json";
import englishWa3Content from "@/data/exam-content/sec1-english-wa3.json";
import englishEoyContent from "@/data/exam-content/sec1-english-eoy.json";

// Import Chinese exam content
import chineseWa1Content from "@/data/exam-content/sec1-chinese-wa1.json";
import chineseWa2Content from "@/data/exam-content/sec1-chinese-wa2.json";
import chineseWa3Content from "@/data/exam-content/sec1-chinese-wa3.json";
import chineseEoyContent from "@/data/exam-content/sec1-chinese-eoy.json";

interface ExamContent {
  id: string;
  instructions: string[];
  instructions_zh?: string[];
  sections: {
    name: string;
    name_zh?: string;
    marks: number;
    questions: Question[];
  }[];
  answerKey?: {
    sectionName: string;
    answers: { questionNum: string; answer: string }[];
  }[];
}

interface Question {
  number: number;
  marks: number;
  prompt: string;
  prompt_zh?: string;
  type: 'mcq' | 'short' | 'structured' | 'short_answer' | 'composition' | 'mcq_group';
  choices?: { label: string; text: string; text_zh?: string }[];
  parts?: { label: string; marks: number; prompt: string; prompt_zh?: string }[];
  diagram?: string;
  passage?: string;
}

const examContents: Record<string, ExamContent> = {
  'sec1-math-wa1': wa1Content as ExamContent,
  'sec1-math-wa2': wa2Content as ExamContent,
  'sec1-math-wa3': wa3Content as ExamContent,
  'sec1-math-eoy-p1': eoyP1Content as ExamContent,
  'sec1-math-eoy-p2': eoyP2Content as ExamContent,
  // Science exams
  'sec1-science-wa1': scienceWa1Content as ExamContent,
  'sec1-science-wa2': scienceWa2Content as ExamContent,
  'sec1-science-wa3': scienceWa3Content as ExamContent,
  'sec1-science-eoy': scienceEoyContent as ExamContent,
  // History exams
  'sec1-history-wa1': historyWa1Content as ExamContent,
  'sec1-history-wa2': historyWa2Content as ExamContent,
  'sec1-history-wa3': historyWa3Content as ExamContent,
  'sec1-history-eoy': historyEoyContent as ExamContent,
  // Geography exams
  'sec1-geography-wa1': geographyWa1Content as ExamContent,
  'sec1-geography-wa2': geographyWa2Content as ExamContent,
  'sec1-geography-wa3': geographyWa3Content as ExamContent,
  'sec1-geography-eoy': geographyEoyContent as ExamContent,
  // English exams
  'sec1-english-wa1': englishWa1Content as ExamContent,
  'sec1-english-wa2': englishWa2Content as ExamContent,
  'sec1-english-wa3': englishWa3Content as ExamContent,
  'sec1-english-eoy': englishEoyContent as ExamContent,
  // Chinese exams
  'sec1-chinese-wa1': chineseWa1Content as ExamContent,
  'sec1-chinese-wa2': chineseWa2Content as ExamContent,
  'sec1-chinese-wa3': chineseWa3Content as ExamContent,
  'sec1-chinese-eoy': chineseEoyContent as ExamContent,
};

export default function ExamView() {
  const { examId } = useParams<{ examId: string }>();
  const { user, language, _hasHydrated } = useStore();
  const t = useTranslations(language);
  const navigate = useNavigate();
  const [showAnswers, setShowAnswers] = useState(false);
  const printRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (_hasHydrated && !user) {
      navigate('/login');
    }
  }, [user, _hasHydrated, navigate]);

  // Wait for store hydration before rendering
  if (!_hasHydrated) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary mx-auto mb-4"></div>
          <p className="text-muted-foreground">Loading...</p>
        </div>
      </div>
    );
  }

  if (!user) return null;

  const exam = (examsData.exams as any[]).find(e => e.id === examId);
  const content = examId ? examContents[examId] : null;

  if (!exam) {
    return (
      <div className="min-h-screen bg-background">
        <AppHeader />
        <main className="container mx-auto px-4 py-8">
          <Card className="p-8 text-center">
            <FileText className="h-12 w-12 mx-auto text-muted-foreground mb-4" />
            <h3 className="text-lg font-medium mb-2">
              {language === 'zh' ? '试卷未找到' : 'Exam Paper Not Found'}
            </h3>
            <Button onClick={() => navigate('/exams')} className="mt-4">
              <ArrowLeft className="h-4 w-4 mr-2" />
              {language === 'zh' ? '返回试卷列表' : 'Back to Exams'}
            </Button>
          </Card>
        </main>
      </div>
    );
  }

  const handlePrint = () => {
    window.print();
  };

  const [isDownloading, setIsDownloading] = useState(false);

  const handleDownloadPDF = async () => {
    if (!printRef.current || isDownloading) return;
    setIsDownloading(true);
    try {
      const filename = `${exam.id}_${language === 'zh' ? exam.title_zh : exam.title}.pdf`.replace(/\s+/g, '_');
      const opt = {
        margin: [10, 10, 10, 10],
        filename,
        image: { type: 'jpeg', quality: 0.95 },
        html2canvas: { scale: 2, useCORS: true, logging: false },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' as const },
        pagebreak: { mode: ['avoid-all', 'css', 'legacy'] },
      };
      await html2pdf().set(opt).from(printRef.current).save();
    } finally {
      setIsDownloading(false);
    }
  };

  const renderMath = (text: string) => (
    <ReactMarkdown
      remarkPlugins={[remarkMath, remarkGfm]}
      rehypePlugins={[rehypeKatex]}
      components={{
        p: ({ children }) => <span>{children}</span>
      }}
    >
      {text}
    </ReactMarkdown>
  );

  return (
    <div className="min-h-screen bg-background">
      <AppHeader />

      <main className="container mx-auto px-4 py-8 max-w-4xl">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="mb-6"
        >
          <Button
            variant="ghost"
            onClick={() => navigate(`/exams?subject=${exam?.subject || ''}`)}
            className="mb-4"
          >
            <ArrowLeft className="h-4 w-4 mr-2" />
            {language === 'zh' ? '返回试卷列表' : 'Back to Exams'}
          </Button>

          <div className="flex items-start justify-between flex-wrap gap-4">
            <div>
              <h1 className="text-2xl font-bold">
                {language === 'zh' ? exam.subjectName_zh : exam.subjectName}
              </h1>
              <h2 className="text-xl text-muted-foreground">
                {language === 'zh' ? exam.title_zh : exam.title}
              </h2>
            </div>
            <div className="flex gap-2">
              <Button
                variant="outline"
                onClick={() => setShowAnswers(!showAnswers)}
              >
                {showAnswers ? (
                  <>
                    <EyeOff className="h-4 w-4 mr-2" />
                    {language === 'zh' ? '隐藏答案' : 'Hide Answers'}
                  </>
                ) : (
                  <>
                    <Eye className="h-4 w-4 mr-2" />
                    {language === 'zh' ? '显示答案' : 'Show Answers'}
                  </>
                )}
              </Button>
              <Button variant="outline" onClick={handleDownloadPDF} disabled={isDownloading}>
                <Download className="h-4 w-4 mr-2" />
                {isDownloading
                  ? (language === 'zh' ? '生成中...' : 'Generating...')
                  : (language === 'zh' ? '下载PDF' : 'Download PDF')
                }
              </Button>
              <Button variant="outline" onClick={handlePrint}>
                <Printer className="h-4 w-4 mr-2" />
                {language === 'zh' ? '打印' : 'Print'}
              </Button>
            </div>
          </div>
        </motion.div>

        {/* Exam Paper Content */}
        <div ref={printRef} className="print:p-8">
          {/* Exam Header Card */}
          <Card className="mb-6 print:border-2 print:border-black">
            <CardHeader className="text-center border-b">
              <CardTitle className="text-xl">
                {language === 'zh' ? exam.subjectName_zh : exam.subjectName}
              </CardTitle>
              <p className="text-lg font-medium">
                {language === 'zh' ? exam.title_zh : exam.title}
              </p>
            </CardHeader>
            <CardContent className="pt-4">
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
                <div>
                  <Clock className="h-5 w-5 mx-auto mb-1 text-muted-foreground" />
                  <p className="text-sm font-medium">{exam.duration} {language === 'zh' ? '分钟' : 'minutes'}</p>
                  <p className="text-xs text-muted-foreground">Duration</p>
                </div>
                <div>
                  <FileText className="h-5 w-5 mx-auto mb-1 text-muted-foreground" />
                  <p className="text-sm font-medium">{exam.totalMarks} {language === 'zh' ? '分' : 'marks'}</p>
                  <p className="text-xs text-muted-foreground">Total</p>
                </div>
                <div>
                  <Calculator className="h-5 w-5 mx-auto mb-1 text-muted-foreground" />
                  <p className="text-sm font-medium">
                    {exam.calculatorAllowed
                      ? (language === 'zh' ? '允许' : 'Allowed')
                      : (language === 'zh' ? '不允许' : 'Not Allowed')
                    }
                  </p>
                  <p className="text-xs text-muted-foreground">Calculator</p>
                </div>
                <div>
                  <Badge variant={exam.assessmentType === 'eoy' ? 'destructive' : 'default'}>
                    {exam.assessmentType.toUpperCase()}
                  </Badge>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Instructions */}
          {content && (
            <Card className="mb-6">
              <CardHeader>
                <CardTitle className="text-lg">
                  {language === 'zh' ? '考生须知' : 'Instructions to Candidates'}
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ol className="list-decimal list-inside space-y-2 text-sm">
                  {(language === 'zh' ? content.instructions_zh : content.instructions).map((instruction, i) => (
                    <li key={i}>{instruction}</li>
                  ))}
                </ol>
              </CardContent>
            </Card>
          )}

          {/* Topics Covered */}
          <Card className="mb-6">
            <CardHeader>
              <CardTitle className="text-lg">
                {language === 'zh' ? '涵盖课题' : 'Topics Covered'}
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="flex flex-wrap gap-2">
                {(language === 'zh' ? exam.topics_zh : exam.topics).map((topic: string, i: number) => (
                  <Badge key={i} variant="outline">{topic}</Badge>
                ))}
              </div>
            </CardContent>
          </Card>

          {/* Questions */}
          {content ? (
            content.sections.map((section, sectionIndex) => (
              <Card key={sectionIndex} className="mb-6">
                <CardHeader className="bg-muted/50">
                  <CardTitle className="text-lg flex justify-between">
                    <span>{language === 'zh' ? section.name_zh : section.name}</span>
                    <Badge variant="secondary">{section.marks} marks</Badge>
                  </CardTitle>
                </CardHeader>
                <CardContent className="pt-4 space-y-6">
                  {section.questions.map((question, qIndex) => (
                    <div key={qIndex} className="border-b pb-4 last:border-0">
                      <div className="flex justify-between items-start mb-2">
                        <span className="font-bold">Question {question.number}</span>
                        <Badge variant="outline">[{question.marks} marks]</Badge>
                      </div>

                      <div className="prose prose-sm max-w-none dark:prose-invert mb-3">
                        {renderMath(language === 'zh' && question.prompt_zh ? question.prompt_zh : question.prompt)}
                      </div>

                      {/* Passage for Editing questions */}
                      {(question as any).passage && (
                        <div className="my-4 p-4 border rounded bg-muted/30">
                          <pre className="text-sm whitespace-pre-wrap font-sans leading-relaxed">{(question as any).passage}</pre>
                        </div>
                      )}

                      {/* Diagram placeholder */}
                      {question.diagram && (
                        <div className="my-4 p-4 border rounded bg-muted/30 text-center">
                          <pre className="text-xs whitespace-pre font-mono">{question.diagram}</pre>
                        </div>
                      )}

                      {/* MCQ Choices */}
                      {question.type === 'mcq' && question.choices && (
                        <div className="space-y-2 ml-4">
                          {question.choices.map((choice, cIndex) => (
                            <div key={cIndex} className="flex gap-3">
                              <span className="font-medium w-6">{choice.label}</span>
                              <span>{renderMath(language === 'zh' && choice.text_zh ? choice.text_zh : choice.text)}</span>
                            </div>
                          ))}
                        </div>
                      )}

                      {/* Multi-part questions */}
                      {question.parts && (
                        <div className="space-y-3 ml-4">
                          {question.parts.map((part, pIndex) => (
                            <div key={pIndex}>
                              <div className="flex gap-2 items-start">
                                <span className="font-medium">({part.label})</span>
                                <div className="flex-1">
                                  {renderMath(language === 'zh' && part.prompt_zh ? part.prompt_zh : part.prompt)}
                                </div>
                                <Badge variant="outline" className="text-xs">[{part.marks}]</Badge>
                              </div>
                            </div>
                          ))}
                        </div>
                      )}

                      {/* Answer space indicator for print */}
                      <div className="mt-4 print:block hidden">
                        <div className="border-t border-dashed pt-2">
                          <p className="text-xs text-muted-foreground">Answer:</p>
                          <div className="h-24 border-b border-dotted" />
                        </div>
                      </div>
                    </div>
                  ))}
                </CardContent>
              </Card>
            ))
          ) : (
            <Card className="p-8 text-center">
              <FileText className="h-12 w-12 mx-auto text-muted-foreground mb-4" />
              <p className="text-muted-foreground">
                {language === 'zh'
                  ? '试卷内容加载中...'
                  : 'Exam content loading...'
                }
              </p>
              <p className="text-sm text-muted-foreground mt-2">
                {language === 'zh'
                  ? '请查看上方的试卷信息和课题'
                  : 'Please view the exam info and topics above'
                }
              </p>
            </Card>
          )}

          {/* Answer Key (shown only when toggled) */}
          {showAnswers && content?.answerKey && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
            >
              <Card className="mb-6 border-green-500 print:hidden">
                <CardHeader className="bg-green-50 dark:bg-green-950">
                  <CardTitle className="text-lg flex items-center gap-2 text-green-700 dark:text-green-300">
                    <CheckCircle className="h-5 w-5" />
                    {language === 'zh' ? '参考答案' : 'Answer Key'}
                  </CardTitle>
                </CardHeader>
                <CardContent className="pt-4">
                  {content.answerKey.map((section, sIndex) => (
                    <div key={sIndex} className="mb-4">
                      <h4 className="font-medium mb-2">{section.sectionName}</h4>
                      <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
                        {section.answers.map((ans, aIndex) => (
                          <div key={aIndex} className="flex gap-2 text-sm">
                            <span className="font-medium">{ans.questionNum}.</span>
                            <span className="text-green-600 dark:text-green-400">{ans.answer}</span>
                          </div>
                        ))}
                      </div>
                    </div>
                  ))}
                </CardContent>
              </Card>
            </motion.div>
          )}
        </div>
      </main>

      {/* Print Styles */}
      <style>{`
        @media print {
          .print\\:hidden { display: none !important; }
          .print\\:block { display: block !important; }
          .print\\:p-8 { padding: 2rem !important; }
          .print\\:border-2 { border-width: 2px !important; }
          .print\\:border-black { border-color: black !important; }
          nav, header, button, .no-print { display: none !important; }
          body { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
        }
      `}</style>
    </div>
  );
}
