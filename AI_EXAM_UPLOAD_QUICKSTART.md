# AI Exam Upload - Quick Start Guide

## 🚀 Setup (5 minutes)

### 1. Get Azure OpenAI Credentials

Visit [Azure Portal](https://portal.azure.com):
1. Navigate to your Azure OpenAI resource
2. Go to "Keys and Endpoint" section
3. Copy:
   - **Key 1** (API Key)
   - **Endpoint** URL
   - **Deployment Name** (should be `gpt-4o`)

### 2. Configure Environment

Create `.env` file in project root:

```bash
# Copy from .env.example
cp .env.example .env
```

Edit `.env` and add your credentials:

```bash
VITE_AZURE_OPENAI_API_KEY=your-actual-api-key-here
VITE_AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
VITE_AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
```

### 3. Restart Dev Server

```bash
npm run dev
```

## 📝 How to Use

### Student Workflow

1. **Login** to the app
2. **Select grade level** from header dropdown (e.g., Sec 3)
3. **Navigate to a subject** (e.g., Mathematics → Sec 3)
4. **Click "Upload Exam Paper"** button (purple gradient)
5. **Choose exam image** (JPG, PNG, WEBP, or PDF < 10MB)
6. **Wait for AI processing** (~30-60 seconds):
   - Stage 1: Extracting questions from image
   - Stage 2: Generating lesson content
7. **Review generated content**:
   - Edit titles, descriptions
   - Review lesson sections (markdown)
   - Check exercises and answers
   - Modify objectives if needed
8. **Save chapter** → New chapter appears with purple "AI Generated" badge

### What AI Generates

✅ **Bilingual content** (English + Chinese)
✅ **3-4 lesson sections** with comprehensive explanations
✅ **10-15 exercises** matching exam difficulty
✅ **Singapore context** (NEWater, MRT, HDB examples)
✅ **Learning objectives** aligned with MOE syllabus
✅ **Pedagogical format** (Problem → Concept → Steps → Answer → Tips)

## 🔍 Testing

### Test with Sample Exam

1. Find or create a test exam image:
   - Screenshot of math/science exam
   - Mobile photo of textbook questions
   - Scanned exam paper (best quality)

2. Upload and verify:
   - Questions extracted correctly
   - Difficulty levels appropriate
   - Content makes sense
   - Exercises match topics

3. Check saved chapter:
   - Appears in chapter list
   - Purple "AI Generated" badge visible
   - Can be opened and completed like regular chapters
   - Progress tracked separately per user

## ⚠️ Troubleshooting

### "Azure OpenAI is not configured"

**Solution**:
- Verify `.env` file exists in project root
- Check all three variables are set
- Restart dev server: `Ctrl+C` then `npm run dev`

### Upload Fails

**Check**:
- ✅ API key is valid (not expired)
- ✅ Endpoint URL is correct (includes `https://`)
- ✅ Deployment name matches (usually `gpt-4o`)
- ✅ Image file < 10MB
- ✅ Internet connection stable

### AI Chapters Don't Appear

**Debug**:
1. Open browser console (F12)
2. Check localStorage:
   ```javascript
   localStorage.getItem('sg-learning-ai-chapters')
   ```
3. If corrupted, clear:
   ```javascript
   localStorage.removeItem('sg-learning-ai-chapters')
   ```

### Poor Quality Content

**Improve by**:
- Using high-resolution exam images
- Ensuring good lighting and contrast
- Uploading images with clear text
- Editing content in review modal before saving

## 💰 Cost Estimation

| Action | Cost | Notes |
|--------|------|-------|
| Extract questions (vision) | $0.01-0.05 | Depends on image size |
| Generate content (text) | $0.01-0.05 | Depends on complexity |
| **Total per upload** | **$0.02-0.10** | ~$1 for 10-50 uploads |

## 🎯 Best Practices

### For Students

1. **Upload clear images**: Better OCR = better content
2. **Review before saving**: AI makes mistakes, check accuracy
3. **Edit as needed**: Customize explanations for your learning style
4. **Use for revision**: Upload past exam papers for targeted practice

### For Developers

1. **Monitor API costs**: Track usage in Azure Portal
2. **Implement rate limiting**: Prevent abuse (e.g., max 5 uploads/hour)
3. **Add error boundaries**: Graceful failure if API down
4. **Cache common patterns**: Reduce API calls for similar exams
5. **User feedback**: Add quality rating for AI-generated content

## 📚 Advanced Usage

### Editing AI Content

In ContentReview modal:
- **Sections tab**: Edit lesson content with markdown preview
- **Exercises tab**: Modify questions, choices, answers
- **Objectives tab**: View/verify learning goals
- **Delete**: Remove poor quality sections/exercises

### Sharing AI Chapters

Currently, AI chapters are user-specific (stored in localStorage). To share:
1. Export chapter JSON from localStorage
2. Import into another user's storage
3. Or migrate to backend database (future feature)

### Bulk Processing

For teachers processing multiple exams:
1. Upload exams one by one
2. Review and standardize content
3. Save as curriculum-aligned chapters
4. Students see chapters in their grade level

## 🔗 Resources

- **Integration Guide**: [AI_EXAM_UPLOAD_INTEGRATION.md](AI_EXAM_UPLOAD_INTEGRATION.md)
- **Architecture Docs**: [CLAUDE.md](CLAUDE.md#ai-exam-upload-feature-new)
- **Azure OpenAI Docs**: https://learn.microsoft.com/en-us/azure/ai-services/openai/
- **GPT-4 Vision Guide**: https://platform.openai.com/docs/guides/vision

## 🆘 Support

Issues or questions? Check:
1. This quickstart guide
2. [AI_EXAM_UPLOAD_INTEGRATION.md](AI_EXAM_UPLOAD_INTEGRATION.md) for detailed setup
3. Browser console for error messages
4. Azure Portal for API usage/errors
5. GitHub issues for bug reports
