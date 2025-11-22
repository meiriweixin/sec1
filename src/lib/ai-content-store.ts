/**
 * AI-Generated Content Storage
 * Manages storage and retrieval of AI-generated chapters
 * Stored separately from main content.json to allow dynamic addition
 */

import type { GeneratedContent } from './azure-openai';

export interface AIGeneratedChapter extends GeneratedContent {
  id: string;
  createdAt: string;
  createdBy: string; // userId
  subjectId: string;
  isAIGenerated: true;
}

const STORAGE_KEY = 'sg-learning-ai-chapters';

class AIContentStore {
  /**
   * Get all AI-generated chapters for a user and subject
   */
  getChapters(userId: string, subjectId: string): AIGeneratedChapter[] {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (!stored) {
        console.log('[AI Store] No chapters in localStorage');
        return [];
      }

      const allChapters: AIGeneratedChapter[] = JSON.parse(stored);
      console.log('[AI Store] Total chapters in storage:', allChapters.length);
      const filtered = allChapters.filter(
        (ch) => ch.createdBy === userId && ch.subjectId === subjectId
      ).map(ch => ({ ...ch, id: ch.id || ch.chapterId }));
      console.log('[AI Store] Filtered chapters for user', userId, 'subject', subjectId, ':', filtered.length);
      return filtered;
    } catch (error) {
      console.error('Error loading AI chapters:', error);
      return [];
    }
  }

  /**
   * Get a specific AI-generated chapter
   */
  getChapter(userId: string, chapterId: string): AIGeneratedChapter | null {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (!stored) return null;

      const allChapters: AIGeneratedChapter[] = JSON.parse(stored);
      const chapter = allChapters.find((ch) => ch.createdBy === userId && ch.chapterId === chapterId);

      if (!chapter) return null;
      return { ...chapter, id: chapter.id || chapter.chapterId };
    } catch (error) {
      console.error('Error loading AI chapter:', error);
      return null;
    }
  }

  /**
   * Save a new AI-generated chapter
   */
  saveChapter(
    userId: string,
    subjectId: string,
    content: GeneratedContent
  ): AIGeneratedChapter {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      const allChapters: AIGeneratedChapter[] = stored ? JSON.parse(stored) : [];

      const aiChapter: AIGeneratedChapter = {
        ...content,
        id: content.chapterId,
        subjectId,
        createdBy: userId,
        createdAt: new Date().toISOString(),
        isAIGenerated: true,
      };

      allChapters.push(aiChapter);
      localStorage.setItem(STORAGE_KEY, JSON.stringify(allChapters));
      console.log('[AI Store] Saved chapter to localStorage. Total chapters now:', allChapters.length);
      console.log('[AI Store] Chapter details:', { id: aiChapter.id, userId, subjectId, title: aiChapter.title });

      return aiChapter;
    } catch (error) {
      console.error('Error saving AI chapter:', error);
      throw error;
    }
  }

  /**
   * Update an existing AI-generated chapter
   */
  updateChapter(userId: string, chapterId: string, updates: Partial<GeneratedContent>): boolean {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (!stored) return false;

      const allChapters: AIGeneratedChapter[] = JSON.parse(stored);
      const index = allChapters.findIndex(
        (ch) => ch.createdBy === userId && ch.chapterId === chapterId
      );

      if (index === -1) return false;

      allChapters[index] = {
        ...allChapters[index],
        ...updates,
      };

      localStorage.setItem(STORAGE_KEY, JSON.stringify(allChapters));
      return true;
    } catch (error) {
      console.error('Error updating AI chapter:', error);
      return false;
    }
  }

  /**
   * Delete an AI-generated chapter
   */
  deleteChapter(userId: string, chapterId: string): boolean {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (!stored) return false;

      const allChapters: AIGeneratedChapter[] = JSON.parse(stored);
      const filtered = allChapters.filter(
        (ch) => !(ch.createdBy === userId && ch.chapterId === chapterId)
      );

      if (filtered.length === allChapters.length) return false; // Not found

      localStorage.setItem(STORAGE_KEY, JSON.stringify(filtered));
      return true;
    } catch (error) {
      console.error('Error deleting AI chapter:', error);
      return false;
    }
  }

  /**
   * Get all chapters for a user (across all subjects)
   */
  getAllUserChapters(userId: string): AIGeneratedChapter[] {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (!stored) return [];

      const allChapters: AIGeneratedChapter[] = JSON.parse(stored);
      return allChapters
        .filter((ch) => ch.createdBy === userId)
        .map(ch => ({ ...ch, id: ch.id || ch.chapterId }));
    } catch (error) {
      console.error('Error loading user AI chapters:', error);
      return [];
    }
  }

  /**
   * Clear all AI-generated chapters (for testing/debugging)
   */
  clearAll(): void {
    localStorage.removeItem(STORAGE_KEY);
  }
}

// Export singleton instance
export const aiContentStore = new AIContentStore();
