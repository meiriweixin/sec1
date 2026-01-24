import { AppHeader } from "@/components/layout/app-header";
import { SubjectCard } from "@/components/cards/subject-card";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { motion } from "framer-motion";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import contentData from "@/data";

export default function Subjects() {
  const { user, language, gradeLevel, _hasHydrated } = useStore();
  const t = useTranslations(language);
  const navigate = useNavigate();

  useEffect(() => {
    // Wait for store to hydrate before checking authentication
    if (_hasHydrated && !user) {
      navigate('/login');
    }
  }, [user, _hasHydrated, navigate]);

  if (!user) return null;

  // Filter subjects based on grade level
  const subjects = contentData.subjects.filter(subject => {
    // AI Playground is only shown when 'ai' grade is selected
    if (subject.id === 'ai-playground') {
      return gradeLevel === 'ai';
    }

    // For 'ai' grade level, only show AI Playground
    if (gradeLevel === 'ai') {
      return false;
    }

    // Check if subject has any chapters for the current grade level
    const hasChaptersForGrade = subject.chapters?.some(
      chapter => chapter.gradeLevel === gradeLevel
    );

    return hasChaptersForGrade;
  });

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
          <h1 className="text-3xl font-bold mb-2">
            {t.subjects}
            <span className="text-xl font-normal text-muted-foreground ml-3">
              {gradeLevel === 'sec1' && (language === 'zh' ? '中一' : 'Secondary 1')}
              {gradeLevel === 'sec2' && (language === 'zh' ? '中二' : 'Secondary 2')}
              {gradeLevel === 'sec3' && (language === 'zh' ? '中三' : 'Secondary 3')}
              {gradeLevel === 'sec4' && (language === 'zh' ? '中四' : 'Secondary 4')}
              {gradeLevel === 'olevel' && (language === 'zh' ? 'O水准备考' : 'O-Level Exam Prep')}
              {gradeLevel === 'jc1' && 'JC 1'}
              {gradeLevel === 'jc2' && 'JC 2'}
              {gradeLevel === 'alevel' && (language === 'zh' ? 'A水准备考' : 'A-Level Exam Prep')}
              {gradeLevel === 'ai' && (language === 'zh' ? '人工智能' : 'Artificial Intelligence')}
            </span>
          </h1>
          <p className="text-muted-foreground">
            {t.chooseSubject}
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
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
      </main>
    </div>
  );
}