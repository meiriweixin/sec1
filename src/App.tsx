import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Index from "./pages/Index";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Subjects from "./pages/Subjects";
import SubjectDetail from "./pages/SubjectDetail";
import ChapterView from "./pages/ChapterView";
import AIPlayground from "./pages/AIPlayground";
import AIModuleDetail from "./pages/AIModuleDetail";
import AIProgress from "./pages/AIProgress";
import AISafety from "./pages/AISafety";
import NotFound from "./pages/NotFound";

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <TooltipProvider>
      <Toaster />
      <Sonner />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Index />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/subjects" element={<Subjects />} />
          <Route path="/subjects/:subjectId" element={<SubjectDetail />} />
          <Route path="/subjects/:subjectId/:chapterId" element={<ChapterView />} />
          <Route path="/ai" element={<AIPlayground />} />
          <Route path="/ai/modules/:moduleId" element={<AIModuleDetail />} />
          <Route path="/ai/progress" element={<AIProgress />} />
          <Route path="/ai/safety" element={<AISafety />} />
          {/* ADD ALL CUSTOM ROUTES ABOVE THE CATCH-ALL "*" ROUTE */}
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </TooltipProvider>
  </QueryClientProvider>
);

export default App;
