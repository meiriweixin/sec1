# Implementation Tasks

## 1. Data Model & State Management

- [x] 1.1 Extend `Progress` interface in `src/lib/store.ts` to add `attempts[]`, `reviewSchedule`, and `retentionScore`
- [x] 1.2 Implement progress data migration function `migrateProgressToV2()` with backward compatibility checks
- [x] 1.3 Add migration flag to localStorage to prevent re-running migration on subsequent loads
- [x] 1.4 Create new store actions: `addExerciseAttempt()`, `updateReviewSchedule()`, `getReviewQueue()`
- [x] 1.5 Update `updateProgress()` action to handle both initial attempts and review attempts
- [x] 1.6 Add store selector `getDueReviews()` to filter chapters with `nextReviewDate <= today`

## 2. Spaced Repetition Algorithm

- [x] 2.1 Create `src/lib/spaced-repetition.ts` module
- [x] 2.2 Implement `calculateEasinessFactor(score: number): number` (range 1.3-3.0)
- [x] 2.3 Implement `calculateNextInterval(currentInterval: number, easinessFactor: number): number` (capped at 30 days)
- [x] 2.4 Implement `calculateReviewPriority(chapter: Progress): number` based on overdue days, score, and importance
- [x] 2.5 Implement `shouldResetInterval(score: number): boolean` (returns true if score <60%)
- [ ] 2.6 Write unit tests for SM-2 algorithm edge cases (first attempt, max interval, reset conditions) - DEFERRED

## 3. Review Mode UI - Chapter View

- [x] 3.1 Add `mode` query parameter handling to `src/pages/ChapterView.tsx` (read from `useSearchParams()`)
- [x] 3.2 Add "Review Mode" badge to page header when `mode=review`
- [x] 3.3 Modify exercise completion logic to check `mode` and set `isReview` flag accordingly
- [x] 3.4 Add "Exit Review Mode" button in header when in review mode
- [x] 3.5 Update success messages to differentiate review attempts ("Review completed!" vs. "Exercise completed!")
- [x] 3.6 Prevent review mode from updating `completed` status (only update attempt history)

## 4. Review Mode UI - Chapter Cards

- [x] 4.1 Add "Review" button to completed chapters in `src/components/cards/chapter-card.tsx`
- [x] 4.2 Add "Due for Review" badge to chapter cards using `isReviewDue()` check
- [x] 4.3 Add "Next review in X days" text for non-due completed chapters
- [x] 4.4 Style badges with color coding (yellow for due today, red for overdue >3 days)
- [x] 4.5 Add tooltip on hover showing exact next review date

## 5. Exercise Player Enhancements

- [ ] 5.1 Add "Retry Exercise" button to exercise completion screen in `src/components/exercises/exercise-player.tsx`
- [ ] 5.2 Implement exercise reset logic (clear answers, reset timer, regenerate questions if needed)
- [ ] 5.3 Track multiple attempts per exercise in `onComplete()` callback
- [ ] 5.4 Add attempt history display to exercise detail view (show all previous scores/dates)
- [ ] 5.5 Implement score trend line chart using Recharts (LineChart with attempts on X-axis, scores on Y-axis)

## 6. Exercise Randomization

- [ ] 6.1 Create `src/lib/exercise-randomizer.ts` utility module
- [ ] 6.2 Implement `shuffleChoices(exercise: MCQExercise): MCQExercise` to randomize option order
- [ ] 6.3 Implement `shuffleDragOrder(exercise: DragOrderExercise): DragOrderExercise` to randomize initial items
- [ ] 6.4 Update `src/components/exercises/mcq-exercise.tsx` to shuffle choices when `isReview=true`
- [ ] 6.5 Update `src/components/exercises/drag-order-exercise.tsx` to shuffle items when `isReview=true`
- [ ] 6.6 Add seeded randomization to ensure consistent shuffle within same attempt (use attempt timestamp as seed)

## 7. Review Queue Dashboard Widget

- [ ] 7.1 Create `src/components/cards/ReviewQueueCard.tsx` component
- [ ] 7.2 Fetch top 5 due chapters using `getDueReviews()` and sort by priority
- [ ] 7.3 Display each chapter with subject name, title, and days since last review
- [ ] 7.4 Add "Start Review" button for each chapter (links to chapter with `?mode=review`)
- [ ] 7.5 Show "You're all caught up!" state when queue is empty
- [ ] 7.6 Add "5 more chapters available" indicator if total due > 5
- [ ] 7.7 Integrate `ReviewQueueCard` into `src/pages/Dashboard.tsx`

