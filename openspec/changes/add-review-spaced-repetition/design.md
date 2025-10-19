# Design: Review Mode and Spaced Repetition

## Context

The current system tracks learning progress as a linear journey: students complete sections and exercises once, and progress is stored as boolean completion flags. This doesn't support revisiting content or tracking retention over time.

We need a solution that:
- Allows multiple attempts at the same exercise/section
- Schedules optimal review times based on learning science
- Integrates seamlessly with existing Zustand state management
- Works offline (leverages localStorage persistence)
- Remains performant with growing attempt history

**Stakeholders**: Secondary 1 students (primary users), parents/teachers (progress monitors)

## Goals / Non-Goals

**Goals**:
- Enable students to retry any completed exercise in Review Mode
- Implement spaced repetition scheduling using proven algorithm (SM-2)
- Visualize progress trends across multiple attempts
- Provide actionable review recommendations in dashboard
- Maintain backward compatibility with existing progress data

**Non-Goals**:
- Social features (peer comparison, sharing reviews)
- Cross-device sync (remains local-only for MVP)
- Advanced analytics (detailed retention curves, predictive models)
- Customizable scheduling algorithms (SM-2 only for MVP)
- Mandatory reviews (all review prompts are optional)

## Decisions

### 1. Spaced Repetition Algorithm: Modified SM-2

**Decision**: Use SuperMemo 2 (SM-2) algorithm with adjustments for educational context

**Why SM-2**:
- Well-researched (proven effective since 1988)
- Simple to implement (5 parameters, straightforward calculation)
- Doesn't require machine learning or large datasets
- Works well for mixed content types (MCQ, short answer, etc.)

**Algorithm Overview**:
```
Initial interval: 1 day
Next interval: 6 days
Subsequent intervals: I(n) = I(n-1) × EF

EF (Easiness Factor) calculation:
- Based on performance score (0-100%)
- EF = 1.3 + (score/100 × 1.7)  [range: 1.3 to 3.0]
- Score ≥80%: Easy (longer interval)
- Score 60-79%: Medium (moderate interval)
- Score <60%: Hard (shorter interval, restart progression)
```

**Adjustments for SG Learning**:
- Cap maximum interval at 30 days (students need regular practice)
- Minimum interval: 1 day (prevent same-day spam)
- Weight by chapter importance (foundational topics reviewed more frequently)

**Alternatives Considered**:
- **Leitner System**: Too rigid (fixed boxes), doesn't adapt to individual performance
- **Anki Algorithm (SM-2 variant)**: More complex, requires user input on difficulty rating
- **Custom ML-based**: Overkill for MVP, requires training data

### 2. Data Model: Attempt History vs. Aggregated Scores

**Decision**: Store full attempt history with timestamps, aggregate on-demand

**Structure**:
```typescript
interface ExerciseAttempt {
  exerciseId: string;
  attemptedAt: string; // ISO 8601
  score: number; // 0-100
  timeSpent: number; // seconds
  isReview: boolean; // true if attempted in review mode
}

interface Progress {
  // ... existing fields
  attempts: ExerciseAttempt[]; // Full history
  reviewSchedule: {
    nextReviewDate: string; // ISO 8601
    intervalDays: number;
    easinessFactor: number; // 1.3 - 3.0
  };
}
```

**Why Full History**:
- Enables rich analytics (score trends, improvement rate)
- Supports future features (progress export, detailed reports)
- localStorage has sufficient capacity (estimated 100KB per user for 1 year)

**Alternatives Considered**:
- **Aggregated only**: Simpler, but loses ability to show trends
- **Server-side storage**: Better scalability, but breaks offline-first principle

### 3. Review Mode UI: In-Place vs. Dedicated Page

**Decision**: Hybrid approach - review mode toggle in ChapterView, dedicated ReviewQueue page

**Why Hybrid**:
- In-place review: Natural workflow, students can review immediately after learning
- Dedicated page: Centralized queue, better for spaced repetition discipline
- Flexibility: Students choose review style (immediate vs. scheduled)

