# Review Queue

## ADDED Requirements

### Requirement: Review Queue Dashboard Widget
The system SHALL display a prioritized list of chapters due for review on the user dashboard.

#### Scenario: View review queue with due items
- **WHEN** a student views the dashboard and has chapters due for review
- **THEN** a "Review Queue" card is displayed showing up to 5 chapters
- **AND** each item shows chapter title, subject, and days since last review
- **AND** items are sorted by urgency (overdue first, then by priority score)
- **AND** a "Start Review" button is available for each item

#### Scenario: View review queue with no due items
- **WHEN** a student views the dashboard and has no chapters due for review
- **THEN** the "Review Queue" card displays "You're all caught up!"
- **AND** a motivational message encourages continued learning
- **AND** the card shows next upcoming review date (if any)

#### Scenario: Click to start review from queue
- **WHEN** a student clicks "Start Review" on a queued chapter
- **THEN** the chapter opens in review mode (`?mode=review`)
- **AND** the review session begins with the first exercise
- **AND** progress is tracked as a review session

### Requirement: Review Priority Calculation
The system SHALL calculate review priority based on time overdue, performance history, and chapter importance.

#### Scenario: Calculate priority for overdue chapter
- **WHEN** a chapter's `nextReviewDate` is in the past
- **THEN** priority score increases by `daysOverdue × 2`
- **AND** chapters overdue by more days appear first in queue
- **AND** maximum priority bonus from overdue is capped at 30 days

#### Scenario: Calculate priority for low-scoring chapter
- **WHEN** a chapter's most recent retention score is <70%
- **THEN** priority score increases by `(70 - retentionScore) / 2`
- **AND** lower scores result in higher priority
- **AND** this bonus stacks with overdue bonus

#### Scenario: Calculate priority for foundational chapter
- **WHEN** a chapter is marked as foundational (e.g., chapter index < 3 in subject)
- **THEN** priority score is multiplied by 1.5
- **AND** foundational topics are reviewed more frequently
- **AND** this multiplier is applied after calculating base priority

#### Scenario: Cap review queue at top 5 items
- **WHEN** more than 5 chapters are due for review
- **THEN** only the top 5 highest-priority chapters are displayed
- **AND** a message indicates "5 more chapters available for review"
- **AND** clicking the message navigates to full review queue page

### Requirement: Review Due Indicators
The system SHALL display indicators on chapter cards showing when reviews are due.

#### Scenario: Show "Due for Review" badge on chapter card
- **WHEN** a completed chapter is due for review (today or past due)
- **THEN** a badge with text "Due for Review" is displayed on the chapter card
- **AND** the badge uses warning color (yellow/orange) if due today
- **AND** the badge uses danger color (red) if overdue by >3 days

#### Scenario: Show days until next review
- **WHEN** a completed chapter is not yet due for review
- **THEN** a subtle text displays "Next review in X days"
- **AND** the text uses muted color (gray)
- **AND** hovering shows tooltip with exact review date

#### Scenario: Show review count in subject summary
- **WHEN** a student views subject detail page
- **THEN** the subject card header shows total chapters due for review
- **AND** the count is displayed as "N chapters due for review"
- **AND** clicking the count filters to show only chapters due for review

### Requirement: Review Session Completion
The system SHALL track and summarize review session results after completion.

#### Scenario: Complete review session successfully
- **WHEN** a student completes all exercises in a review session
- **THEN** a summary screen displays overall score, time spent, and improvement vs. previous attempt
- **AND** confetti animation plays if score improved by ≥10%
- **AND** next review date is calculated and displayed
- **AND** a "Continue Reviewing" button navigates to next queued chapter

#### Scenario: Exit review session early
- **WHEN** a student exits review mode before completing all exercises
- **THEN** a confirmation dialog asks "Are you sure? Progress will be saved."
- **AND** clicking "Yes, Exit" saves completed exercise attempts
- **AND** the chapter remains in review queue with updated priority
- **AND** partial review counts toward attempt history

### Requirement: Review Scheduling Algorithm (SM-2)
The system SHALL calculate next review intervals using the SuperMemo 2 algorithm with adjustments for educational context.

#### Scenario: Calculate initial review interval
- **WHEN** a chapter is completed for the first time with average score ≥60%
- **THEN** `nextReviewDate` is set to 1 day from completion
- **AND** `intervalDays` is set to 1
- **AND** `easinessFactor` is calculated as `1.3 + (avgScore/100 × 1.7)` (range 1.3-3.0)

#### Scenario: Calculate subsequent review interval
- **WHEN** a review session is completed with average score ≥60%
- **THEN** new interval is calculated as `intervalDays × easinessFactor`
- **AND** `intervalDays` is updated to the new interval (capped at 30 days)
- **AND** `easinessFactor` is adjusted: `EF + (0.1 - (5 - quality) × (0.08 + (5 - quality) × 0.02))`
  - Where quality = `Math.floor(score/20)` (0-5 scale)

#### Scenario: Reset interval on poor performance
- **WHEN** a review session is completed with average score <60%
- **THEN** `intervalDays` is reset to 1 day
- **AND** `nextReviewDate` is set to tomorrow
- **AND** `easinessFactor` is decreased by 0.2 (minimum 1.3)

#### Scenario: Snooze review for 1 day
- **WHEN** a student clicks "Snooze" on a due review
- **THEN** `nextReviewDate` is postponed by 1 day
- **AND** the chapter is removed from today's review queue
- **AND** a toast notification confirms "Review snoozed until tomorrow"
- **AND** snooze action is tracked in analytics (future use)
