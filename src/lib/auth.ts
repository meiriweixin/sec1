import { supabase, SglearnUser } from './supabase';

/**
 * Validates Google OAuth login against whitelist
 * @param googleSub - Google user's unique identifier
 * @param email - User's email address
 * @param name - User's display name
 * @param photoUrl - User's profile photo URL
 * @returns User data if valid, null otherwise
 */
export async function validateGoogleLogin(
  googleSub: string,
  email: string,
  name: string,
  photoUrl?: string
): Promise<SglearnUser | null> {
  try {
    // Check if user exists in whitelist by email
    const { data: users, error } = await supabase
      .from('sglearn_users')
      .select('*')
      .eq('email', email)
      .limit(1);

    if (error) {
      console.error('Error checking user whitelist:', error);
      return null;
    }

    if (!users || users.length === 0) {
      console.log('User not in whitelist:', email);
      return null;
    }

    const user = users[0] as SglearnUser;

    // Check if user is active
    if (!user.is_active) {
      console.log('User is inactive:', email);
      return null;
    }

    // Update google_sub if not set (first Google login)
    if (!user.google_sub) {
      const { error: updateError } = await supabase
        .from('sglearn_users')
        .update({ google_sub: googleSub })
        .eq('id', user.id);

      if (updateError) {
        console.error('Error updating google_sub:', updateError);
      }
    }

    // Update last login time and photo URL
    const { error: loginError } = await supabase
      .from('sglearn_users')
      .update({
        last_login_at: new Date().toISOString(),
        photo_url: photoUrl || user.photo_url
      })
      .eq('id', user.id);

    if (loginError) {
      console.error('Error updating last login:', loginError);
    }

    return user;
  } catch (error) {
    console.error('Error validating Google login:', error);
    return null;
  }
}

/**
 * Checks if user has admin privileges
 * @param userId - User's Supabase UUID
 * @returns true if user is admin, false otherwise
 */
export async function isUserAdmin(userId: string): Promise<boolean> {
  try {
    const { data, error } = await supabase
      .from('sglearn_users')
      .select('is_admin')
      .eq('id', userId)
      .single();

    if (error) {
      console.error('Error checking admin status:', error);
      return false;
    }

    return data?.is_admin || false;
  } catch (error) {
    console.error('Error checking admin status:', error);
    return false;
  }
}

/**
 * Updates user's last login timestamp
 * @param userId - User's Supabase UUID
 */
export async function updateLastLogin(userId: string): Promise<void> {
  try {
    const { error } = await supabase
      .from('sglearn_users')
      .update({ last_login_at: new Date().toISOString() })
      .eq('id', userId);

    if (error) {
      console.error('Error updating last login:', error);
    }
  } catch (error) {
    console.error('Error updating last login:', error);
  }
}
