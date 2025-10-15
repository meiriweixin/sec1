import { Link } from "react-router-dom";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { ArrowLeft, Shield, AlertTriangle, Eye, Lock, Users, Globe, CheckCircle } from "lucide-react";

export default function AISafety() {
  const safetyTips = [
    {
      icon: Shield,
      title: "Protect Your Privacy",
      description: "Never share personal information like your full name, address, phone number, school name, or photos with AI tools.",
      color: "text-blue-600",
      bg: "bg-blue-50 dark:bg-blue-950/30"
    },
    {
      icon: Eye,
      title: "Ask Before You Share",
      description: "Always ask a parent, teacher, or trusted adult before uploading documents, images, or any files to AI platforms.",
      color: "text-purple-600",
      bg: "bg-purple-50 dark:bg-purple-950/30"
    },
    {
      icon: AlertTriangle,
      title: "Spot Deepfakes",
      description: "AI can create fake images, videos, and voices. If something looks too perfect or strange, it might be AI-generated. Always verify sources.",
      color: "text-orange-600",
      bg: "bg-orange-50 dark:bg-orange-950/30"
    },
    {
      icon: Lock,
      title: "Keep Accounts Safe",
      description: "Use strong passwords and never share login details. Some AI tools require accounts—always get permission first.",
      color: "text-red-600",
      bg: "bg-red-50 dark:bg-red-950/30"
    },
    {
      icon: Globe,
      title: "Check Your Sources",
      description: "AI can make mistakes or create false information. Always verify facts from reliable sources like textbooks or trusted websites.",
      color: "text-green-600",
      bg: "bg-green-50 dark:bg-green-950/30"
    },
    {
      icon: Users,
      title: "Be Kind & Respectful",
      description: "Use AI to create positive, helpful content. Never use it to bully, spread rumors, or create harmful content about others.",
      color: "text-pink-600",
      bg: "bg-pink-50 dark:bg-pink-950/30"
    }
  ];

  const dosDonts = {
    dos: [
      "Use AI as a learning tool to understand concepts",
      "Ask an adult when you're unsure about something",
      "Verify AI-generated information with trusted sources",
      "Create positive and creative content",
      "Respect copyright and give credit to original creators",
      "Use AI to improve your homework, not replace your thinking"
    ],
    donts: [
      "Don't share personal or sensitive information",
      "Don't upload photos of yourself or others without permission",
      "Don't use AI to cheat on assignments or tests",
      "Don't create fake or misleading content",
      "Don't believe everything AI tells you without checking",
      "Don't use AI tools without adult supervision"
    ]
  };

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
            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-r from-blue-600 to-purple-600 rounded-full blur-2xl opacity-50 animate-pulse" />
              <Shield className="relative h-20 w-20 text-blue-600 dark:text-blue-400" />
            </div>
          </div>
          <h1 className="text-5xl font-bold bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 bg-clip-text text-transparent">
            AI Safety & Responsible Use
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto">
            Learn how to use AI tools safely, responsibly, and ethically
          </p>
        </div>

        {/* Important Notice */}
        <Alert className="mb-8 border-2 border-orange-300 dark:border-orange-700 bg-orange-50 dark:bg-orange-950/30">
          <AlertTriangle className="h-5 w-5 text-orange-600" />
          <AlertDescription className="text-base text-orange-900 dark:text-orange-100 ml-2">
            <strong>Important:</strong> Always ask a parent, guardian, or teacher before using any AI tool or website. 
            This playground is for educational purposes with adult supervision.
          </AlertDescription>
        </Alert>

        {/* Safety Tips */}
        <div className="mb-12">
          <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-6">Safety Guidelines</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {safetyTips.map((tip, index) => {
              const IconComponent = tip.icon;
              return (
                <Card key={index} className="border-2 hover:shadow-lg transition-shadow">
                  <CardHeader className={tip.bg}>
                    <div className="flex items-center gap-3 mb-2">
                      <IconComponent className={`h-8 w-8 ${tip.color}`} />
                      <CardTitle className="text-xl">{tip.title}</CardTitle>
                    </div>
                  </CardHeader>
                  <CardContent className="pt-4">
                    <CardDescription className="text-base leading-relaxed text-gray-700 dark:text-gray-300">
                      {tip.description}
                    </CardDescription>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </div>

        {/* Do's and Don'ts */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
          {/* Do's */}
          <Card className="border-2 border-green-300 dark:border-green-700">
            <CardHeader className="bg-green-50 dark:bg-green-950/30">
              <CardTitle className="text-2xl flex items-center gap-3 text-green-700 dark:text-green-300">
                <CheckCircle className="h-6 w-6" />
                ✓ DO's - Good Practices
              </CardTitle>
            </CardHeader>
            <CardContent className="pt-6">
              <ul className="space-y-3">
                {dosDonts.dos.map((item, index) => (
                  <li key={index} className="flex items-start gap-3">
                    <CheckCircle className="h-5 w-5 text-green-600 shrink-0 mt-0.5" />
                    <span className="text-gray-700 dark:text-gray-300">{item}</span>
                  </li>
                ))}
              </ul>
            </CardContent>
          </Card>

          {/* Don'ts */}
          <Card className="border-2 border-red-300 dark:border-red-700">
            <CardHeader className="bg-red-50 dark:bg-red-950/30">
              <CardTitle className="text-2xl flex items-center gap-3 text-red-700 dark:text-red-300">
                <AlertTriangle className="h-6 w-6" />
                ✗ DON'Ts - Avoid These
              </CardTitle>
            </CardHeader>
            <CardContent className="pt-6">
              <ul className="space-y-3">
                {dosDonts.donts.map((item, index) => (
                  <li key={index} className="flex items-start gap-3">
                    <AlertTriangle className="h-5 w-5 text-red-600 shrink-0 mt-0.5" />
                    <span className="text-gray-700 dark:text-gray-300">{item}</span>
                  </li>
                ))}
              </ul>
            </CardContent>
          </Card>
        </div>

        {/* Resources */}
        <Card className="border-2 border-purple-300 dark:border-purple-700">
          <CardHeader className="bg-purple-50 dark:bg-purple-950/30">
            <CardTitle className="text-2xl flex items-center gap-3">
              <Globe className="h-6 w-6 text-purple-600" />
              Learn More About AI Safety
            </CardTitle>
          </CardHeader>
          <CardContent className="pt-6">
            <div className="space-y-4">
              <div>
                <h3 className="font-semibold text-lg mb-2 text-gray-900 dark:text-white">UNESCO AI Ethics Guide for Youth</h3>
                <p className="text-gray-600 dark:text-gray-400 mb-3">
                  Learn about ethical AI use and global guidelines for responsible technology
                </p>
                <a
                  href="https://unesdoc.unesco.org/ark:/48223/pf0000385308"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-block"
                >
                  <Button variant="outline" className="border-purple-300 text-purple-700 hover:bg-purple-50 dark:border-purple-700 dark:text-purple-300">
                    Visit UNESCO Guide
                    <Globe className="ml-2 h-4 w-4" />
                  </Button>
                </a>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Call to Action */}
        <div className="mt-12 text-center">
          <Link to="/ai">
            <Button size="lg" className="bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700">
              Start Learning Safely
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
}











