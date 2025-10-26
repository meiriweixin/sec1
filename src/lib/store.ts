import { create } from 'zustand';
import { persist } from 'zustand/middleware';

export interface User {
  id: string;
  email: string;
  name: string;
  isGuest?: boolean;
  provider?: 'email' | 'google' | 'guest';
  photoURL?: string;
}

export interface ExerciseAttempt {
  exerciseId: string;
  attemptedAt: string; // ISO 8601
  score: number; // 0-100
  timeSpent: number; // seconds
  isReview: boolean; // true if attempted in review mode
}

export interface ReviewSchedule {
  nextReviewDate: string; // ISO 8601
  intervalDays: number;
  easinessFactor: number; // 1.3 - 3.0
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
  // Review mode fields (v2)
  attempts?: ExerciseAttempt[]; // Full attempt history
  reviewSchedule?: ReviewSchedule; // Spaced repetition metadata
  retentionScore?: number; // 0-100, weighted average of recent attempts
}

export interface AIModuleProgress {
  done: boolean;
  doneAt?: string;
}

export interface UserState {
  user: User | null;
  language: 'en' | 'zh';
  theme: 'light' | 'dark' | 'system';
  progress: Progress[];
  aiProgress: Record<string, AIModuleProgress>;
  currentSubject: string | null;
  currentChapter: string | null;
  _hasHydrated: boolean; // Internal flag to track if store has loaded from localStorage

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
  toggleAIModuleComplete: (moduleId: string) => void;
  addExerciseAttempt: (subjectId: string, chapterId: string, attempt: ExerciseAttempt) => void;
  updateReviewSchedule: (subjectId: string, chapterId: string, schedule: ReviewSchedule) => void;
  getReviewQueue: () => Progress[];
  getDueReviews: () => Progress[];
  setHasHydrated: (state: boolean) => void; // Method to set hydration state
}

/**
 * Migrates legacy progress data to v2 format with review mode fields
 * @param oldProgress - Legacy progress object without review fields
 * @returns Migrated progress object with attempts, reviewSchedule, and retentionScore
 */
function migrateProgressToV2(oldProgress: Progress): Progress {
  // Skip if already migrated
  if (oldProgress.attempts && oldProgress.reviewSchedule) {
    return oldProgress;
  }

  // Convert exercisesCompleted to attempts array
  const attempts: ExerciseAttempt[] = oldProgress.exercisesCompleted.map(exerciseId => ({
    exerciseId,
    attemptedAt: oldProgress.lastAccessed || new Date().toISOString(),
    score: oldProgress.exerciseScores[exerciseId] || 0,
    timeSpent: 0, // Unknown for legacy data
    isReview: false, // First attempts are never reviews
  }));

  // Calculate average score for initial easiness factor
  const avgScore = attempts.length > 0
    ? attempts.reduce((sum, att) => sum + att.score, 0) / attempts.length
    : 60; // Default to medium difficulty

  // Calculate initial easiness factor: EF = 1.3 + (score/100 × 1.7)
  const easinessFactor = Math.max(1.3, Math.min(3.0, 1.3 + (avgScore / 100) * 1.7));

  // Set initial review date to 1 day from last access if chapter is completed
  const nextReviewDate = oldProgress.completed
    ? new Date(new Date(oldProgress.lastAccessed || Date.now()).getTime() + 24 * 60 * 60 * 1000).toISOString()
    : new Date(Date.now() + 365 * 24 * 60 * 60 * 1000).toISOString(); // Far future if not completed

  return {
    ...oldProgress,
    attempts,
    reviewSchedule: {
      nextReviewDate,
      intervalDays: 1,
      easinessFactor,
    },
    retentionScore: avgScore,
  };
}

