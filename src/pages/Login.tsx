import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Separator } from "@/components/ui/separator";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { BookOpen, Mail, Lock, UserCheck } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { useToast } from "@/hooks/use-toast";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const { login, language } = useStore();
  const t = useTranslations(language);
  const navigate = useNavigate();
  const { toast } = useToast();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);

    // Simulate API call
    setTimeout(() => {
      if (email && password) {
        login({
          id: "user1",
          email,
          name: email.split("@")[0],
          isGuest: false
        });
        toast({
          title: t.welcomeBack,
          description: "Successfully logged in!",
        });
        navigate("/dashboard");
      } else {
        toast({
          title: t.error,
          description: "Please enter both email and password.",
          variant: "destructive",
        });
      }
      setIsLoading(false);
    }, 1000);
  };

  const handleGuestLogin = () => {
    login({
      id: "guest",
      email: "guest@example.com",
      name: "Guest User",
      isGuest: true
    });
    toast({
      title: "Welcome!",
      description: "Continuing as guest user.",
    });
    navigate("/dashboard");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-background via-primary-soft/5 to-accent-soft/5 flex items-center justify-center p-4">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="w-full max-w-md"
      >
        <Card className="lesson-card">
          <CardHeader className="text-center space-y-2">
            <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-xl bg-primary text-primary-foreground mb-4">
              <BookOpen className="h-6 w-6" />
            </div>
            <CardTitle className="text-2xl font-bold bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">
              SG Learning
            </CardTitle>
            <CardDescription className="text-base">
              {t.loginToContinue}
            </CardDescription>
          </CardHeader>

          <CardContent className="space-y-6">
            {/* Email & Password Form */}
            <form onSubmit={handleLogin} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="email" className="flex items-center space-x-2">
                  <Mail className="h-4 w-4" />
                  <span>{t.email}</span>
                </Label>
                <Input
                  id="email"
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="student@example.com"
                  required
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="password" className="flex items-center space-x-2">
                  <Lock className="h-4 w-4" />
                  <span>{t.password}</span>
                </Label>
                <Input
                  id="password"
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••"
                  required
                />
              </div>

              <Button 
                type="submit" 
                className="w-full btn-primary"
                disabled={isLoading}
              >
                {isLoading ? t.loading : t.login}
              </Button>
            </form>

            {/* Separator */}
            <div className="relative">
              <Separator />
              <span className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 bg-background px-2 text-xs text-muted-foreground">
                or
              </span>
            </div>

            {/* Guest Login */}
            <Button 
              onClick={handleGuestLogin}
              variant="outline" 
              className="w-full"
            >
              <UserCheck className="mr-2 h-4 w-4" />
              {t.continueAsGuest}
            </Button>

            {/* Demo Credentials */}
            <div className="text-center text-xs text-muted-foreground space-y-1">
              <p><strong>Demo:</strong> Use any email/password combination</p>
              <p>or continue as guest to explore</p>
            </div>
          </CardContent>
        </Card>

        {/* Back to Landing */}
        <div className="text-center mt-6">
          <Button 
            variant="ghost" 
            onClick={() => navigate("/")}
            className="text-muted-foreground hover:text-foreground"
          >
            ← Back to Home
          </Button>
        </div>
      </motion.div>
    </div>
  );
}