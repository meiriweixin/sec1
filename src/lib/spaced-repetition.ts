import type { Progress, ReviewSchedule } from './store';

/**
 * Calculates the Easiness Factor (EF) based on performance score
 * EF determines how quickly intervals increase
 *
 * @param score - Performance score (0-100)
 * @returns Easiness Factor (1.3 - 3.0)
 *
 * Formula: EF = 1.3 + (score/100 × 1.7)
 * - Score 0%: EF = 1.3 (slowest progression)
 * - Score 50%: EF = 2.15 (medium)
 * - Score 100%: EF = 3.0 (fastest progression)
 */
export function calculateEasinessFactor(score: number): number {
  // Clamp score to 0-100 range
  const clampedScore = Math.max(0, Math.min(100, score));

  // EF ranges from 1.3 to 3.0
  const ef = 1.3 + (clampedScore / 100) * 1.7;

  return Math.max(1.3, Math.min(3.0, ef));
}

/**
 * Calculates the next review interval in days
 * Implements SM-2 algorithm with educational adjustments
 *
 * @param currentInterval - Current interval in days
 * @param easinessFactor - Easiness factor (1.3 - 3.0)
 * @returns Next interval in days (capped at 30)
 *
 * Formula: newInterval = currentInterval × easinessFactor
 * Max interval: 30 days (students need regular practice)
 * Min interval: 1 day (prevent same-day spam)
 */
export function calculateNextInterval(
  currentInterval: number,
  easinessFactor: number
): number {
  const newInterval = Math.max(1, currentInterval * easinessFactor);

  // Cap at 30 days for educational context
  return Math.min(30, Math.round(newInterval));
}

/**
 * Determines if the review interval should be reset due to poor performance
 *
 * @param score - Performance score (0-100)
 * @returns true if score < 60% (failing threshold)
 */
export function shouldResetInterval(score: number): boolean {
  return score < 60;
}

/**
 * Calculates review priority score for sorting the review queue
 * Higher scores = higher priority (more urgent to review)
 *
 * Priority factors:
 * 1. Days overdue (×2 multiplier, max 30 days bonus)
 * 2. Low retention score ((70 - score) / 2)
 * 3. Chapter importance (foundational topics ×1.5)
 *
 * @param chapter - Progress object with review schedule
 * @param chapterIndex - Index of chapter in subject (0-based)
 * @returns Priority score (higher = more urgent)
 */
export function calculateReviewPriority(
  chapter: Progress,
  chapterIndex: number = 0
): number {
  if (!chapter.reviewSchedule || !chapter.completed) {
    return 0;
  }

  let priority = 0;
  const now = new Date();
  const nextReview = new Date(chapter.reviewSchedule.nextReviewDate);

  // Factor 1: Days overdue (×2 multiplier, capped at 30 days)
  if (nextReview <= now) {
    const daysOverdue = Math.min(
      30,
      (now.getTime() - nextReview.getTime()) / (1000 * 60 * 60 * 24)
    );
    priority += daysOverdue * 2;
  }

  // Factor 2: Low retention score
  const retentionScore = chapter.retentionScore || 70;
  if (retentionScore < 70) {
    priority += (70 - retentionScore) / 2;
  }

  // Factor 3: Foundational chapters (first 3 in subject)
  if (chapterIndex < 3) {
    priority *= 1.5;
  }

  return priority;
}

/**
 * Calculates the next review date based on current performance
 * Implements full SM-2 algorithm logic
 *
 * @param currentSchedule - Current review schedule
 * @param sessionScore - Average score from review session (0-100)
 * @returns Updated review schedule
 */
export function calculateNextReviewSchedule(
  currentSchedule: ReviewSchedule,
  sessionScore: number
): ReviewSchedule {
  // If score is too low, reset to day 1
  if (shouldResetInterval(sessionScore)) {
    return {
      nextReviewDate: new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString(),
      intervalDays: 1,
      easinessFactor: Math.max(1.3, currentSchedule.easinessFactor - 0.2),
    };
  }

  // Calculate new EF based on performance
  const newEF = calculateEasinessFactor(sessionScore);

  // Calculate next interval
  const nextInterval = calculateNextInterval(currentSchedule.intervalDays, newEF);

  // Calculate next review date
  const nextReviewDate = new Date(
    Date.now() + nextInterval * 24 * 60 * 60 * 1000
  ).toISOString();

  return {
    nextReviewDate,
    intervalDays: nextInterval,
    easinessFactor: newEF,
  };
}

/**
 * Creates initial review schedule for newly completed chapter
 *
 * @param averageScore - Average score across all exercises in chapter
 * @returns Initial review schedule (1 day interval)
 */
export function createInitialReviewSchedule(averageScore: number): ReviewSchedule {
  return {
    nextReviewDate: new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString(),
    intervalDays: 1,
    easinessFactor: calculateEasinessFactor(averageScore),
  };
}

/**
 * Calculates retention score from multiple attempts
 * Uses weighted average favoring recent attempts
 *
 * @param scores - Array of scores in chronological order
 * @returns Weighted retention score (0-100)
 *
 * Weights: [most recent: 0.5, previous: 0.3, older: 0.2]
 */
export function calculateRetentionScore(scores: number[]): number {
  if (scores.length === 0) return 0;
  if (scores.length === 1) return scores[0];

  // Use last 3 scores
  const recentScores = scores.slice(-3).reverse();
  const weights = [0.5, 0.3, 0.2];

  const weightedScore = recentScores.reduce(
    (sum, score, idx) => sum + score * (weights[idx] || 0),
    0
  );

  return Math.round(weightedScore);
}
