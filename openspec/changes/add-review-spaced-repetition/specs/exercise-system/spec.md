# Exercise System

## ADDED Requirements

### Requirement: Review Mode Toggle
The system SHALL provide a review mode that allows students to retry completed exercises without affecting completion status.

#### Scenario: Enter review mode from chapter view
- **WHEN** a student clicks "Review" button on a completed chapter
- **THEN** the chapter opens in review mode (indicated by `?mode=review` query parameter)
- **AND** a "Review Mode" badge is displayed in the page header
- **AND** all exercises are available regardless of completion status

#### Scenario: Complete exercise in review mode
- **WHEN** a student completes an exercise while in review mode
- **THEN** a new attempt record is created with `isReview: true`
- **AND** the exercise score is saved to attempt history
- **AND** the chapter completion status remains unchanged
- **AND** a success message indicates "Review completed! Your progress has been tracked."

#### Scenario: Exit review mode
- **WHEN** a student clicks "Exit Review Mode" or navigates back
- **THEN** review mode is deactivated
- **AND** the student returns to normal chapter view
- **AND** all progress indicators reflect the latest review attempt

### Requirement: Retry Exercise Option
The system SHALL allow students to immediately retry any exercise after completion.

#### Scenario: Retry from exercise completion screen
- **WHEN** a student completes an exercise and views the completion screen
- **THEN** a "Retry Exercise" button is displayed alongside "Next Exercise"
- **AND** clicking "Retry Exercise" resets the exercise to initial state
- **AND** previous answers are cleared
- **AND** the timer (if applicable) is reset

#### Scenario: Retry counts as review attempt
- **WHEN** a student retries an exercise that was previously completed
- **THEN** the retry is tracked as a review attempt (`isReview: true`)
- **AND** the new score is added to attempt history
- **AND** the original completion is preserved

### Requirement: Score Trend Visualization
The system SHALL display score trends across multiple attempts to visualize improvement.

#### Scenario: View score trend for exercise with multiple attempts
- **WHEN** a student views an exercise that has been attempted multiple times
- **THEN** a line chart is displayed showing scores over time
- **AND** the X-axis shows attempt dates (formatted as "MMM DD")
- **AND** the Y-axis shows scores (0-100%)
- **AND** review attempts are marked with a different color/icon than initial attempts

#### Scenario: View score trend for exercise with single attempt
- **WHEN** a student views an exercise with only one attempt
- **THEN** a message displays "Complete this exercise again to see your progress trend"
- **AND** the single score is shown as a data point
- **AND** the chart is grayed out to indicate insufficient data

### Requirement: Exercise Randomization in Review Mode
The system SHALL randomize question order and options for certain exercise types in review mode to prevent memorization.

#### Scenario: Randomize MCQ options in review
- **WHEN** a student attempts an MCQ exercise in review mode
- **THEN** the answer choices are shuffled randomly (different from previous attempt order)
- **AND** the correct answer index is updated to match new position
- **AND** the question text remains the same

#### Scenario: Randomize drag-order items in review
- **WHEN** a student attempts a drag-order exercise in review mode
- **THEN** the initial item order is shuffled randomly
- **AND** the target correct order remains the same
- **AND** the student must drag items to match the original correct sequence

#### Scenario: No randomization for short-answer exercises
- **WHEN** a student attempts a short-answer exercise in review mode
- **THEN** the question text and expected answer remain identical
- **AND** no randomization occurs (not applicable for this exercise type)
