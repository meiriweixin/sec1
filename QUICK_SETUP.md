# 🚀 Quick Google OAuth Setup (5 Minutes)

## The Error You're Seeing

If you see "Error 400 (Bad Request)" when clicking "Continue with Google", it means the Google Client ID hasn't been configured yet. Follow these steps to fix it!

## ✅ Step-by-Step Setup

### 1️⃣ Go to Google Cloud Console
🔗 **https://console.cloud.google.com/**
- Sign in with your Google account

### 2️⃣ Create a New Project
1. Click the **project dropdown** (top left, next to "Google Cloud")
2. Click **"NEW PROJECT"**
3. Enter name: `SG-Learning`
4. Click **"CREATE"**
5. Wait for project creation (10-20 seconds)

### 3️⃣ Enable Google APIs
1. Click the **☰ menu** (top left)
2. Go to **"APIs & Services"** → **"Library"**
3. Search for: `Google People API`
4. Click on it → Click **"ENABLE"**

### 4️⃣ Configure OAuth Consent Screen
1. Go to **"APIs & Services"** → **"OAuth consent screen"**
2. Select **"External"** → Click **"CREATE"**
3. Fill in:
   - **App name**: `SG Learning`
   - **User support email**: (select your email from dropdown)
   - **Developer contact**: (type your email)
4. Click **"SAVE AND CONTINUE"**
5. Click **"ADD OR REMOVE SCOPES"**
6. Filter for `userinfo` and select:
   - ✅ `openid`
   - ✅ `userinfo.email`
   - ✅ `userinfo.profile`
7. Click **"UPDATE"** → **"SAVE AND CONTINUE"**
8. Click **"ADD USERS"**
9. Add your Gmail address
10. Click **"ADD"** → **"SAVE AND CONTINUE"**
11. Click **"BACK TO DASHBOARD"**

### 5️⃣ Create OAuth Client ID (MOST IMPORTANT!)
1. Go to **"APIs & Services"** → **"Credentials"**
2. Click **"+ CREATE CREDENTIALS"** → **"OAuth client ID"**
3. Select: **"Web application"**
4. Fill in:
   - **Name**: `SG Learning Web`
   - Under **"Authorized JavaScript origins"**:
     - Click **"+ ADD URI"**
     - Enter: `http://localhost:8080`
     - Click **"+ ADD URI"** again
     - Enter: `http://localhost:5173`
5. Click **"CREATE"**
6. 🎉 A popup shows your credentials!
   - **Copy the Client ID** (looks like: `123456789-abc.apps.googleusercontent.com`)
   - You can ignore the Client Secret

### 6️⃣ Update Your .env File
1. Open the `.env` file in your project root folder
2. Replace this line:
   ```
   VITE_GOOGLE_CLIENT_ID=YOUR_GOOGLE_CLIENT_ID_HERE
   ```

   With (paste your actual Client ID):
   ```
   VITE_GOOGLE_CLIENT_ID=123456789-abc.apps.googleusercontent.com
   ```

3. **Save the file**

### 7️⃣ Restart Development Server
```bash
# Stop the current server (Ctrl+C in the terminal)
# Then start it again:
npm run dev
```

### 8️⃣ Test Google Sign-In
1. Go to: http://localhost:8080/login
2. Click **"Continue with Google"**
3. Select your Google account
4. Click **"Allow"** to grant permissions
5. 🎉 You're signed in!

---

## 🔍 Troubleshooting

### "Error 400 (Bad Request)"
- ✅ Make sure you updated the `.env` file with your actual Client ID
- ✅ Make sure you restarted the dev server after changing `.env`
- ✅ Check that Client ID doesn't have spaces or quotes

### "Access blocked: This app's request is invalid"
- ✅ Make sure you added `http://localhost:8080` to Authorized JavaScript origins
- ✅ Check spelling - it must be exactly `http://localhost:8080` (no trailing slash)

### "This app is blocked"
- ✅ Make sure OAuth consent screen is configured
- ✅ Add your email as a test user
- ✅ Your app is in "Testing" mode - that's OK for development

### Button doesn't do anything
- ✅ Open browser console (F12) to see error messages
- ✅ Check that `.env` file exists and has the right format
- ✅ Make sure you restarted the dev server

---

## 📸 Visual Checklist

After setup, you should have:

✅ A Google Cloud project named "SG Learning"
✅ Google People API enabled
✅ OAuth consent screen configured (External, Testing mode)
✅ Your email added as a test user
✅ OAuth Client ID created (Web application type)
✅ `http://localhost:8080` in Authorized JavaScript origins
✅ Client ID copied to `.env` file
✅ Dev server restarted

---

## 🎯 What Happens When You Click "Continue with Google"

```
1. You click button
   ↓
2. Google login popup opens
   ↓
3. You select your Google account
   ↓
4. You grant permissions (email, profile)
   ↓
5. Google sends back your info
   ↓
6. App logs you in automatically
   ↓
7. Redirects to dashboard
```

---

## 💡 Pro Tips

- **Save your Client ID**: You can find it anytime in Google Cloud Console → Credentials
- **Testing mode**: Your app stays in "Testing" mode - perfect for development
- **Multiple users**: Add more test users in OAuth consent screen if needed
- **Production**: When ready to deploy, follow [GOOGLE_AUTH_SETUP.md](GOOGLE_AUTH_SETUP.md) for production setup

---

## ⏱️ Time Estimate

- Google Cloud setup: **3 minutes**
- Updating .env file: **30 seconds**
- Restarting server: **30 seconds**
- Testing: **1 minute**
- **Total: ~5 minutes**

---

## 🆘 Need Help?

1. Check the browser console (F12) for error messages
2. Read [GOOGLE_AUTH_SETUP.md](GOOGLE_AUTH_SETUP.md) for detailed instructions
3. Make sure all steps above are completed in order

---

## ✨ After Setup

Once configured, you can:
- ✅ Sign in with your real Gmail account
- ✅ See your Google profile name and picture
- ✅ Your progress is automatically saved
- ✅ One-click sign-in on future visits

Enjoy using SG Learning with Google Sign-In! 🎉
