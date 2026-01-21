-- Migration script for SG Learning User Management System
-- Run this in Supabase SQL Editor

-- 1. Create the sglearn_users table
CREATE TABLE sglearn_users (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  email TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  google_sub TEXT UNIQUE,
  is_admin BOOLEAN DEFAULT FALSE,
  is_active BOOLEAN DEFAULT TRUE,
  photo_url TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  last_login_at TIMESTAMP WITH TIME ZONE,

  CONSTRAINT email_format CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- 2. Create indexes for better query performance
CREATE INDEX idx_sglearn_users_email ON sglearn_users(email);
CREATE INDEX idx_sglearn_users_google_sub ON sglearn_users(google_sub);
CREATE INDEX idx_sglearn_users_is_active ON sglearn_users(is_active);

-- 3. Enable Row Level Security (RLS)
ALTER TABLE sglearn_users ENABLE ROW LEVEL SECURITY;

-- 4. Create RLS policy - Users can view their own data, admins can view all
CREATE POLICY "Users can view their own data"
  ON sglearn_users FOR SELECT
  USING (auth.uid()::text = id::text OR is_admin = TRUE);

-- 5. Create function to automatically update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 6. Create trigger to call the function on UPDATE
CREATE TRIGGER update_sglearn_users_updated_at
  BEFORE UPDATE ON sglearn_users
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();

-- 7. Insert the admin user (xwxnju@gmail.com)
-- Note: google_sub will be populated on first Google OAuth login
INSERT INTO sglearn_users (email, name, is_admin, is_active)
VALUES (
  'xwxnju@gmail.com',
  'Admin User',
  TRUE,
  TRUE
);

-- Verify the table was created and admin user was inserted
SELECT * FROM sglearn_users;
