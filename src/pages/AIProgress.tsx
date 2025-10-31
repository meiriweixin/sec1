import { Link } from "react-router-dom";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { useUserStore } from "@/lib/store";
import aiModules from "@/data/ai-modules.json";
import { ArrowLeft, Trophy, Star, Target, Sparkles } from "lucide-react";

export default function AIProgress() {
  const { user, allUsersAIProgress } = useUserStore();

  const userId = user?.id;
  const userAIProgress = userId ? (allUsersAIProgress[userId] || {}) : {};

  const completedModules = Object.entries(userAIProgress).filter(([_, p]) => p.done);
  const totalModules = aiModules.modules.length;
  const completionPercentage = totalModules > 0 ? Math.round((completedModules.length / totalModules) * 100) : 0;

  // Badge achievements
  const badges = [
    { id: "starter", name: "AI Explorer", emoji: "🚀", condition: completedModules.length >= 1 },
    { id: "learner", name: "Creative Learner", emoji: "🎨", condition: completedModules.length >= 3 },
    { id: "expert", name: "AI Expert", emoji: "🧠", condition: completedModules.length >= 5 },
    { id: "master", name: "AI Master", emoji: "🏆", condition: completedModules.length >= 8 },
    { id: "champion", name: "AI Champion", emoji: "⭐", condition: completedModules.length >= 10 },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-pink-50 to-blue-50 dark:from-gray-900 dark:via-purple-900/20 dark:to-gray-900">
      <div className="container mx-auto px-4 py-12 max-w-6xl">
        {/* Back Button */}
        <Link to="/ai">
          <Button variant="ghost" className="mb-6 hover:bg-purple-100 dark:hover:bg-purple-900/30">
            <ArrowLeft className="mr-2 h-4 w-4" />
            Back to Playground
          </Button>
        </Link>

        {/* Header */}
        <div className="text-center mb-12 space-y-4">
          <div className="flex justify-center mb-4">
            <Trophy className="h-20 w-20 text-yellow-500" />
          </div>
          <h1 className="text-5xl font-bold bg-gradient-to-r from-purple-600 via-pink-600 to-blue-600 bg-clip-text text-transparent">
            Your AI Journey
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            Track your progress and earn badges!
          </p>
        </div>

        {/* Overall Progress */}
        <Card className="mb-8 border-2 border-purple-200 dark:border-purple-800">
          <CardHeader>
            <CardTitle className="text-2xl flex items-center gap-3">
              <Target className="h-6 w-6 text-purple-600" />
              Overall Progress
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-6">
            <div>
              <div className="flex justify-between mb-3">
                <span className="text-lg font-semibold text-gray-700 dark:text-gray-300">
                  {completedModules.length} of {totalModules} modules completed
                </span>
                <span className="text-2xl font-bold text-purple-600">
                  {completionPercentage}%
                </span>
              </div>
              <Progress value={completionPercentage} className="h-4" />
            </div>

            <div className="grid grid-cols-3 gap-4 text-center">
              <div className="p-4 bg-purple-50 dark:bg-purple-950/30 rounded-lg">
                <div className="text-3xl font-bold text-purple-600">{completedModules.length}</div>
                <div className="text-sm text-gray-600 dark:text-gray-400">Completed</div>
              </div>
              <div className="p-4 bg-pink-50 dark:bg-pink-950/30 rounded-lg">
                <div className="text-3xl font-bold text-pink-600">{totalModules - completedModules.length}</div>
                <div className="text-sm text-gray-600 dark:text-gray-400">Remaining</div>
              </div>
              <div className="p-4 bg-blue-50 dark:bg-blue-950/30 rounded-lg">
                <div className="text-3xl font-bold text-blue-600">{badges.filter(b => b.condition).length}</div>
                <div className="text-sm text-gray-600 dark:text-gray-400">Badges Earned</div>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Badges */}
        <Card className="mb-8 border-2 border-purple-200 dark:border-purple-800">
          <CardHeader>
            <CardTitle className="text-2xl flex items-center gap-3">
              <Star className="h-6 w-6 text-yellow-500" />
              Achievement Badges
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
              {badges.map((badge) => (
                <div
                  key={badge.id}
                  className={`p-4 rounded-xl text-center transition-all ${
                    badge.condition
                      ? "bg-gradient-to-br from-yellow-100 to-yellow-200 dark:from-yellow-900/30 dark:to-yellow-800/30 scale-105 shadow-lg"
                      : "bg-gray-100 dark:bg-gray-800 opacity-50 grayscale"
                  }`}
                >
                  <div className="text-4xl mb-2">{badge.emoji}</div>
                  <div className={`text-sm font-semibold ${badge.condition ? "text-yellow-900 dark:text-yellow-100" : "text-gray-600 dark:text-gray-400"}`}>
                    {badge.name}
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Module Status */}
        <Card className="border-2 border-purple-200 dark:border-purple-800">
          <CardHeader>
            <CardTitle className="text-2xl flex items-center gap-3">
              <Sparkles className="h-6 w-6 text-purple-600" />
              Module Status
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {aiModules.modules.map((module) => {
                const isCompleted = userAIProgress?.[module.id]?.done || false;
                const completedAt = userAIProgress?.[module.id]?.doneAt;

                return (
                  <Link key={module.id} to={`/ai/modules/${module.id}`}>
                    <div className="flex items-center justify-between p-4 rounded-lg hover:bg-purple-50 dark:hover:bg-purple-950/30 transition-colors cursor-pointer border border-gray-200 dark:border-gray-700">
                      <div className="flex items-center gap-4">
                        <div className="text-3xl">{module.emoji}</div>
                        <div>
                          <div className="font-semibold text-gray-900 dark:text-white">
                            {module.title}
                          </div>
                          {isCompleted && completedAt && (
                            <div className="text-sm text-gray-500 dark:text-gray-400">
                              Completed on {new Date(completedAt).toLocaleDateString()}
                            </div>
                          )}
                        </div>
                      </div>
                      <div>
                        {isCompleted ? (
                          <Badge className="bg-gradient-to-r from-green-500 to-emerald-500 text-white">
                            ✓ Done
                          </Badge>
                        ) : (
                          <Badge variant="outline" className="border-purple-300 text-purple-700 dark:border-purple-700 dark:text-purple-300">
                            Start
                          </Badge>
                        )}
                      </div>
                    </div>
                  </Link>
                );
              })}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}











