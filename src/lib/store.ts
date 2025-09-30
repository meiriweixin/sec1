import { create } from 'zustand';
import { persist } from 'zustand/middleware';

export interface User {
  id: string;
  email: string;
  name: string;
  isGuest?: boolean;
}

export interface Progress {
  subjectId: string;
  chapterId: string;
  sectionsCompleted: string[];
  exercisesCompleted: string[];
  exerciseScores: Record<string, number>;
  totalTimeSpent: number;
  lastAccessed: string;
  completed: boolean;
}

export interface UserState {
  user: User | null;
  language: 'en' | 'zh';
  theme: 'light' | 'dark' | 'system';
  progress: Progress[];
  currentSubject: string | null;
  currentChapter: string | null;
  
  // Actions
  login: (user: User) => void;
  logout: () => void;
  setLanguage: (language: 'en' | 'zh') => void;
  setTheme: (theme: 'light' | 'dark' | 'system') => void;
  setCurrentSubject: (subjectId: string | null) => void;
  setCurrentChapter: (chapterId: string | null) => void;
  updateProgress: (progress: Partial<Progress> & { subjectId: string; chapterId: string }) => void;
  getChapterProgress: (subjectId: string, chapterId: string) => Progress | undefined;
  getSubjectProgress: (subjectId: string) => Progress[];
}

export const useStore = create<UserState>()(
  persist(
    (set, get) => ({
      user: null,
      language: 'en',
      theme: 'system',
      progress: [],
      currentSubject: null,
      currentChapter: null,

      login: (user) => set({ user }),
      
      logout: () => set({ 
        user: null, 
        currentSubject: null, 
        currentChapter: null 
      }),
      
      setLanguage: (language) => set({ language }),
      
      setTheme: (theme) => set({ theme }),
      
      setCurrentSubject: (subjectId) => set({ currentSubject: subjectId }),
      
      setCurrentChapter: (chapterId) => set({ currentChapter: chapterId }),
      
      updateProgress: (newProgress) => {
        const state = get();
        const existingIndex = state.progress.findIndex(
          p => p.subjectId === newProgress.subjectId && p.chapterId === newProgress.chapterId
        );
        
        const updatedProgress = {
          subjectId: newProgress.subjectId,
          chapterId: newProgress.chapterId,
          sectionsCompleted: [],
          exercisesCompleted: [],
          exerciseScores: {},
          totalTimeSpent: 0,
          lastAccessed: new Date().toISOString(),
          completed: false,
          ...newProgress,
        };
        
        if (existingIndex >= 0) {
          const newProgressArray = [...state.progress];
          newProgressArray[existingIndex] = {
            ...newProgressArray[existingIndex],
            ...updatedProgress,
          };
          set({ progress: newProgressArray });
        } else {
          set({ progress: [...state.progress, updatedProgress] });
        }
      },
      
      getChapterProgress: (subjectId, chapterId) => {
        return get().progress.find(
          p => p.subjectId === subjectId && p.chapterId === chapterId
        );
      },
      
      getSubjectProgress: (subjectId) => {
        return get().progress.filter(p => p.subjectId === subjectId);
      },
    }),
    {
      name: 'sg-learning-app-storage',
      partialize: (state) => ({
        user: state.user,
        language: state.language,
        theme: state.theme,
        progress: state.progress,
      }),
    }
  )
);