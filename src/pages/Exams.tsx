import { AppHeader } from "@/components/layout/app-header";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { motion } from "framer-motion";
import { useEffect, useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  FileText,
  Clock,
  Calculator,
  CalendarDays,
  BookOpen,
  Eye,
  Download,
  Printer,
  Filter
} from "lucide-react";
import examsData from "@/data/exams.json";

interface ExamSection {
  name: string;
  name_zh: string;
  marks: number;
  questions: number;
}

interface Exam {
  id: string;
  subject: string;
  subjectName: string;
  subjectName_zh: string;
  gradeLevel: string;
  assessmentType: string;
  title: string;
  title_zh: string;
  description: string;
  description_zh: string;
  duration: number;
  totalMarks: number;
  calculatorAllowed: boolean;
  topics: string[];
  topics_zh: string[];
  sections: ExamSection[];
  file: string;
}

export default function Exams() {
  const { user, language, gradeLevel, _hasHydrated } = useStore();
  const t = useTranslations(language);
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const [selectedTab, setSelectedTab] = useState<string>("all");
  const [selectedSubject, setSelectedSubject] = useState<string>(
    searchParams.get('subject') || "all"
  );

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

  // Filter exams by current grade level
  const gradeFilteredExams = (examsData.exams as Exam[]).filter(
    exam => exam.gradeLevel === gradeLevel
  );

  // Get unique subjects for the dropdown
  const uniqueSubjects = Array.from(
    new Set(gradeFilteredExams.map(exam => exam.subject))
  ).map(subject => {
    const exam = gradeFilteredExams.find(e => e.subject === subject);
    return {
      id: subject,
      name: exam?.subjectName || subject,
      name_zh: exam?.subjectName_zh || subject
    };
  });

  // Filter exams by selected subject
  const filteredExams = selectedSubject === "all"
    ? gradeFilteredExams
    : gradeFilteredExams.filter(exam => exam.subject === selectedSubject);

  // Group exams by assessment type
  const examsByType = filteredExams.reduce((acc, exam) => {
    if (!acc[exam.assessmentType]) {
      acc[exam.assessmentType] = [];
    }
    acc[exam.assessmentType].push(exam);
    return acc;
  }, {} as Record<string, Exam[]>);

  const getAssessmentColor = (type: string) => {
    const colors: Record<string, string> = {
      wa1: "bg-blue-500",
      wa2: "bg-green-500",
      wa3: "bg-orange-500",
      eoy: "bg-red-500"
    };
    return colors[type] || "bg-gray-500";
  };

  const getAssessmentBadgeVariant = (type: string): "default" | "secondary" | "destructive" | "outline" => {
    if (type === "eoy") return "destructive";
    return "default";
  };

  const gradeLevelName = {
    sec1: language === 'zh' ? '中一' : 'Secondary 1',
    sec2: language === 'zh' ? '中二' : 'Secondary 2',
    sec3: language === 'zh' ? '中三' : 'Secondary 3',
    sec4: language === 'zh' ? '中四' : 'Secondary 4',
    jc1: 'JC 1',
    jc2: 'JC 2'
  }[gradeLevel] || gradeLevel;

  const handleViewExam = (examId: string) => {
    navigate(`/exams/${examId}`);
  };

  const ExamCard = ({ exam }: { exam: Exam }) => (
    <Card className="hover:shadow-lg transition-shadow">
      <CardHeader className="pb-3">
        <div className="flex items-start justify-between">
          <div>
            <CardTitle className="text-lg">
              {language === 'zh' ? exam.title_zh : exam.title}
            </CardTitle>
            <CardDescription className="mt-1">
              {language === 'zh' ? exam.subjectName_zh : exam.subjectName}
            </CardDescription>
          </div>
          <Badge
            variant={getAssessmentBadgeVariant(exam.assessmentType)}
            className={exam.assessmentType === 'eoy' ? '' : getAssessmentColor(exam.assessmentType)}
          >
            {exam.assessmentType.toUpperCase()}
          </Badge>
        </div>
      </CardHeader>
      <CardContent>
        <p className="text-sm text-muted-foreground mb-4">
          {language === 'zh' ? exam.description_zh : exam.description}
        </p>

        {/* Exam Info */}
        <div className="grid grid-cols-2 gap-3 mb-4">
          <div className="flex items-center gap-2 text-sm">
            <Clock className="h-4 w-4 text-muted-foreground" />
            <span>{exam.duration} {language === 'zh' ? '分钟' : 'min'}</span>
          </div>
          <div className="flex items-center gap-2 text-sm">
            <FileText className="h-4 w-4 text-muted-foreground" />
            <span>{exam.totalMarks} {language === 'zh' ? '分' : 'marks'}</span>
          </div>
          <div className="flex items-center gap-2 text-sm col-span-2">
            <Calculator className="h-4 w-4 text-muted-foreground" />
            <span>
              {exam.calculatorAllowed
                ? (language === 'zh' ? '允许使用计算器' : 'Calculator allowed')
                : (language === 'zh' ? '不允许使用计算器' : 'No calculator')
              }
            </span>
          </div>
        </div>

        {/* Topics */}
        <div className="mb-4">
          <p className="text-xs font-medium text-muted-foreground mb-2">
            {language === 'zh' ? '涵盖课题' : 'Topics Covered'}
          </p>
          <div className="flex flex-wrap gap-1">
            {(language === 'zh' ? exam.topics_zh : exam.topics).slice(0, 3).map((topic, i) => (
              <Badge key={i} variant="outline" className="text-xs">
                {topic}
              </Badge>
            ))}
            {exam.topics.length > 3 && (
              <Badge variant="outline" className="text-xs">
                +{exam.topics.length - 3}
              </Badge>
            )}
          </div>
        </div>

        {/* Sections */}
        <div className="mb-4 border rounded-lg p-3 bg-muted/30">
          <p className="text-xs font-medium mb-2">
            {language === 'zh' ? '试卷结构' : 'Paper Structure'}
          </p>
          {exam.sections.map((section, i) => (
            <div key={i} className="flex justify-between text-xs py-1">
              <span className="text-muted-foreground">
                {language === 'zh' ? section.name_zh : section.name}
              </span>
              <span className="font-medium">{section.marks} marks</span>
            </div>
          ))}
        </div>

        {/* Actions */}
        <div className="flex gap-2">
          <Button
            className="flex-1"
            onClick={() => handleViewExam(exam.id)}
          >
            <Eye className="h-4 w-4 mr-2" />
            {language === 'zh' ? '查看试卷' : 'View Paper'}
          </Button>
          <Button variant="outline" size="icon" title="Print">
            <Printer className="h-4 w-4" />
          </Button>
        </div>
      </CardContent>
    </Card>
  );

  return (
    <div className="min-h-screen bg-background">
      <AppHeader />

      <main className="container mx-auto px-4 py-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="mb-8"
        >
          <div className="flex items-center gap-3 mb-2">
            <BookOpen className="h-8 w-8 text-primary" />
            <h1 className="text-3xl font-bold">
              {language === 'zh' ? '考试试卷' : 'Exam Papers'}
              <span className="text-xl font-normal text-muted-foreground ml-3">
                {gradeLevelName}
              </span>
            </h1>
          </div>
          <p className="text-muted-foreground">
            {language === 'zh'
              ? '查看和下载各学期的考试试卷'
              : 'View and download exam papers for each assessment period'
            }
          </p>
        </motion.div>

        {/* Subject Filter */}
        {uniqueSubjects.length > 1 && (
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.3, delay: 0.1 }}
            className="mb-6"
          >
            <div className="flex items-center gap-3">
              <Filter className="h-4 w-4 text-muted-foreground" />
              <span className="text-sm font-medium text-muted-foreground">
                {language === 'zh' ? '按科目筛选' : 'Filter by Subject'}
              </span>
              <Select value={selectedSubject} onValueChange={setSelectedSubject}>
                <SelectTrigger className="w-[200px]">
                  <SelectValue placeholder={language === 'zh' ? '选择科目' : 'Select subject'} />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="all">
                    {language === 'zh' ? '全部科目' : 'All Subjects'}
                  </SelectItem>
                  {uniqueSubjects.map(subject => (
                    <SelectItem key={subject.id} value={subject.id}>
                      {language === 'zh' ? subject.name_zh : subject.name}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
              {selectedSubject !== "all" && (
                <Button
                  variant="ghost"
                  size="sm"
                  onClick={() => setSelectedSubject("all")}
                  className="text-xs"
                >
                  {language === 'zh' ? '清除筛选' : 'Clear filter'}
                </Button>
              )}
            </div>
          </motion.div>
        )}

        {filteredExams.length === 0 ? (
          <Card className="p-8 text-center">
            <FileText className="h-12 w-12 mx-auto text-muted-foreground mb-4" />
            <h3 className="text-lg font-medium mb-2">
              {language === 'zh' ? '暂无试卷' : 'No Exam Papers Available'}
            </h3>
            <p className="text-muted-foreground">
              {language === 'zh'
                ? `${gradeLevelName}的试卷即将推出`
                : `Exam papers for ${gradeLevelName} are coming soon`
              }
            </p>
          </Card>
        ) : (
          <Tabs value={selectedTab} onValueChange={setSelectedTab} className="space-y-6">
            <TabsList className="grid grid-cols-5 w-full max-w-lg">
              <TabsTrigger value="all">
                {language === 'zh' ? '全部' : 'All'}
              </TabsTrigger>
              <TabsTrigger value="wa1" className="data-[state=active]:bg-blue-500 data-[state=active]:text-white">
                WA1
              </TabsTrigger>
              <TabsTrigger value="wa2" className="data-[state=active]:bg-green-500 data-[state=active]:text-white">
                WA2
              </TabsTrigger>
              <TabsTrigger value="wa3" className="data-[state=active]:bg-orange-500 data-[state=active]:text-white">
                WA3
              </TabsTrigger>
              <TabsTrigger value="eoy" className="data-[state=active]:bg-red-500 data-[state=active]:text-white">
                EOY
              </TabsTrigger>
            </TabsList>

            <TabsContent value="all">
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {filteredExams.map((exam, index) => (
                  <motion.div
                    key={exam.id}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.3, delay: index * 0.1 }}
                  >
                    <ExamCard exam={exam} />
                  </motion.div>
                ))}
              </div>
            </TabsContent>

            {['wa1', 'wa2', 'wa3', 'eoy'].map(type => (
              <TabsContent key={type} value={type}>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                  {(examsByType[type] || []).map((exam, index) => (
                    <motion.div
                      key={exam.id}
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ duration: 0.3, delay: index * 0.1 }}
                    >
                      <ExamCard exam={exam} />
                    </motion.div>
                  ))}
                  {(!examsByType[type] || examsByType[type].length === 0) && (
                    <Card className="p-8 text-center col-span-full">
                      <FileText className="h-12 w-12 mx-auto text-muted-foreground mb-4" />
                      <p className="text-muted-foreground">
                        {language === 'zh'
                          ? `${type.toUpperCase()} 试卷即将推出`
                          : `${type.toUpperCase()} papers coming soon`
                        }
                      </p>
                    </Card>
                  )}
                </div>
              </TabsContent>
            ))}
          </Tabs>
        )}

        {/* Assessment Calendar Overview */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.3 }}
          className="mt-12"
        >
          <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
            <CalendarDays className="h-5 w-5" />
            {language === 'zh' ? '考试日程概览' : 'Assessment Calendar'}
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            {[
              { type: 'wa1', term: 'Term 1', term_zh: '第一学期', weeks: 'Week 8-10' },
              { type: 'wa2', term: 'Term 2', term_zh: '第二学期', weeks: 'Week 18-20' },
              { type: 'wa3', term: 'Term 3', term_zh: '第三学期', weeks: 'Week 28-30' },
              { type: 'eoy', term: 'Term 4', term_zh: '第四学期', weeks: 'Week 38-40' }
            ].map((period) => (
              <Card key={period.type} className="p-4">
                <div className="flex items-center gap-2 mb-2">
                  <div className={`w-3 h-3 rounded-full ${getAssessmentColor(period.type)}`} />
                  <span className="font-medium">{period.type.toUpperCase()}</span>
                </div>
                <p className="text-sm text-muted-foreground">
                  {language === 'zh' ? period.term_zh : period.term}
                </p>
                <p className="text-xs text-muted-foreground">{period.weeks}</p>
              </Card>
            ))}
          </div>
        </motion.div>
      </main>
    </div>
  );
}
