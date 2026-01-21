/**
 * Progress Migration Utilities
 * Handles migration of user progress from old localStorage format to Supabase UUID format
 */

/**
 * Returns the old user ID format for Google OAuth users
 * @param googleSub - Google user's unique identifier
 * @returns Old format user ID (e.g., "google_123456")
 */
export function getOldUserIdFormat(googleSub: string): string {
  return `google_${googleSub}`;
}

/**
 * Migrates user progress from old userId to new Supabase UUID
 * This is non-destructive - old data is preserved
 *
 * @param oldUserId - Old format user ID (e.g., "google_123456", "user1", or "guest")
 * @param newSupabaseId - New Supabase UUID
 */
export function migrateUserProgress(oldUserId: string, newSupabaseId: string): void {
  try {
    // Get current store state from localStorage
    const storeKey = 'sg-learning-app-storage';
    const storeData = localStorage.getItem(storeKey);

    if (!storeData) {
      console.log('No store data found, skipping migration');
      return;
    }

    const store = JSON.parse(storeData);
    const state = store.state;

    if (!state) {
      console.log('No state found in store, skipping migration');
      return;
    }

    let migrated = false;

    // Migrate allUsersProgress
    if (state.allUsersProgress && state.allUsersProgress[oldUserId]) {
      if (!state.allUsersProgress[newSupabaseId]) {
        state.allUsersProgress[newSupabaseId] = state.allUsersProgress[oldUserId];
        migrated = true;
        console.log(`Migrated progress for ${oldUserId} → ${newSupabaseId}`);
      }
    }

    // Migrate allUsersAIProgress
    if (state.allUsersAIProgress && state.allUsersAIProgress[oldUserId]) {
      if (!state.allUsersAIProgress[newSupabaseId]) {
        state.allUsersAIProgress[newSupabaseId] = state.allUsersAIProgress[oldUserId];
        migrated = true;
        console.log(`Migrated AI progress for ${oldUserId} → ${newSupabaseId}`);
      }
    }

    // Migrate allUsersExerciseVotes
    if (state.allUsersExerciseVotes && state.allUsersExerciseVotes[oldUserId]) {
      if (!state.allUsersExerciseVotes[newSupabaseId]) {
        state.allUsersExerciseVotes[newSupabaseId] = state.allUsersExerciseVotes[oldUserId];
        migrated = true;
        console.log(`Migrated exercise votes for ${oldUserId} → ${newSupabaseId}`);
      }
    }

    // Migrate allUsersWrongAnswerReviews
    if (state.allUsersWrongAnswerReviews && state.allUsersWrongAnswerReviews[oldUserId]) {
      if (!state.allUsersWrongAnswerReviews[newSupabaseId]) {
        state.allUsersWrongAnswerReviews[newSupabaseId] = state.allUsersWrongAnswerReviews[oldUserId];
        migrated = true;
        console.log(`Migrated wrong answer reviews for ${oldUserId} → ${newSupabaseId}`);
      }
    }

    // Save updated store if migration occurred
    if (migrated) {
      store.state = state;
      localStorage.setItem(storeKey, JSON.stringify(store));
      console.log('✅ Progress migration completed successfully');
    } else {
      console.log('No migration needed - data already exists for new user ID or old data not found');
    }
  } catch (error) {
    console.error('Error migrating user progress:', error);
  }
}
