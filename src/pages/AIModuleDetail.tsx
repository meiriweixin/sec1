import { useParams, Link } from "react-router-dom";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { useUserStore } from "@/lib/store";
import aiModules from "@/data/ai-modules.json";
import { ArrowLeft, ExternalLink, Copy, CheckCircle, Shield, Sparkles } from "lucide-react";
import { useState } from "react";
import { useToast } from "@/hooks/use-toast";
import { Alert, AlertDescription } from "@/components/ui/alert";

export default function AIModuleDetail() {
  const { moduleId } = useParams();
  const { aiProgress, toggleAIModuleComplete } = useUserStore();
  const { toast } = useToast();
  const [copiedPrompt, setCopiedPrompt] = useState<number | null>(null);

  const module = aiModules.modules.find(m => m.id === moduleId);
  const isCompleted = aiProgress?.[moduleId || ""]?.done || false;

  if (!module) {
    return (
      <div className="container mx-auto px-4 py-12">
        <Alert variant="destructive">
          <AlertDescription>Module not found</AlertDescription>
        </Alert>
      </div>
    );
  }

  const copyPrompt = async (prompt: string, index: number) => {
    try {
      await navigator.clipboard.writeText(prompt);
      setCopiedPrompt(index);
      toast({
        title: "Prompt copied! 📋",
        description: "Paste it into the AI tool",
        duration: 2000,
      });
      setTimeout(() => setCopiedPrompt(null), 2000);
    } catch (err) {
      toast({
        title: "Copy failed",
        description: "Please copy manually",
        variant: "destructive",
      });
    }
  };

  const handleToggleComplete = () => {
    if (moduleId) {
      toggleAIModuleComplete(moduleId);
      if (!isCompleted) {
        toast({
          title: "🎉 Module completed!",
          description: "Great job learning about " + module.title,
          duration: 3000,
        });
      }
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-pink-50 to-blue-50 dark:from-gray-900 dark:via-purple-900/20 dark:to-gray-900">
      {/* Safety Notice */}
      <div className="sticky top-16 z-40 bg-purple-100 dark:bg-purple-900/30 border-b border-purple-200 dark:border-purple-800">
        <div className="container mx-auto px-4 py-2 flex items-center gap-2 text-sm text-purple-900 dark:text-purple-100">
          <Shield className="h-4 w-4" />
          <span>Ask an adult if you're unsure. Don't upload personal info.</span>
        </div>
      </div>

      <div className="container mx-auto px-4 py-12 max-w-5xl">
        {/* Back Button */}
        <Link to="/ai">
          <Button variant="ghost" className="mb-6 hover:bg-purple-100 dark:hover:bg-purple-900/30">
            <ArrowLeft className="mr-2 h-4 w-4" />
            Back to Playground
          </Button>
        </Link>

        {/* Module Header */}
        <div className="text-center mb-12 space-y-4">
          <div className="text-8xl mb-4">{module.emoji}</div>
          <h1 className="text-5xl font-bold bg-gradient-to-r from-purple-600 via-pink-600 to-blue-600 bg-clip-text text-transparent">
            {module.title}
          </h1>
          <p className="text-xl text-gray-700 dark:text-gray-300 max-w-2xl mx-auto leading-relaxed">
            {module.concept}
          </p>
        </div>

        {/* Mark as Done Toggle */}
        <div className="flex justify-center mb-8">
          <Button
            size="lg"
            onClick={handleToggleComplete}
            className={
              isCompleted
                ? "bg-gradient-to-r from-green-500 to-emerald-500 hover:from-green-600 hover:to-emerald-600"
                : "bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700"
            }
          >
            <CheckCircle className="mr-2 h-5 w-5" />
            {isCompleted ? "Completed ✓" : "Mark as Done"}
          </Button>
        </div>

        {/* Activities */}
        <div className="space-y-6">
          <h2 className="text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
            <Sparkles className="h-8 w-8 text-purple-600" />
            Try These Activities
          </h2>

          {module.activities.map((activity, index) => (
            <Card key={index} className="overflow-hidden border-2 border-purple-200 dark:border-purple-800 hover:border-purple-400 dark:hover:border-purple-600 transition-all">
              <CardHeader className="bg-gradient-to-r from-purple-50 to-pink-50 dark:from-purple-950/30 dark:to-pink-950/30">
                <div className="flex items-start justify-between gap-4">
                  <div className="flex-1">
                    <CardTitle className="text-2xl text-purple-900 dark:text-purple-100 mb-2">
                      {activity.label}
                    </CardTitle>
                    <CardDescription className="text-base text-gray-700 dark:text-gray-300">
                      Click to open this AI tool in a new tab
                    </CardDescription>
                  </div>
                  <a
                    href={activity.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="shrink-0"
                  >
                    <Button size="lg" className="bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700">
                      Open Tool
                      <ExternalLink className="ml-2 h-5 w-5" />
                    </Button>
                  </a>
                </div>
              </CardHeader>
              <CardContent className="pt-6">
                <div className="bg-gray-50 dark:bg-gray-800 rounded-xl p-6 border-2 border-dashed border-purple-300 dark:border-purple-700">
                  <div className="flex items-start justify-between gap-4 mb-3">
                    <h3 className="font-semibold text-lg text-purple-900 dark:text-purple-100">
                      📝 Suggested Prompt:
                    </h3>
                    <Button
                      size="sm"
                      variant={copiedPrompt === index ? "default" : "outline"}
                      onClick={() => copyPrompt(activity.prompt, index)}
                      className={
                        copiedPrompt === index
                          ? "bg-green-500 hover:bg-green-600"
                          : "border-purple-300 text-purple-700 hover:bg-purple-50 dark:border-purple-700 dark:text-purple-300"
                      }
                    >
                      {copiedPrompt === index ? (
                        <>
                          <CheckCircle className="mr-2 h-4 w-4" />
                          Copied!
                        </>
                      ) : (
                        <>
                          <Copy className="mr-2 h-4 w-4" />
                          Copy Prompt
                        </>
                      )}
                    </Button>
                  </div>
                  <p className="text-gray-700 dark:text-gray-300 leading-relaxed whitespace-pre-line text-base">
                    {activity.prompt}
                  </p>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Next Steps */}
        <div className="mt-12 text-center">
          <Link to="/ai">
            <Button size="lg" variant="outline" className="border-purple-300 text-purple-700 hover:bg-purple-50 dark:border-purple-700 dark:text-purple-300">
              Explore More Modules
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
}











