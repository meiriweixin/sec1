import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { useStore } from "@/lib/store";
import { useTranslations } from "@/lib/i18n";
import { BookOpen } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { useToast } from "@/hooks/use-toast";
import { useGoogleLogin } from '@react-oauth/google';
import { validateGoogleLogin } from '@/lib/auth';
import { migrateUserProgress, getOldUserIdFormat } from '@/lib/migration';

export default function Login() {
  const [isLoading, setIsLoading] = useState(false);
  const { login, language } = useStore();
  const t = useTranslations(language);
  const navigate = useNavigate();
  const { toast } = useToast();

  // Check if Google Client ID is configured
  const googleClientId = import.meta.env.VITE_GOOGLE_CLIENT_ID;
  const isGoogleConfigured = googleClientId && googleClientId !== 'YOUR_GOOGLE_CLIENT_ID_HERE' && googleClientId.trim() !== '';

  // Google Login using useGoogleLogin hook with authorization code flow
  // Only initialize if Google is properly configured
  const googleLogin = isGoogleConfigured ? useGoogleLogin({
    onSuccess: async (codeResponse) => {
      setIsLoading(true);
      try {
        // Exchange authorization code for user info
        const response = await fetch('https://www.googleapis.com/oauth2/v3/userinfo', {
          headers: {
            Authorization: `Bearer ${codeResponse.access_token}`,
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch user info');
        }

        const userInfo = await response.json();

        // Validate user against Supabase whitelist
        const sglearnUser = await validateGoogleLogin(
          userInfo.sub,
          userInfo.email,
          userInfo.name || userInfo.email.split('@')[0],
          userInfo.picture
        );

        if (!sglearnUser) {
          toast({
            title: "Access Denied",
            description: "Your email is not authorized to access this application. Please contact the administrator.",
            variant: "destructive",
          });
          setIsLoading(false);
          return;
        }

        // Migrate progress from old user ID format to Supabase UUID
        const oldUserId = getOldUserIdFormat(userInfo.sub);
        migrateUserProgress(oldUserId, sglearnUser.id);

        // Create user object for store
        const googleUser = {
          id: sglearnUser.id, // Use Supabase UUID
          email: sglearnUser.email,
          name: sglearnUser.name,
          isGuest: false,
          provider: 'google' as const,
          photoURL: sglearnUser.photo_url || userInfo.picture || undefined,
          isAdmin: sglearnUser.is_admin
        };

        login(googleUser);
        toast({
          title: t.welcomeBack,
          description: `Successfully signed in as ${googleUser.name}!`,
        });
        navigate("/dashboard");
      } catch (error) {
        console.error('Google login error:', error);
        toast({
          title: t.error,
          description: "Failed to sign in with Google. Please try again.",
          variant: "destructive",
        });
      } finally {
        setIsLoading(false);
      }
    },
    onError: (error) => {
      console.error('Google Login Failed:', error);
      toast({
        title: t.error,
        description: "Google sign-in was cancelled or failed.",
        variant: "destructive",
      });
    },
  }) : null;

  const handleGoogleClick = () => {
    if (!isGoogleConfigured || !googleLogin) {
      toast({
        title: "Google Sign-In Not Configured",
        description: "Please set up Google OAuth credentials. See GOOGLE_AUTH_SETUP.md for instructions.",
        variant: "destructive",
      });
      // Open setup guide in console
      console.log('%c⚠️ Google OAuth Setup Required', 'font-size: 16px; font-weight: bold; color: #EA4335;');
      console.log('%cFollow these steps:', 'font-size: 14px; color: #4285F4;');
      console.log('1. Go to https://console.cloud.google.com/');
      console.log('2. Create a new project');
      console.log('3. Enable Google+ API');
      console.log('4. Create OAuth 2.0 credentials');
      console.log('5. Add http://localhost:8080 to authorized origins');
      console.log('6. Copy the Client ID');
      console.log('7. Update .env file: VITE_GOOGLE_CLIENT_ID=your-client-id');
      console.log('8. Restart dev server: npm run dev');
      console.log('%cSee GOOGLE_AUTH_SETUP.md for detailed instructions', 'font-size: 12px; color: #34A853;');
      return;
    }
    googleLogin();
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
            {/* Google Login */}
            <Button
              onClick={handleGoogleClick}
              variant="outline"
              className="w-full border-2 hover:bg-accent/50 transition-colors h-12"
              disabled={isLoading}
              type="button"
            >
              <svg className="mr-2 h-5 w-5" viewBox="0 0 24 24">
                <path
                  fill="#4285F4"
                  d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
                />
                <path
                  fill="#34A853"
                  d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
                />
                <path
                  fill="#FBBC05"
                  d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"
                />
                <path
                  fill="#EA4335"
                  d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
                />
              </svg>
              <span className="font-medium">
                {isLoading ? "Signing in..." : t.continueWithGoogle}
              </span>
            </Button>

            {/* Info Text */}
            <div className="text-center text-xs text-muted-foreground space-y-2">
              <p className="font-semibold">Sign in with your Google account</p>
              <p>Only authorized users can access the application.</p>
              <p className="text-[10px] mt-2">
                Contact the administrator if you need access.
              </p>
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
