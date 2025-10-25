# Fixing Google OAuth Public Access

## Issue
When students try to log in with their own Gmail accounts, they see:
> "Social Account is not yet connected to any Vercel user. Sign up?"

This happens because your Google OAuth app is in **Testing mode** and only allows specific test users.

## Solution: Make OAuth App Available to All Users

### Option 1: Add Test Users (Quick Fix)

If you want to keep the app in Testing mode but allow specific students:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project
3. Navigate to **APIs & Services** → **OAuth consent screen**
4. Scroll down to **Test users** section
5. Click **+ ADD USERS**
6. Add student email addresses (one per line):
   ```
   student1@gmail.com
   student2@gmail.com
   student3@gmail.com
   ```
7. Click **SAVE**

**Note:** You can add up to 100 test users in Testing mode.

---

### Option 2: Publish the App (Recommended for Production)

To allow **ANY** Gmail account to sign in:

#### Step 1: Complete OAuth Consent Screen

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project
3. Navigate to **APIs & Services** → **OAuth consent screen**

#### Step 2: Fill Required Information

Make sure you have completed:

- ✅ **App name**: SG Learning (or your app name)
- ✅ **User support email**: Your email address
- ✅ **App logo**: (Optional but recommended)
- ✅ **Application home page**: http://localhost:8081 (or your domain)
- ✅ **Application privacy policy link**: (Optional for internal apps)
- ✅ **Application terms of service link**: (Optional for internal apps)
- ✅ **Authorized domains**:
  - Add `localhost` if testing locally
  - Add your production domain when deploying
- ✅ **Developer contact information**: Your email address

#### Step 3: Configure Scopes (Already Done)

Your current scopes are fine:
- `userinfo.email`
- `userinfo.profile`
- `openid`

#### Step 4: Publish the App

1. Click **PUBLISH APP** button
2. Review the warning message
3. Click **CONFIRM**

**Important Notes:**
- For apps that only use basic scopes (email, profile), you **do NOT need Google verification**
- The app will be available immediately to all Google accounts
- If you add sensitive scopes later, you'll need verification

---

### Option 3: Use Internal User Type (For Google Workspace Only)

If all your students use the same Google Workspace domain (e.g., @school.edu.sg):

1. Go to **OAuth consent screen**
2. Change **User Type** to **Internal**
3. This automatically allows all users in your Google Workspace organization
4. No verification needed

**Note:** This only works if you have a Google Workspace organization.

---

## Current Configuration

Your OAuth Client ID:
```
1070955723701-8ml4c30lm1g2uf87a4jbcobmncrekvj1.apps.googleusercontent.com
```

Authorized JavaScript origins:
- http://localhost:8080
- http://localhost:8081
- (Add your production domain when deploying)

Authorized redirect URIs:
- http://localhost:8080
- http://localhost:8081
- (Add your production domain when deploying)

---

## Quick Verification

After making changes, test with a different Gmail account:

1. Open the app in an **incognito/private window**
2. Click **Continue with Google**
3. Try logging in with a Gmail account that's NOT in the test users list
4. You should now be able to sign in successfully

---

## What Changed?

### Before (Testing Mode)
- ❌ Only you and test users can sign in
- ❌ Students see "Social Account is not yet connected" error
- ✅ Quick to set up

### After (Published)
- ✅ **Any Gmail account** can sign in
- ✅ Students can use their own Gmail accounts
- ✅ No verification needed (for basic scopes)
- ✅ Ready for production

---

## Troubleshooting

### Still seeing the error?

1. **Clear browser cache and cookies**
2. **Try in incognito mode**
3. **Wait 5-10 minutes** for Google's changes to propagate
4. **Verify app is published**: Check OAuth consent screen shows "In production" status

### Need to revert to Testing?

1. Go to **OAuth consent screen**
2. Click **BACK TO TESTING**
3. App will only allow test users again

---

## Production Deployment Checklist

When deploying to production (e.g., Vercel, Netlify):

- [ ] Add production domain to **Authorized JavaScript origins**
- [ ] Add production domain to **Authorized redirect URIs**
- [ ] Update `.env.production` with the same Client ID
- [ ] Ensure OAuth app is **Published** (not Testing)
- [ ] Test with multiple Gmail accounts
- [ ] Monitor Google Cloud Console for any warnings

---

## Security Notes

✅ **Safe to publish** because:
- We only request basic user info (email, name, profile picture)
- No sensitive scopes (Gmail, Drive, Calendar, etc.)
- No verification required from Google
- Users can revoke access anytime at https://myaccount.google.com/permissions

🔒 **Best practices**:
- Never commit `.env` file to Git (already in `.gitignore`)
- Keep Client ID public-safe (it's not a secret)
- Keep Client Secret secure (not used in frontend apps)
- Use HTTPS in production
- Add your production domain to authorized origins

---

## Need Help?

If you encounter issues:

1. Check [Google OAuth Documentation](https://developers.google.com/identity/protocols/oauth2)
2. Review [Console Cloud Error Messages](https://console.cloud.google.com/)
3. Verify all settings in OAuth consent screen
4. Test in incognito mode to avoid cache issues

---

**Quick Links:**
- [Google Cloud Console](https://console.cloud.google.com/)
- [OAuth Consent Screen](https://console.cloud.google.com/apis/credentials/consent)
- [Credentials](https://console.cloud.google.com/apis/credentials)
