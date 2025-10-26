import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { BookOpen, Users, TrendingUp, Award, ArrowRight, Play } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { useEffect } from "react";

const Index = () => {
  const { user, language, _hasHydrated } = useStore();
  const t = useTranslations(language);
  const navigate = useNavigate();

  useEffect(() => {
    // Only redirect if user is logged in AND they're actively on the landing page
    // Wait for store hydration to avoid premature redirects
    if (_hasHydrated && user && window.location.pathname === '/') {
      navigate('/dashboard');
    }
  }, [user, _hasHydrated, navigate]);

  const features = [
    {
      icon: BookOpen,
      title: "Interactive Lessons",
      title_zh: "互动课程",
      description: "Animated explanations and step-by-step learning",
      description_zh: "动画解释和循序渐进的学习"
    },
    {
      icon: TrendingUp,
      title: "Track Progress",
      title_zh: "跟踪进度",
      description: "Monitor your learning journey and achievements",
      description_zh: "监控您的学习过程和成就"
    },
    {
      icon: Award,
      title: "Earn Badges",
      title_zh: "获得徽章",
      description: "Get rewarded for completing chapters and exercises",
      description_zh: "完成章节和练习获得奖励"
    },
    {
      icon: Users,
      title: "Designed for Sec 1",
      title_zh: "专为中一设计",
      description: "Curriculum aligned with Singapore Secondary 1",
      description_zh: "与新加坡中一课程相对应"
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-background via-primary-soft/5 to-accent-soft/5">
      {/* Header */}
      <header className="border-b border-border/40 bg-background/80 backdrop-blur">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary text-primary-foreground">
                <BookOpen className="h-5 w-5" />
              </div>
              <span className="font-bold text-xl bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">
                SG Learning
              </span>
            </div>
            <Button 
              onClick={() => navigate('/login')}
              className="btn-primary"
            >
              {t.login}
            </Button>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="container mx-auto px-4 py-16 text-center">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <h1 className="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary via-accent to-primary bg-clip-text text-transparent">
            {language === 'zh' ? "掌握四大核心科目" : "Master Your Core Subjects"}
          </h1>
          <p className="text-xl md:text-2xl text-muted-foreground mb-8 max-w-3xl mx-auto">
            {language === 'zh'
              ? "为新加坡中一学生设计的互动学习平台。通过动画课程和即时反馈掌握英语、华文、数学和科学。"
              : "Interactive learning platform designed for Singapore Secondary 1 students. Master English, Chinese, Math and Science through animated lessons and instant feedback."
            }
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button 
              onClick={() => navigate('/login')}
              className="btn-primary text-lg px-8 py-6"
            >
              <Play className="mr-2 h-5 w-5" />
              {t.startLearning}
            </Button>
            <Button 
              variant="outline" 
              onClick={() => navigate('/login')}
              className="text-lg px-8 py-6"
            >
              {t.continueAsGuest}
              <ArrowRight className="ml-2 h-5 w-5" />
            </Button>
          </div>
        </motion.div>
      </section>

      {/* Features Section */}
      <section className="container mx-auto px-4 py-16">
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.6, delay: 0.2 }}
        >
          <h2 className="text-3xl font-bold text-center mb-12">
            {language === 'zh' ? "为什么选择SG Learning？" : "Why Choose SG Learning?"}
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {features.map((feature, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.3, delay: 0.1 * index }}
              >
                <Card className="lesson-card card-hover h-full text-center">
                  <CardHeader>
                    <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-xl bg-primary/10 text-primary mb-4">
                      <feature.icon className="h-6 w-6" />
                    </div>
                    <CardTitle className="text-lg">
                      {language === 'zh' && feature.title_zh ? feature.title_zh : feature.title}
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <CardDescription>
                      {language === 'zh' && feature.description_zh ? feature.description_zh : feature.description}
                    </CardDescription>
                  </CardContent>
                </Card>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* CTA Section */}
      <section className="container mx-auto px-4 py-16">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="text-center bg-gradient-to-r from-primary/5 to-accent/5 rounded-2xl p-8 md:p-12"
        >
          <h2 className="text-3xl font-bold mb-4">
            {language === 'zh' ? "准备好开始您的学习之旅了吗？" : "Ready to Start Your Learning Journey?"}
          </h2>
          <p className="text-lg text-muted-foreground mb-8">
            {language === 'zh'
              ? "加入数千名学生，通过我们的互动平台提高他们的英语、华文、数学和科学技能。"
              : "Join thousands of students improving their English, Chinese, Math and Science skills with our interactive platform."
            }
          </p>
          <Button 
            onClick={() => navigate('/login')}
            className="btn-primary text-lg px-8 py-6"
          >
            {t.startLearning}
            <ArrowRight className="ml-2 h-5 w-5" />
          </Button>
        </motion.div>
      </section>

      {/* Footer */}
      <footer className="border-t border-border/40 bg-background/50 py-8">
        <div className="container mx-auto px-4 text-center text-muted-foreground">
          <p>&copy; 2024 SG Learning. {language === 'zh' ? '为新加坡学生设计。' : 'Designed for Singapore students.'}</p>
        </div>
      </footer>
    </div>
  );
};

export default Index;
