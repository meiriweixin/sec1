# Google Authentication - Quick Reference

## For Users

### How to Sign In with Google

1. Go to the login page
2. Click the "Continue with Google" button (with the colorful Google icon)
3. Select your Google account
4. Grant permissions to access your email and profile
5. You'll be automatically logged in and redirected to the dashboard

### Benefits of Google Sign-In

- **No password to remember**: Use your existing Google account
- **Faster login**: One-click authentication
- **Secure**: Powered by Google's OAuth 2.0
- **Profile sync**: Your name and photo from Google are automatically imported

## For Developers

### Quick Setup (5 minutes)

1. **Get Google Client ID**:
   - Visit [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing
   - Enable Google+ API
   - Create OAuth 2.0 credentials
   - Copy the Client ID

2. **Configure Environment**:
   ```bash
   # Create .env file
   echo "VITE_GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com" > .env
   ```

3. **Add Authorized Origins**:
   In Google Cloud Console, add:
   - `http://localhost:8080`
   - `http://localhost:5173`
   - Your production domain

4. **Start Development**:
   ```bash
   npm install
   npm run dev
   ```

### How It Works

```typescript
// 1. User clicks "Continue with Google"
<Button onClick={() => googleLogin()}>
  Continue with Google
</Button>

// 2. Google OAuth popup opens
// 3. User grants permissions
// 4. App receives access token
// 5. App fetches user info from Google API

const userInfo = await fetch('https://www.googleapis.com/oauth2/v3/userinfo', {
  headers: { Authorization: `Bearer ${accessToken}` }
});

// 6. User is logged in
login({
  id: "google_" + userInfo.sub,
  email: userInfo.email,
  name: userInfo.name,
  provider: 'google',
  photoURL: userInfo.picture
});
```

### Architecture

```
┌─────────────────┐
│   Login Page    │
│  (React)        │
└────────┬────────┘
         │ User clicks Google button
         ↓
┌─────────────────┐
│ Google OAuth    │
│ (Popup)         │
└────────┬────────┘
         │ User grants access
         ↓
┌─────────────────┐
│ Google API      │
│ Returns token   │
└────────┬────────┘
         │ Fetch user info
         ↓
┌─────────────────┐
│ Zustand Store   │
│ (Login user)    │
└────────┬────────┘
         │ Navigate to dashboard
         ↓
┌─────────────────┐
│   Dashboard     │
│ (Authenticated) │
└─────────────────┘
```

### Files Modified

- **src/App.tsx**: Added `GoogleOAuthProvider` wrapper
- **src/pages/Login.tsx**: Implemented `useGoogleLogin` hook
- **src/lib/store.ts**: Added `provider` and `photoURL` fields
- **src/lib/i18n.ts**: Added Google login translations
- **.env**: Added `VITE_GOOGLE_CLIENT_ID`

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `VITE_GOOGLE_CLIENT_ID` | Yes | OAuth 2.0 Client ID from Google Cloud Console |

### Dependencies Added

```json
{
  "@react-oauth/google": "^0.12.1",
  "jwt-decode": "^4.0.0"
}
```

## Testing

### Local Testing

1. Ensure `.env` has valid `VITE_GOOGLE_CLIENT_ID`
2. Run `npm run dev`
3. Navigate to `http://localhost:8080/login`
4. Click "Continue with Google"
5. Sign in with a Google account (must be added as test user if app is in testing mode)

### Production Testing

1. Deploy to production environment
2. Add production domain to Google Cloud Console authorized origins
3. Set `VITE_GOOGLE_CLIENT_ID` environment variable in hosting platform
4. Test login flow

## Security Considerations

✅ **Client ID is safe to expose** - It's designed for client-side use
✅ **HTTPS required in production** - Google OAuth requires secure connections
✅ **No client secret needed** - Using implicit flow (client-side only)
✅ **Minimal scopes** - Only requests email and profile
✅ **No server-side storage** - All data stored locally in browser

⚠️ **In production**:
- Use HTTPS
- Restrict authorized origins to your actual domains
- Consider rate limiting for API calls
- Monitor for abuse

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Button doesn't appear | Check `VITE_GOOGLE_CLIENT_ID` is set |
| "Redirect URI mismatch" | Add your URL to authorized origins |
| "Access blocked" | Add email as test user in OAuth consent screen |
| Popup blocked | Allow popups for your domain |
| "Invalid client" | Verify Client ID is correct |

## Next Steps

- [ ] Set up your own Google Cloud project
- [ ] Configure OAuth consent screen
- [ ] Add production domains to authorized origins
- [ ] Test with multiple Google accounts
- [ ] Consider adding more OAuth providers (GitHub, Microsoft, etc.)

For detailed setup instructions, see [GOOGLE_AUTH_SETUP.md](GOOGLE_AUTH_SETUP.md).