**Implementation**:
- Add `?mode=review` query parameter to existing ChapterView route
- Create `/review` route with prioritized queue
- Review mode disables progress updates (doesn't affect "completed" status)
- Show "Review Mode" badge in header when active

**Alternatives Considered**:
- **In-place only**: Misses opportunity for structured review sessions
- **Dedicated only**: Forces context switch, less convenient for immediate retry

### 4. Review Scheduling: Push vs. Pull

**Decision**: Pull-based system (dashboard widget + indicators), no push notifications

**Why Pull**:
- Respects user autonomy (no intrusive notifications)
- Simpler implementation (no notification permission flow)
- Aligns with self-paced learning philosophy
- Reduces cognitive load (students check when ready)

**Implementation**:
- Dashboard: "Review Queue" card showing top 5 due items
- Chapter cards: Badge showing "Due for Review" count
- Subject detail: Summary of total reviews due

**Alternatives Considered**:
- **Push notifications**: More engaging, but risks annoyance and requires permission
- **Email reminders**: Requires email integration, out of scope for MVP

## Risks / Trade-offs

### Risk 1: Storage Bloat from Attempt History
**Impact**: localStorage has 5-10MB limit, full attempt history could exceed this for power users

**Mitigation**:
- Implement rolling window (keep last 50 attempts per exercise)
- Compress old attempts into aggregated stats after 90 days
- Monitor usage, add warning if approaching 80% capacity

### Risk 2: SM-2 Algorithm May Not Fit All Learning Styles
**Impact**: Some students may need more/fewer reviews than algorithm suggests

**Mitigation**:
- Make all review suggestions optional (never block progress)
- Allow manual review of any content anytime
- Track user behavior, adjust algorithm in future iterations

### Risk 3: Review Fatigue (Too Many Due Reviews)
**Impact**: Large review queue could overwhelm students, reduce engagement

**Mitigation**:
- Cap dashboard queue at 5 items (prioritize by urgency × importance)
- Show "You're all caught up!" when queue is empty (positive reinforcement)
- Allow "Snooze" option to defer reviews by 1 day

### Risk 4: Confusion Between "Completed" and "Mastered"
**Impact**: Students may think completing an exercise means they don't need to review

**Mitigation**:
- Clear UI labeling: "Completed" vs. "Due for Review"
- Educate with tooltip: "Regular review helps long-term retention"
- Show retention score separately from completion status

## Migration Plan

### Phase 1: Data Model Update (Non-Breaking)
1. Add new fields to `Progress` interface with default values
2. Implement migration function in store initialization:
   ```typescript
   const migrateProgress = (old: Progress): Progress => ({
     ...old,
     attempts: old.exercisesCompleted.map(id => ({
       exerciseId: id,
       attemptedAt: old.lastAccessed,
       score: old.exerciseScores[id] || 0,
       timeSpent: 0,
       isReview: false
     })),
     reviewSchedule: calculateInitialSchedule(old)
   });
   ```
3. Run migration on first load, set flag to prevent re-run

### Phase 2: Feature Rollout
1. Deploy Review Mode first (no scheduling, manual retry only)
2. Monitor usage for 1 week
3. Enable spaced repetition scheduling
4. Iterate based on feedback

### Rollback Strategy
- Migration is backward compatible (doesn't remove old fields)
- Feature flag in store: `enableReviewMode` (default: true)
- Can disable via localStorage: `localStorage.setItem('feature:review-mode', 'false')`

## Open Questions

1. **Should review attempts count toward exercise completion percentage?**
   - Leaning toward: No (completion = first successful attempt, reviews are separate)
   - Need to validate with user testing

2. **What constitutes a "successful" first attempt for completion?**
   - Current behavior: Any attempt completes the exercise
   - Proposal: Require ≥60% score for completion, otherwise mark as "attempted but incomplete"
   - Needs discussion with educators

3. **Should spaced repetition apply to sections (content) or only exercises?**
   - MVP: Exercises only (easier to quantify performance)
   - Future: Could add "Reread Section" for low-scoring exercise topics

4. **How to handle drag-order and matching exercises in review mode?**
   - These need fresh randomization each attempt
   - Should we randomize order, or keep same questions? (Leaning toward randomize)

## Performance Considerations

**Expected Load**:
- Average student: 4 subjects × 10 chapters × 12 exercises = 480 total exercises
- If reviewed 3 times each over 1 year = 1,440 attempts
- Storage: ~30 bytes/attempt × 1,440 = ~43KB (well within limits)

**Optimization Strategies**:
- Lazy load attempt history (only fetch for current chapter)
- Debounce review schedule recalculations (batch updates)
- Index exercises by `nextReviewDate` for O(1) queue retrieval
