import { GraduationCap } from "lucide-react";
import { useStore, type GradeLevel } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Button } from "@/components/ui/button";

const gradeLevels: { value: GradeLevel; label_en: string; label_zh: string }[] = [
  { value: 'sec1', label_en: 'Sec 1', label_zh: '中一' },
  { value: 'sec2', label_en: 'Sec 2', label_zh: '中二' },
  { value: 'sec3', label_en: 'Sec 3', label_zh: '中三' },
  { value: 'sec4', label_en: 'Sec 4', label_zh: '中四' },
  { value: 'olevel', label_en: 'O-Level', label_zh: 'O水准' },
  { value: 'jc1', label_en: 'JC 1', label_zh: 'JC 1' },
  { value: 'jc2', label_en: 'JC 2', label_zh: 'JC 2' },
  { value: 'alevel', label_en: 'A-Level', label_zh: 'A水准' },
  { value: 'ai', label_en: 'AI', label_zh: 'AI' },
];

export default function GradeLevelSelector() {
  const { gradeLevel, setGradeLevel, language } = useStore();
  const t = useTranslations(language);

  const currentGrade = gradeLevels.find(g => g.value === gradeLevel);
  const currentLabel = language === 'zh' ? currentGrade?.label_zh : currentGrade?.label_en;

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" size="sm" className="gap-2">
          <GraduationCap className="h-4 w-4" />
          <span>{currentLabel}</span>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        {gradeLevels.map((grade) => (
          <DropdownMenuItem
            key={grade.value}
            onClick={() => setGradeLevel(grade.value)}
            className={gradeLevel === grade.value ? 'bg-accent' : ''}
          >
            {language === 'zh' ? grade.label_zh : grade.label_en}
          </DropdownMenuItem>
        ))}
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
