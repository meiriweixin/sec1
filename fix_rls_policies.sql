-- Fix RLS Policies for Admin Operations
-- Run this in Supabase SQL Editor to enable INSERT, UPDATE, DELETE

-- Drop the existing restrictive SELECT policy
DROP POLICY IF EXISTS "Users can view their own data" ON sglearn_users;

-- Create permissive policies that allow all operations with anon key
-- Since we're controlling access in the application layer, we'll allow all operations

-- Policy 1: Allow all SELECT operations
CREATE POLICY "Enable read access for all users" ON sglearn_users
  FOR SELECT USING (true);

-- Policy 2: Allow all INSERT operations (for adding users)
CREATE POLICY "Enable insert for all users" ON sglearn_users
  FOR INSERT WITH CHECK (true);

-- Policy 3: Allow all UPDATE operations (for toggling status, updating login time, etc.)
CREATE POLICY "Enable update for all users" ON sglearn_users
  FOR UPDATE USING (true);

-- Policy 4: Allow all DELETE operations (for deleting users)
CREATE POLICY "Enable delete for all users" ON sglearn_users
  FOR DELETE USING (true);

-- Verify policies were created
SELECT schemaname, tablename, policyname, permissive, roles, cmd, qual
FROM pg_policies
WHERE tablename = 'sglearn_users';
