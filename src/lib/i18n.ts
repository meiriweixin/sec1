export const translations = {
  en: {
    // Navigation
    dashboard: "Dashboard",
    subjects: "Subjects",
    progress: "Progress",
    profile: "Profile",
    logout: "Logout",
    
    // Auth
    login: "Login",
    email: "Email",
    password: "Password",
    continueAsGuest: "Continue as Guest",
    welcomeBack: "Welcome Back",
    loginToContinue: "Login to continue your learning journey",
    
    // Dashboard
    welcomeMessage: "Welcome to your learning journey!",
    chooseSubject: "Choose a subject to begin",
    recentActivity: "Recent Activity",
    continueWhere: "Continue where you left off",
    startLearning: "Start Learning",
    
    // Subjects & Chapters
    chapters: "Chapters",
    objectives: "Learning Objectives",
    startChapter: "Start Chapter",
    continueChapter: "Continue Chapter",
    completed: "Completed",
    inProgress: "In Progress",
    notStarted: "Not Started",
    
    // Lessons
    lesson: "Lesson",
    nextSection: "Next Section",
    previousSection: "Previous Section",
    startExercises: "Start Exercises",
    backToChapter: "Back to Chapter",
    
    // Exercises
    exercise: "Exercise",
    question: "Question",
    submit: "Submit",
    next: "Next",
    previous: "Previous",
    hint: "Hint",
    showHint: "Show Hint",
    explanation: "Explanation",
    correct: "Correct!",
    incorrect: "Incorrect",
    tryAgain: "Try Again",
    score: "Score",
    complete: "Complete",
    
    // Progress
    yourProgress: "Your Progress",
    timeSpent: "Time Spent",
    chaptersCompleted: "Chapters Completed",
    exercisesCompleted: "Exercises Completed",
    averageScore: "Average Score",
    streak: "Day Streak",
    badges: "Badges",
    
    // Common
    loading: "Loading...",
    error: "Error",
    retry: "Retry",
    close: "Close",
    save: "Save",
    cancel: "Cancel",
    settings: "Settings",
    language: "Language",
    theme: "Theme",
    light: "Light",
    dark: "Dark",
    system: "System",
  },
  zh: {
    // Navigation
    dashboard: "仪表板",
    subjects: "科目",
    progress: "进度",
    profile: "个人资料",
    logout: "登出",
    
    // Auth
    login: "登录",
    email: "邮箱",
    password: "密码",
    continueAsGuest: "以访客身份继续",
    welcomeBack: "欢迎回来",
    loginToContinue: "登录以继续您的学习之旅",
    
    // Dashboard
    welcomeMessage: "欢迎来到您的学习之旅！",
    chooseSubject: "选择一个科目开始学习",
    recentActivity: "最近活动",
    continueWhere: "从上次停止的地方继续",
    startLearning: "开始学习",
    
    // Subjects & Chapters
    chapters: "章节",
    objectives: "学习目标",
    startChapter: "开始章节",
    continueChapter: "继续章节",
    completed: "已完成",
    inProgress: "进行中",
    notStarted: "未开始",
    
    // Lessons
    lesson: "课程",
    nextSection: "下一节",
    previousSection: "上一节",
    startExercises: "开始练习",
    backToChapter: "返回章节",
    
    // Exercises
    exercise: "练习",
    question: "问题",
    submit: "提交",
    next: "下一个",
    previous: "上一个",
    hint: "提示",
    showHint: "显示提示",
    explanation: "解释",
    correct: "正确！",
    incorrect: "错误",
    tryAgain: "再试一次",
    score: "分数",
    complete: "完成",
    
    // Progress
    yourProgress: "您的进度",
    timeSpent: "学习时间",
    chaptersCompleted: "已完成章节",
    exercisesCompleted: "已完成练习",
    averageScore: "平均分数",
    streak: "连续天数",
    badges: "徽章",
    
    // Common
    loading: "加载中...",
    error: "错误",
    retry: "重试",
    close: "关闭",
    save: "保存",
    cancel: "取消",
    settings: "设置",
    language: "语言",
    theme: "主题",
    light: "浅色",
    dark: "深色",
    system: "系统",
  }
};

export const useTranslations = (language: 'en' | 'zh') => {
  return translations[language];
};