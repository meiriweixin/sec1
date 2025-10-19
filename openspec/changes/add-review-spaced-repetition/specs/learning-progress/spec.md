# Learning Progress Tracking

## ADDED Requirements

### Requirement: Exercise Attempt History
The system SHALL track all attempts at each exercise, including score, timestamp, time spent, and whether the attempt was in review mode.

#### Scenario: First attempt at exercise
- **WHEN** a student completes an exercise for the first time
- **THEN** an attempt record is created with `isReview: false`
- **AND** the attempt includes `attemptedAt` (ISO 8601 timestamp), `score` (0-100), and `timeSpent` (seconds)

#### Scenario: Review attempt at exercise
- **WHEN** a student retries a previously completed exercise in review mode
- **THEN** a new attempt record is created with `isReview: true`
- **AND** the new attempt does not overwrite previous attempt history
- **AND** the completion status remains "completed" (review attempts don't affect completion)

#### Scenario: Viewing attempt history
- **WHEN** a student views their progress for a specific exercise
- **THEN** all attempts are displayed in chronological order (newest first)
- **AND** each attempt shows score, date, and time spent
- **AND** review attempts are visually distinguished from initial attempts

### Requirement: Review Schedule Metadata
The system SHALL calculate and store review schedule metadata for each completed chapter using the SM-2 spaced repetition algorithm.

#### Scenario: First completion of chapter
- **WHEN** a student completes all exercises in a chapter for the first time
- **THEN** a review schedule is initialized with `nextReviewDate` set to 1 day from completion
- **AND** `intervalDays` is set to 1
- **AND** `easinessFactor` is calculated based on average exercise scores (range 1.3 to 3.0)

#### Scenario: Successful review session
- **WHEN** a student completes a review session with average score ≥60%
- **THEN** `nextReviewDate` is updated to current date plus `intervalDays × easinessFactor`
- **AND** `intervalDays` is multiplied by `easinessFactor`
- **AND** `easinessFactor` is adjusted based on performance (higher score = higher EF, max 3.0)

#### Scenario: Failed review session
- **WHEN** a student completes a review session with average score <60%
- **THEN** `nextReviewDate` is reset to 1 day from current date
- **AND** `intervalDays` is reset to 1
- **AND** `easinessFactor` is decreased by 0.2 (minimum 1.3)

#### Scenario: Maximum interval cap
- **WHEN** calculated next review interval exceeds 30 days
- **THEN** `intervalDays` is capped at 30
- **AND** `nextReviewDate` is set to current date plus 30 days

### Requirement: Retention Score Calculation
The system SHALL calculate a retention score for each chapter based on weighted average of recent attempts.

#### Scenario: Calculate retention score with multiple attempts
- **WHEN** a chapter has multiple exercise attempts across review sessions
- **THEN** retention score is calculated as weighted average: `(mostRecentScore × 0.5) + (previousScore × 0.3) + (olderScore × 0.2)`
- **AND** retention score is displayed as percentage (0-100%)
- **AND** retention score is updated after each review session

#### Scenario: Calculate retention score with single attempt
- **WHEN** a chapter has only been completed once (no reviews yet)
- **THEN** retention score equals the initial average exercise score
- **AND** a tooltip indicates "Complete a review to see retention trend"

### Requirement: Progress Data Migration
The system SHALL migrate existing progress data to new format on first load without data loss.

#### Scenario: Migrating legacy progress data
- **WHEN** the application loads for the first time after the review feature is deployed
- **THEN** existing `exercisesCompleted` array is converted to `attempts` array
- **AND** each completed exercise gets an attempt record with `attemptedAt` set to `lastAccessed` date
- **AND** scores from `exerciseScores` map are preserved in attempt records
- **AND** `timeSpent` defaults to 0 for migrated attempts
- **AND** a migration flag is set to prevent re-running migration

#### Scenario: Backward compatibility check
- **WHEN** migrated progress data is loaded
- **THEN** existing completion status, scores, and timestamps remain unchanged
- **AND** all legacy features (chapter progress ring, dashboard stats) continue to work
- **AND** no data is removed from the old format (only new fields are added)
