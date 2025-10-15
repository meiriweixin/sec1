import { Link } from "react-router-dom";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { useUserStore } from "@/lib/store";
import aiModules from "@/data/ai-modules.json";
import { Sparkles, Brain, Play, Shield } from "lucide-react";

export default function AIPlayground() {
  const { aiProgress } = useUserStore();

  const completedCount = Object.values(aiProgress || {}).filter(p => p.done).length;
  const totalModules = aiModules.modules.length;
  const completionPercentage = totalModules > 0 ? Math.round((completedCount / totalModules) * 100) : 0;

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-pink-50 to-blue-50 dark:from-gray-900 dark:via-purple-900/20 dark:to-gray-900">
      {/* Safety Notice */}
      <div className="sticky top-16 z-40 bg-purple-100 dark:bg-purple-900/30 border-b border-purple-200 dark:border-purple-800">
        <div className="container mx-auto px-4 py-2 flex items-center justify-between">
          <div className="flex items-center gap-2 text-sm text-purple-900 dark:text-purple-100">
            <Shield className="h-4 w-4" />
            <span>Ask an adult if you're unsure. Don't upload personal info.</span>
          </div>
          <Link to="/ai/safety">
            <Button variant="link" size="sm" className="text-purple-700 dark:text-purple-300">
              Safety Tips
            </Button>
          </Link>
        </div>
      </div>

      <div className="container mx-auto px-4 py-12">
        {/* Hero Section */}
        <div className="text-center mb-12 space-y-4">
          <div className="flex justify-center mb-4">
            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-r from-purple-600 to-pink-600 rounded-full blur-2xl opacity-50 animate-pulse" />
              <Brain className="relative h-20 w-20 text-purple-600 dark:text-purple-400" />
            </div>
          </div>
          <h1 className="text-5xl font-bold bg-gradient-to-r from-purple-600 via-pink-600 to-blue-600 bg-clip-text text-transparent">
            Welcome to AI Playground!
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto leading-relaxed">
            Read one simple idea, then click a link and try it. Learn by doing—music, images, videos, code, voice, and more. 
            <span className="block mt-2 font-semibold text-purple-600 dark:text-purple-400">
              Be curious, be kind, and use AI responsibly.
            </span>
          </p>

          {/* Progress Overview */}
          <div className="flex justify-center gap-6 mt-8">
            <div className="text-center">
              <div className="text-4xl font-bold text-purple-600">{completedCount}/{totalModules}</div>
              <div className="text-sm text-gray-600 dark:text-gray-400">Modules Complete</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-pink-600">{completionPercentage}%</div>
              <div className="text-sm text-gray-600 dark:text-gray-400">Progress</div>
            </div>
          </div>
        </div>

        {/* Quick Links */}
        <div className="flex justify-center gap-4 mb-12">
          <Link to="/ai/progress">
            <Button size="lg" className="bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700">
              <Sparkles className="mr-2 h-5 w-5" />
              My Progress
            </Button>
          </Link>
          <Link to="/ai/safety">
            <Button size="lg" variant="outline" className="border-purple-300 text-purple-700 hover:bg-purple-50 dark:border-purple-700 dark:text-purple-300">
              <Shield className="mr-2 h-5 w-5" />
              Safety Guide
            </Button>
          </Link>
        </div>

        {/* Modules Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {aiModules.modules.map((module) => {
            const isCompleted = aiProgress?.[module.id]?.done || false;
            
            return (
              <Link key={module.id} to={`/ai/modules/${module.id}`}>
                <Card className="h-full transition-all duration-300 hover:shadow-2xl hover:scale-105 hover:border-purple-400 dark:hover:border-purple-600 cursor-pointer bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm">
                  <CardHeader className="pb-3">
                    <div className="flex items-start justify-between mb-2">
                      <div className="text-5xl">{module.emoji}</div>
                      {isCompleted && (
                        <Badge className="bg-gradient-to-r from-green-500 to-emerald-500 text-white">
                          ✓ Done
                        </Badge>
                      )}
                    </div>
                    <CardTitle className="text-xl font-bold text-gray-900 dark:text-white">
                      {module.title}
                    </CardTitle>
                    <CardDescription className="text-base leading-relaxed mt-2 text-gray-700 dark:text-gray-300">
                      {module.concept}
                    </CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="flex items-center gap-2 text-sm text-purple-600 dark:text-purple-400 font-semibold">
                      <Play className="h-4 w-4" />
                      {module.activities.length} Activities
                    </div>
                  </CardContent>
                </Card>
              </Link>
            );
          })}
        </div>
      </div>
    </div>
  );
}











