# AI Exam Upload Feature - Integration Guide

This document provides step-by-step instructions to integrate the AI-powered exam upload feature into the SG Learning platform.

## Overview

Students can upload scanned exam papers, which are analyzed by Azure OpenAI GPT-4o to:
1. Extract questions and assess difficulty
2. Generate comprehensive lesson content
3. Create practice exercises matching exam standards
4. Save as a new AI-generated chapter

## Files Created

### Core Services
- `src/lib/azure-openai.ts` - Azure OpenAI integration service
- `src/lib/ai-content-store.ts` - Storage manager for AI-generated chapters

### UI Components
- `src/components/ExamUpload.tsx` - File upload and processing UI
- `src/components/ContentReview.tsx` - Review and edit generated content

### Configuration
- `.env.example` - Added Azure OpenAI environment variables

## Step-by-Step Integration

### Step 1: Install Required Dependencies

```bash
npm install @radix-ui/react-progress @radix-ui/react-tabs
```

### Step 2: Set Up Environment Variables

Create or update your `.env` file:

```bash
# Azure OpenAI Configuration
VITE_AZURE_OPENAI_API_KEY=your-api-key
VITE_AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
VITE_AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
```

Get your credentials from: https://portal.azure.com

### Step 3: Add Missing shadcn/ui Components

```bash
# If these components don't exist, add them:
npx shadcn-ui@latest add progress
npx shadcn-ui@latest add tabs
npx shadcn-ui@latest add alert
npx shadcn-ui@latest add textarea
```

### Step 4: Modify SubjectDetail.tsx

Add the following imports at the top:

```typescript
import { useState } from 'react';
import { Upload } from 'lucide-react';
import { ExamUpload } from '@/components/ExamUpload';
import { ContentReview } from '@/components/ContentReview';
import { aiContentStore, type AIGeneratedChapter } from '@/lib/ai-content-store';
import type { GeneratedContent } from '@/lib/azure-openai';
```

Add state variables after existing hooks:

```typescript
const [showUpload, setShowUpload] = useState(false);
const [generatedContent, setGeneratedContent] = useState<GeneratedContent | null>(null);
const [aiChapters, setAIChapters] = useState<AIGeneratedChapter[]>([]);
```

Add useEffect to load AI chapters:

```typescript
useEffect(() => {
  if (user && subjectId) {
    const chapters = aiContentStore.getChapters(user.id, subjectId);
    setAIChapters(chapters);
  }
}, [user, subjectId]);
```

Add "Upload Exam" button after the subject header (around line 115):

```typescript
{/* Upload Exam Button */}
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.6, delay: 0.1 }}
  className="mb-6"
>
  <Button
    onClick={() => setShowUpload(true)}
    className="w-full sm:w-auto bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700"
  >
    <Upload className="mr-2 h-4 w-4" />
    {language === 'zh' ? '上传试卷' : 'Upload Exam Paper'}
  </Button>
  <p className="text-sm text-muted-foreground mt-2">
    {language === 'zh'
      ? 'AI 将分析试卷并创建学习内容'
      : 'AI will analyze your exam and create lesson content'}
  </p>
</motion.div>
```

Combine AI chapters with existing chapters in the display logic:

```typescript
// After line 48, add:
const aiChaptersForGrade = aiChapters.filter(ch => ch.gradeLevel === gradeLevel);
const allChapters = [...filteredChapters, ...aiChaptersForGrade];
```

Update chapter display to use `allChapters`:

```typescript
// Replace filteredChapters with allChapters in:
// - totalChapters calculation
// - completedChapters filter
// - chapter mapping in the grid
```

Add modals at the end of the component (before the closing div):

```typescript
{/* Upload Exam Modal */}
{showUpload && (
  <ExamUpload
    subject={subjectId}
    subjectTitle={title}
    gradeLevel={gradeLevel}
    onContentGenerated={(content) => {
      setGeneratedContent(content);
      setShowUpload(false);
    }}
    onClose={() => setShowUpload(false)}
  />
)}

{/* Content Review Modal */}
{generatedContent && (
  <ContentReview
    content={generatedContent}
    onSave={(content) => {
      // Save to AI content store
      const saved = aiContentStore.saveChapter(user!.id, subjectId, content);
      setAIChapters([...aiChapters, saved]);
      setGeneratedContent(null);

      // Show success message
      alert(language === 'zh' ? '章节已保存！' : 'Chapter saved successfully!');
    }}
    onCancel={() => setGeneratedContent(null)}
  />
)}
```

### Step 5: Update ChapterCard to Handle AI Chapters

Modify `src/components/cards/chapter-card.tsx` to accept AI-generated chapters:

