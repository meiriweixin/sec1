import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { BookOpen, Sun, Moon, Globe, User, LogOut, GraduationCap, FileText, Brain, Settings } from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { useNavigate } from "react-router-dom";
import GradeLevelSelector from "@/components/ui/grade-level-selector";
import { isUserAdmin } from "@/lib/auth";

export function AppHeader() {
  const { user, language, theme, setLanguage, setTheme, logout } = useStore();
  const t = useTranslations(language);
  const navigate = useNavigate();
  const [isAdmin, setIsAdmin] = useState(false);

  useEffect(() => {
    if (user) {
      isUserAdmin(user.id).then(setIsAdmin);
    } else {
      setIsAdmin(false);
    }
  }, [user]);

  const toggleTheme = () => {
    if (theme === 'light') setTheme('dark');
    else if (theme === 'dark') setTheme('system');
    else setTheme('light');
  };

  const toggleLanguage = () => {
    setLanguage(language === 'en' ? 'zh' : 'en');
  };

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 items-center justify-between px-4">
        {/* Logo */}
        <div 
          className="flex items-center space-x-2 cursor-pointer"
          onClick={() => navigate('/dashboard')}
        >
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary text-primary-foreground">
            <BookOpen className="h-5 w-5" />
          </div>
          <span className="font-bold text-xl bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">
            SG Learning
          </span>
        </div>

        {/* Navigation Links */}
        {user && (
          <nav className="hidden md:flex items-center space-x-1">
            <Button
              variant="ghost"
              size="sm"
              onClick={() => navigate('/subjects')}
              className="text-muted-foreground hover:text-foreground"
            >
              <GraduationCap className="h-4 w-4 mr-2" />
              {t.subjects}
            </Button>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => navigate('/exams')}
              className="text-muted-foreground hover:text-foreground"
            >
              <FileText className="h-4 w-4 mr-2" />
              {t.exams}
            </Button>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => navigate('/ai')}
              className="text-muted-foreground hover:text-foreground"
            >
              <Brain className="h-4 w-4 mr-2" />
              AI
            </Button>
            {isAdmin && (
              <Button
                variant="ghost"
                size="sm"
                onClick={() => navigate('/admin')}
                className="text-muted-foreground hover:text-foreground"
              >
                <Settings className="h-4 w-4 mr-2" />
                Admin
              </Button>
            )}
          </nav>
        )}

        {/* Right side controls */}
        <div className="flex items-center space-x-2">
          {/* Grade Level Selector */}
          {user && <GradeLevelSelector />}

          {/* Language Toggle */}
          <Button
            variant="ghost"
            size="sm"
            onClick={toggleLanguage}
            className="h-9 w-9"
          >
            <Globe className="h-4 w-4" />
            <span className="sr-only">{t.language}</span>
          </Button>

          {/* Theme Toggle */}
          <Button 
            variant="ghost" 
            size="sm" 
            onClick={toggleTheme}
            className="h-9 w-9"
          >
            {theme === 'dark' ? (
              <Sun className="h-4 w-4" />
            ) : theme === 'light' ? (
              <Moon className="h-4 w-4" />
            ) : (
              <div className="h-4 w-4 rounded-full bg-gradient-to-r from-primary to-accent" />
            )}
            <span className="sr-only">{t.theme}</span>
          </Button>

          {/* User Menu */}
          {user && (
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="ghost" size="sm" className="h-9 w-9">
                  <User className="h-4 w-4" />
                  <span className="sr-only">{t.profile}</span>
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="end" className="w-56">
                <div className="px-2 py-1.5">
                  <p className="text-sm font-medium">{user.name}</p>
                  <p className="text-xs text-muted-foreground">{user.email}</p>
                </div>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={() => navigate('/progress')}>
                  {t.progress}
                </DropdownMenuItem>
                <DropdownMenuItem onClick={() => navigate('/profile')}>
                  {t.profile}
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={handleLogout} className="text-destructive">
                  <LogOut className="mr-2 h-4 w-4" />
                  {t.logout}
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          )}
        </div>
      </div>
    </header>
  );
}