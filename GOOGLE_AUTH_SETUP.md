# Google Authentication Setup Guide

This guide will help you set up Google OAuth authentication for SG Learning.

## Prerequisites

- A Google account
- Access to [Google Cloud Console](https://console.cloud.google.com/)

## Step-by-Step Setup

### 1. Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click on the project dropdown at the top of the page
3. Click "New Project"
4. Enter a project name (e.g., "SG Learning")
5. Click "Create"

### 2. Enable Google+ API

1. In your Google Cloud Console, go to "APIs & Services" > "Library"
2. Search for "Google+ API" or "People API"
3. Click on it and press "Enable"

### 3. Configure OAuth Consent Screen

1. Go to "APIs & Services" > "OAuth consent screen"
2. Select "External" user type (unless you have a Google Workspace account)
3. Click "Create"
4. Fill in the required information:
   - **App name**: SG Learning
   - **User support email**: Your email address
   - **Developer contact information**: Your email address
5. Click "Save and Continue"
6. On the "Scopes" page, click "Add or Remove Scopes"
7. Add these scopes:
   - `userinfo.email`
   - `userinfo.profile`
   - `openid`
8. Click "Save and Continue"
9. Add test users (your email and any other testers)
10. Click "Save and Continue"

### 4. Create OAuth 2.0 Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth client ID"
3. Select "Web application" as the application type
4. Configure the following:
   - **Name**: SG Learning Web Client
   - **Authorized JavaScript origins**:
     - `http://localhost:8080` (for local development)
     - `http://localhost:5173` (Vite default)
     - Your production domain (e.g., `https://yourdomain.com`)
   - **Authorized redirect URIs**:
     - `http://localhost:8080`
     - `http://localhost:5173`
     - Your production domain
5. Click "Create"
6. Copy the "Client ID" (you'll need this in the next step)

### 5. Configure Environment Variables

1. Create a `.env` file in the root of your project (if it doesn't exist)
2. Add your Google Client ID:

```env
VITE_GOOGLE_CLIENT_ID=your-actual-client-id-here.apps.googleusercontent.com
```

3. Replace `your-actual-client-id-here` with the Client ID you copied from Google Cloud Console

**Important**: Never commit your actual Client ID to version control if it's a production secret. The `.env` file is already in `.gitignore`.

### 6. Test the Integration

1. Start the development server:
   ```bash
   npm run dev
   ```

2. Navigate to the login page (`http://localhost:8080/login`)

3. Click the "Continue with Google" button

4. You should be redirected to Google's OAuth consent screen

5. Select your Google account and grant permissions

6. You'll be redirected back to the app and logged in with your Google account

## Production Deployment

### Lovable / Hosted Deployment

If deploying to Lovable or another hosting platform:

1. Add your production domain to the "Authorized JavaScript origins" in Google Cloud Console
2. Set the `VITE_GOOGLE_CLIENT_ID` environment variable in your hosting platform's settings
3. Redeploy the application

### Important Security Notes

- **Client ID is public**: The Google Client ID is safe to expose in client-side code
- **No Client Secret needed**: For client-side OAuth (implicit flow), you don't need a client secret
- **Scope limitations**: Only request the minimum scopes needed (email, profile)
- **Domain restrictions**: Always restrict authorized origins to your actual domains

## Troubleshooting

### "Redirect URI mismatch" error

- Ensure your authorized redirect URIs in Google Cloud Console match your application's URL exactly
- Check that you've added both development and production URLs

### "Access blocked" error

- Your OAuth consent screen might still be in testing mode
- Add your email as a test user in the OAuth consent screen settings
- For public access, you'll need to submit your app for verification

### "Invalid client" error

- Double-check that your Client ID is correct in the `.env` file
- Ensure you're using `VITE_` prefix (required for Vite environment variables)
- Restart the development server after changing `.env`

### Google button doesn't appear

- Check browser console for errors
- Verify that `VITE_GOOGLE_CLIENT_ID` is set
- Make sure the GoogleOAuthProvider is wrapping your app

## Features

Once authenticated with Google, users get:

- ✅ Their real name and email from Google account
- ✅ Profile picture from Google account
- ✅ Persistent login (stored in localStorage)
- ✅ Same learning progress tracking as other login methods
- ✅ Automatic account creation on first sign-in

## User Data

The app requests and stores:

- **Email address**: Used for user identification
- **Name**: Displayed in the app
- **Profile picture URL**: Shown in user profile (optional)
- **Google User ID**: Used as unique identifier (prefixed with `google_`)

All user data is stored locally in the browser's localStorage. No data is sent to external servers.

## Additional Resources

- [Google Identity Services Documentation](https://developers.google.com/identity/gsi/web/guides/overview)
- [@react-oauth/google Documentation](https://www.npmjs.com/package/@react-oauth/google)
- [OAuth 2.0 for Client-side Applications](https://developers.google.com/identity/protocols/oauth2/javascript-implicit-flow)
