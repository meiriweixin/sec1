import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL || '';
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY || '';

export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    persistSession: false,
    autoRefreshToken: false
  }
});

export interface SglearnUser {
  id: string;
  email: string;
  name: string;
  google_sub?: string | null;
  is_admin: boolean;
  is_active: boolean;
  photo_url?: string | null;
  created_at: string;
  updated_at: string;
  last_login_at?: string | null;
}