```typescript
// Add to the ChapterCard props interface:
isAIGenerated?: boolean;

// Add a badge to show AI-generated chapters:
{isAIGenerated && (
  <Badge variant="secondary" className="bg-purple-100 text-purple-700">
    <Sparkles className="w-3 h-3 mr-1" />
    AI Generated
  </Badge>
)}
```

### Step 6: Update ChapterView to Load AI Chapters

In `src/pages/ChapterView.tsx`, add logic to check both content.json and AI content store:

```typescript
import { aiContentStore } from '@/lib/ai-content-store';

// In the component, after loading from contentData:
let chapter = contentData.subjects
  .find(s => s.id === subjectId)
  ?.chapters.find(c => c.id === chapterId);

// If not found in content.json, check AI store
if (!chapter && user) {
  const aiChapter = aiContentStore.getChapter(user.id, chapterId);
  if (aiChapter) {
    chapter = aiChapter;
  }
}
```

### Step 7: Add TypeScript Type Definitions

Ensure your `tsconfig.json` includes proper type checking. No changes needed if using the existing configuration.

### Step 8: Test the Feature

1. **Start dev server**: `npm run dev`
2. **Login** to the app
3. **Select a grade level** and **navigate to a subject**
4. **Click "Upload Exam Paper"**
5. **Upload a test image** (exam paper screenshot)
6. **Wait for AI processing** (may take 30-60 seconds)
7. **Review generated content** in the review modal
8. **Edit if needed** and click "Save Chapter"
9. **Verify** the new chapter appears in the chapter list

## Usage Notes

### Azure OpenAI Configuration

- **Deployment**: Must use GPT-4o or GPT-4 Vision
- **API Version**: 2024-02-15-preview or later
- **Rate Limits**: Be aware of Azure OpenAI rate limits
- **Cost**: Each upload costs approximately $0.02-0.10 depending on image size and complexity

### File Validation

- **Supported formats**: JPG, PNG, WEBP, PDF
- **Max file size**: 10MB
- **Best quality**: High-resolution scans work best
- **Language**: Supports English and Chinese exam papers

### Content Quality

The AI generates:
- **3-4 lesson sections** with markdown formatting
- **10-15 exercises** matching exam difficulty
- **Bilingual content** (English and Chinese)
- **Singapore context** (NEWater, MRT, HDB examples)
- **Pedagogical explanations** (6-step format)

### Limitations

- AI extraction may miss poorly scanned questions
- Math symbols and equations may need manual review
- Generated content should be reviewed before student use
- Requires active internet connection and Azure credits

## Troubleshooting

### "Azure OpenAI is not configured"
- Check `.env` file has all three variables
- Restart dev server after adding environment variables
- Verify variables start with `VITE_` prefix

### Upload fails or times out
- Check Azure OpenAI API key is valid
- Verify endpoint URL is correct
- Check image file size (<10MB)
- Ensure stable internet connection

### Generated content is incomplete
- Try uploading a clearer image
- Check Azure OpenAI deployment has GPT-4o model
- Review console for API error messages

### AI chapters don't appear
- Verify user is logged in
- Check browser localStorage for 'sg-learning-ai-chapters'
- Clear localStorage and try again if corrupted

## Future Enhancements

1. **Batch Upload**: Process multiple exam pages at once
2. **OCR Fallback**: Use alternative OCR if Azure fails
3. **Export/Import**: Share AI-generated chapters between users
4. **Quality Scoring**: Rate AI-generated content quality
5. **Collaborative Review**: Allow teachers to review student uploads
6. **Version History**: Track edits to AI-generated content
7. **Template Library**: Save common lesson patterns
8. **Multi-language**: Support more languages beyond EN/ZH

## Security Considerations

- **API Keys**: Never commit `.env` to git (already in `.gitignore`)
- **User Data**: AI chapters are user-specific in localStorage
- **Content Moderation**: Consider adding content filtering
- **Rate Limiting**: Implement client-side throttling for API calls
- **GDPR Compliance**: Users should own their uploaded content

## Cost Optimization

To reduce Azure OpenAI costs:
1. Cache common exam patterns
2. Limit uploads per user per day
3. Use smaller context windows when possible
4. Implement preview before full generation
5. Offer free tier with limited uploads

## Documentation

- Azure OpenAI Docs: https://learn.microsoft.com/en-us/azure/ai-services/openai/
- GPT-4 Vision Guide: https://platform.openai.com/docs/guides/vision
- React Upload Patterns: https://react.dev/reference/react-dom/components/input#file

## Support

For issues or questions:
1. Check this integration guide
2. Review browser console for errors
3. Test with sample exam images
4. Verify Azure OpenAI dashboard for API usage
5. Open GitHub issue with error details
