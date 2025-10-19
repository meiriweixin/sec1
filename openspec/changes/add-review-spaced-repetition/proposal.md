# Add Review Mode and Spaced Repetition

## Why

Students currently complete exercises once and move on, with no systematic way to revisit weak topics or reinforce learning over time. This leads to knowledge decay and gaps in retention. Research shows that spaced repetition significantly improves long-term retention compared to one-time learning.

The platform needs a way for students to:
1. Review previously completed exercises to reinforce understanding
2. Receive intelligent recommendations for what to review based on performance and time elapsed
3. Track improvement over multiple attempts at the same content

## What Changes

- **Review Mode**: Allow students to retry any completed exercise or chapter section
  - Add "Review" button to completed chapters in chapter list
  - Add "Retry Exercise" option in exercise completion screen
  - Track multiple attempts with timestamps and scores
  - Display score trends across attempts (improvement tracking)

- **Spaced Repetition System**: Intelligent review scheduling based on performance
  - Calculate review intervals using modified SM-2 algorithm (Supermemo)
  - Priority queue of topics due for review based on:
    - Time since last attempt (longer = higher priority)
    - Performance score (lower scores = sooner reviews)
    - Importance weighting (foundational topics prioritized)
  - "Review Queue" dashboard widget showing recommended reviews
  - Notifications for overdue reviews (optional, respects user settings)

- **Progress Tracking Enhancements**:
  - Extend `Progress` interface to track multiple attempts per exercise
  - Add retention score calculation (weighted average across attempts)
  - Add review schedule metadata (next review date, interval multiplier)
  - Track total review sessions and time spent reviewing

## Impact

**Affected Specs**:
- `learning-progress` (NEW) - Progress tracking and persistence
- `exercise-system` (NEW) - Exercise rendering and scoring
- `review-queue` (NEW) - Spaced repetition scheduling
- `user-dashboard` (MODIFIED) - Dashboard will show review recommendations

**Affected Code**:
- `src/lib/store.ts` - Extend `Progress` interface, add review scheduling state
- `src/pages/ChapterView.tsx` - Add review mode toggle
- `src/pages/Dashboard.tsx` - Add review queue widget
- `src/components/exercises/exercise-player.tsx` - Track multiple attempts
- `src/pages/SubjectDetail.tsx` - Add review indicators to chapter cards
- New files:
  - `src/lib/spaced-repetition.ts` - SM-2 algorithm implementation
  - `src/components/cards/ReviewQueueCard.tsx` - Dashboard widget
  - `src/pages/ReviewMode.tsx` - Dedicated review interface (optional)

**Breaking Changes**: None (purely additive)

**Migration Required**: Existing progress data will be migrated to new format on first load (backward compatible)