export const useStore = create<UserState>()(
  persist(
    (set, get) => ({
      user: null,
      language: 'en',
      theme: 'system',
      progress: [],
      aiProgress: {},
      currentSubject: null,
      currentChapter: null,
      _hasHydrated: false,

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

      toggleAIModuleComplete: (moduleId) => {
        const state = get();
        const currentProgress = state.aiProgress[moduleId];

        set({
          aiProgress: {
            ...state.aiProgress,
            [moduleId]: {
              done: !currentProgress?.done,
              doneAt: !currentProgress?.done ? new Date().toISOString() : undefined,
            },
          },
        });
      },

      /**
       * Adds an exercise attempt to the progress history
       */
      addExerciseAttempt: (subjectId, chapterId, attempt) => {
        const state = get();
        const existingProgress = state.progress.find(
          p => p.subjectId === subjectId && p.chapterId === chapterId
        );

        if (!existingProgress) return;

        const migratedProgress = migrateProgressToV2(existingProgress);
        const updatedAttempts = [...(migratedProgress.attempts || []), attempt];

        // Calculate retention score (weighted average of recent attempts)
        const recentAttempts = updatedAttempts
          .filter(att => att.exerciseId === attempt.exerciseId)
          .slice(-3); // Last 3 attempts for this exercise

        let retentionScore = migratedProgress.retentionScore || 0;
        if (recentAttempts.length >= 2) {
          const weights = [0.5, 0.3, 0.2];
          retentionScore = recentAttempts
            .slice(-3)
            .reverse()
            .reduce((sum, att, idx) => sum + att.score * (weights[idx] || 0), 0);
        } else if (recentAttempts.length === 1) {
          retentionScore = recentAttempts[0].score;
        }

        const newProgressArray = state.progress.map(p =>
          p.subjectId === subjectId && p.chapterId === chapterId
            ? {
                ...migratedProgress,
                attempts: updatedAttempts,
                retentionScore,
                lastAccessed: new Date().toISOString(),
              }
            : p
        );

        set({ progress: newProgressArray });
      },

      /**
       * Updates the review schedule for a chapter
       */
      updateReviewSchedule: (subjectId, chapterId, schedule) => {
        const state = get();
        const newProgressArray = state.progress.map(p => {
          if (p.subjectId === subjectId && p.chapterId === chapterId) {
            const migrated = migrateProgressToV2(p);
            return {
              ...migrated,
              reviewSchedule: schedule,
            };
          }
          return p;
        });

        set({ progress: newProgressArray });
      },

      /**
       * Gets all chapters in review queue (due or overdue)
       */
      getReviewQueue: () => {
        const state = get();
        const now = new Date().toISOString();

        return state.progress
          .map(migrateProgressToV2)
          .filter(
            p =>
              p.completed &&
              p.reviewSchedule &&
              p.reviewSchedule.nextReviewDate <= now
          );
      },

      /**
       * Gets chapters due for review (same as getReviewQueue, alias for clarity)
       */
      getDueReviews: () => {
        return get().getReviewQueue();
      },

      setHasHydrated: (state) => set({ _hasHydrated: state }),
    }),
    {
      name: 'sg-learning-app-storage',
      partialize: (state) => ({
        user: state.user,
        language: state.language,
        theme: state.theme,
        progress: state.progress,
        aiProgress: state.aiProgress,
      }),
      onRehydrateStorage: () => {
        // This runs synchronously when the store is created
        // Return a callback that handles the rehydrated state
        return (state, error) => {
          if (error) {
            console.error('Error during hydration:', error);
          }

          if (state) {
            // Check migration flag
            const migrationFlag = localStorage.getItem('sg-learning-progress-migration-v2');

            if (!migrationFlag) {
              // Migrate all progress items
              const migratedProgress = state.progress.map(migrateProgressToV2);
              state.progress = migratedProgress;

              // Set migration flag to prevent re-running
              localStorage.setItem('sg-learning-progress-migration-v2', 'completed');
            }

            // Mark hydration as complete after rehydration
            state._hasHydrated = true;
          }
        };
      },
    }
  )
);

// Create an alias for compatibility
export const useUserStore = useStore;