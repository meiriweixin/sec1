import { supabase, SglearnUser } from './supabase';

/**
 * Fetches all users from the database
 * Admin-only function
 * @returns Array of all users or null on error
 */
export async function fetchAllUsers(): Promise<SglearnUser[] | null> {
  try {
    const { data, error } = await supabase
      .from('sglearn_users')
      .select('*')
      .order('created_at', { ascending: false });

    if (error) {
      console.error('Error fetching users:', error);
      return null;
    }

    return data as SglearnUser[];
  } catch (error) {
    console.error('Error fetching users:', error);
    return null;
  }
}

/**
 * Adds a new user to the whitelist
 * Admin-only function
 * @param email - User's email address
 * @param name - User's display name
 * @param isAdmin - Whether user should have admin privileges
 * @returns Created user or null on error
 */
export async function addUser(
  email: string,
  name: string,
  isAdmin: boolean = false
): Promise<SglearnUser | null> {
  try {
    // Check if user already exists
    const { data: existing } = await supabase
      .from('sglearn_users')
      .select('email')
      .eq('email', email)
      .limit(1);

    if (existing && existing.length > 0) {
      throw new Error('User with this email already exists');
    }

    // Insert new user
    const { data, error } = await supabase
      .from('sglearn_users')
      .insert([
        {
          email,
          name,
          is_admin: isAdmin,
          is_active: true
        }
      ])
      .select()
      .single();

    if (error) {
      console.error('Error adding user:', error);
      console.error('Error details:', JSON.stringify(error, null, 2));
      throw new Error(error.message || 'Failed to add user to database');
    }

    return data as SglearnUser;
  } catch (error) {
    console.error('Error adding user:', error);
    throw error;
  }
}

/**
 * Deletes a user from the database
 * Admin-only function
 * Prevents deleting the last admin user
 * @param userId - User's Supabase UUID
 * @returns true on success, false on error
 */
export async function deleteUser(userId: string): Promise<boolean> {
  try {
    // Check if user is admin
    const { data: user } = await supabase
      .from('sglearn_users')
      .select('is_admin')
      .eq('id', userId)
      .single();

    if (user?.is_admin) {
      // Count total admins
      const { count } = await supabase
        .from('sglearn_users')
        .select('*', { count: 'exact', head: true })
        .eq('is_admin', true);

      if (count && count <= 1) {
        throw new Error('Cannot delete the last admin user');
      }
    }

    // Delete user
    const { error } = await supabase
      .from('sglearn_users')
      .delete()
      .eq('id', userId);

    if (error) {
      console.error('Error deleting user:', error);
      return false;
    }

    return true;
  } catch (error) {
    console.error('Error deleting user:', error);
    throw error;
  }
}

/**
 * Toggles user's active status
 * Admin-only function
 * @param userId - User's Supabase UUID
 * @param isActive - New active status
 * @returns true on success, false on error
 */
export async function toggleUserStatus(
  userId: string,
  isActive: boolean
): Promise<boolean> {
  try {
    const { error } = await supabase
      .from('sglearn_users')
      .update({ is_active: isActive })
      .eq('id', userId);

    if (error) {
      console.error('Error toggling user status:', error);
      return false;
    }

    return true;
  } catch (error) {
    console.error('Error toggling user status:', error);
    return false;
  }
}