## 8. Review Session Summary

- [ ] 8.1 Create `src/components/review/ReviewSummary.tsx` component
- [ ] 8.2 Calculate and display overall review session score (average of all attempts)
- [ ] 8.3 Calculate and display time spent in review session
- [ ] 8.4 Calculate and display improvement percentage vs. previous attempt
- [ ] 8.5 Show confetti animation (using existing confetti logic) if improvement ≥10%
- [ ] 8.6 Display calculated next review date based on SM-2 algorithm
- [ ] 8.7 Add "Continue Reviewing" button to navigate to next queued chapter

## 9. Review Queue Page (Optional Enhancement)

- [ ] 9.1 Create `src/pages/ReviewQueue.tsx` page component
- [ ] 9.2 Display full list of all due reviews (not capped at 5)
- [ ] 9.3 Add filtering by subject (All, Math, Science, English, Chinese)
- [ ] 9.4 Add sorting options (By Priority, By Subject, By Overdue Days)
- [ ] 9.5 Add "Snooze" button for each chapter (postpone by 1 day)
- [ ] 9.6 Add route `/review` to `src/App.tsx`
- [ ] 9.7 Add navigation link to full review queue from dashboard widget

## 10. Bilingual Support

- [x] 10.1 Add review-related translations to `src/lib/i18n.ts`:
  - `reviewMode`, `dueForReview`, `nextReviewIn`, `startReview`, `retryExercise`
  - `reviewCompleted`, `youreCaughtUp`, `reviewQueue`, `snoozeReview`
  - `improvementVsPrevious`, `retentionScore`, `daysOverdue`
- [x] 10.2 Update all review UI components to use `useTranslations()` hook
- [ ] 10.3 Test all review features in both English and Chinese language modes - REQUIRES MANUAL TESTING

## 11. Testing & Validation

- [ ] 11.1 Test migration from existing progress data (create test fixture with legacy data)
- [ ] 11.2 Test backward compatibility (ensure old features still work after migration)
- [ ] 11.3 Test review mode flow: enter review → complete exercises → exit review → verify attempt history
- [ ] 11.4 Test SM-2 algorithm calculations with various score scenarios (high, medium, low, failing)
- [ ] 11.5 Test review queue priority ordering with multiple due chapters
- [ ] 11.6 Test localStorage storage limits (simulate 1 year of attempts, verify <5MB usage)
- [ ] 11.7 Test exercise randomization (verify MCQ choices shuffle, drag-order items shuffle)
- [ ] 11.8 Test review session summary calculations (score, time, improvement percentage)
- [ ] 11.9 Test snooze functionality (verify date postponement and queue removal)
- [ ] 11.10 Test bilingual support (all review text appears in both languages)

## 12. Documentation & Polish

- [ ] 12.1 Add JSDoc comments to new store actions and spaced repetition functions
- [ ] 12.2 Update `CLAUDE.md` with review mode usage instructions
- [ ] 12.3 Add tooltip help text explaining spaced repetition benefits
- [ ] 12.4 Add onboarding toast on first review: "Tip: Regular reviews help long-term retention!"
- [ ] 12.5 Ensure all new components follow project conventions (kebab-case files, PascalCase components)
- [ ] 12.6 Run `npm run lint` and fix any linting errors
- [ ] 12.7 Test responsive design for review queue widget on mobile screens
- [ ] 12.8 Verify accessibility (keyboard navigation, screen reader labels for review buttons)

## 13. Performance Optimization (Post-MVP)

- [ ] 13.1 Implement lazy loading for attempt history (only load for current chapter)
- [ ] 13.2 Add debouncing to review schedule recalculations (batch updates every 5 seconds)
- [ ] 13.3 Index exercises by `nextReviewDate` for O(1) queue retrieval
- [ ] 13.4 Implement rolling window for attempt history (keep last 50 attempts, compress older)
- [ ] 13.5 Add storage monitoring (warn user if localStorage approaching 80% capacity)
