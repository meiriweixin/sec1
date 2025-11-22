import { useState } from 'react';
import { Upload, FileImage, Loader2, CheckCircle, XCircle, AlertCircle } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { azureOpenAIService, type ExamExtraction, type GeneratedContent } from '@/lib/azure-openai';

interface ExamUploadProps {
  subject: string;
  subjectTitle: string;
  gradeLevel: string;
  onContentGenerated: (content: GeneratedContent) => void;
  onClose: () => void;
}

type UploadStage = 'idle' | 'uploading' | 'extracting' | 'generating' | 'complete' | 'error';

export function ExamUpload({
  subject,
  subjectTitle,
  gradeLevel,
  onContentGenerated,
  onClose,
}: ExamUploadProps) {
  const [stage, setStage] = useState<UploadStage>('idle');
  const [progress, setProgress] = useState(0);
  const [selectedFiles, setSelectedFiles] = useState<File[]>([]);
  const [previewUrls, setPreviewUrls] = useState<string[]>([]);
  const [extraction, setExtraction] = useState<ExamExtraction | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleFileSelect = (event: React.ChangeEvent<HTMLInputElement>) => {
    const files = Array.from(event.target.files || []);
    if (files.length === 0) return;

    // Validate file types
    const validTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp', 'application/pdf'];
    const invalidFiles = files.filter(file => !validTypes.includes(file.type));
    if (invalidFiles.length > 0) {
      setError('Please upload only JPG, PNG, WEBP, or PDF files');
      return;
    }

    // Validate total file size (max 50MB total for multiple files)
    const totalSize = files.reduce((sum, file) => sum + file.size, 0);
    if (totalSize > 50 * 1024 * 1024) {
      setError('Total file size must be less than 50MB');
      return;
    }

    // Validate individual file size (max 10MB each)
    const oversizedFiles = files.filter(file => file.size > 10 * 1024 * 1024);
    if (oversizedFiles.length > 0) {
      setError('Each file must be less than 10MB');
      return;
    }

    setSelectedFiles(files);
    setError(null);

    // Create previews for images
    const newPreviewUrls: string[] = [];
    files.forEach((file, index) => {
      if (file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = (e) => {
          newPreviewUrls[index] = e.target?.result as string;
          if (newPreviewUrls.filter(Boolean).length === files.filter(f => f.type.startsWith('image/')).length) {
            setPreviewUrls([...newPreviewUrls]);
          }
        };
        reader.readAsDataURL(file);
      }
    });
  };

  const handleUpload = async () => {
    if (selectedFiles.length === 0) return;

    // Check if Azure OpenAI is configured
    if (!azureOpenAIService.isConfigured()) {
      setError(
        'Azure OpenAI is not configured. Please add VITE_AZURE_OPENAI_API_KEY, VITE_AZURE_OPENAI_ENDPOINT, and VITE_AZURE_OPENAI_DEPLOYMENT_NAME to your .env file.'
      );
      return;
    }

    try {
      setStage('uploading');
      setProgress(10);

      // Stage 1: Extract questions from all images
      setStage('extracting');
      setProgress(20);

      // Process files sequentially to avoid rate limits
      const allExtractions: ExamExtraction[] = [];
      const filesCount = selectedFiles.length;

      for (let i = 0; i < filesCount; i++) {
        const file = selectedFiles[i];
        const fileProgress = 20 + (i / filesCount) * 40; // Progress from 20% to 60%
        setProgress(fileProgress);

        const extractedData = await azureOpenAIService.extractQuestionsFromImage(
          file,
          subjectTitle,
          gradeLevel
        );
        allExtractions.push(extractedData);
      }

      // Merge all extractions into one
      const mergedExtraction: ExamExtraction = {
        title: allExtractions[0].title,
        gradeLevel: gradeLevel,
        subject: subjectTitle,
        questions: allExtractions.flatMap(e => e.questions),
        topics: Array.from(new Set(allExtractions.flatMap(e => e.topics))),
      };

      setExtraction(mergedExtraction);
      setProgress(60);

      // Stage 2: Generate lesson content from merged questions
      setStage('generating');
      setProgress(70);

      const generatedContent = await azureOpenAIService.generateLessonContent(
        mergedExtraction,
        subjectTitle
      );

      setProgress(100);
      setStage('complete');

      // Pass generated content to parent
      setTimeout(() => {
        onContentGenerated(generatedContent);
      }, 1000);
    } catch (err) {
      console.error('Upload error:', err);
      setError(err instanceof Error ? err.message : 'Failed to process exam. Please try again.');
      setStage('error');
      setProgress(0);
    }
  };

  const getStageMessage = () => {
    const fileCount = selectedFiles.length;
    switch (stage) {
      case 'uploading':
        return `Uploading ${fileCount} file${fileCount > 1 ? 's' : ''}...`;
      case 'extracting':
        return `Extracting questions from ${fileCount} file${fileCount > 1 ? 's' : ''} with AI...`;
      case 'generating':
        return 'Generating lesson content...';
      case 'complete':
        return 'Content generated successfully!';
      case 'error':
        return 'An error occurred';
      default:
        return '';
    }
  };

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50">
      <Card className="w-full max-w-2xl p-6 bg-white dark:bg-gray-800">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h2 className="text-2xl font-bold">Upload Exam Paper</h2>
            <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">
              {subjectTitle} - {gradeLevel.toUpperCase()}
            </p>
          </div>
          <Button variant="ghost" size="sm" onClick={onClose}>
            ✕
          </Button>
        </div>

        {error && (
          <Alert variant="destructive" className="mb-4">
            <AlertCircle className="h-4 w-4" />
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        )}

        {stage === 'idle' && (
          <div className="space-y-4">
            <div className="border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-lg p-8 text-center">
              <input
                type="file"
                id="exam-upload"
                className="hidden"
                accept="image/*,.pdf"
                multiple
                onChange={handleFileSelect}
              />
              <label htmlFor="exam-upload" className="cursor-pointer">
                <FileImage className="w-16 h-16 mx-auto text-gray-400 mb-4" />
                <p className="text-lg font-medium mb-2">Click to upload exam paper</p>
                <p className="text-sm text-gray-600 dark:text-gray-400">
                  Select multiple images or PDFs (max 10MB each, 50MB total)
                </p>
              </label>
            </div>

            {selectedFiles.length > 0 && (
              <div className="mt-4">
                <p className="text-sm font-medium mb-2">
                  {selectedFiles.length} file{selectedFiles.length > 1 ? 's' : ''} selected
                </p>
                <div className="grid grid-cols-2 gap-2 max-h-64 overflow-y-auto">
                  {previewUrls.map((url, index) => url && (
                    <img
                      key={index}
                      src={url}
                      alt={`Preview ${index + 1}`}
                      className="w-full h-32 object-cover rounded border"
                    />
                  ))}
                  {selectedFiles.map((file, index) => !file.type.startsWith('image/') && (
                    <div key={index} className="w-full h-32 flex items-center justify-center bg-gray-100 dark:bg-gray-700 rounded border">
                      <div className="text-center">
                        <FileImage className="w-8 h-8 mx-auto text-gray-400 mb-1" />
                        <p className="text-xs text-gray-600 dark:text-gray-400">{file.name}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            <div className="bg-blue-50 dark:bg-blue-900/20 p-4 rounded-lg">
              <h3 className="font-semibold mb-2 flex items-center gap-2">
                <Upload className="w-4 h-4" />
                How it works:
              </h3>
              <ol className="text-sm space-y-1 list-decimal list-inside">
                <li>Upload a scanned exam paper image</li>
                <li>AI extracts questions and analyzes difficulty</li>
                <li>System generates comprehensive lesson content</li>
                <li>Practice exercises created matching exam difficulty</li>
                <li>Review and save as new chapter</li>
              </ol>
            </div>

            <div className="flex gap-3">
              <Button onClick={handleUpload} disabled={selectedFiles.length === 0} className="flex-1">
                <Upload className="w-4 h-4 mr-2" />
                Process Exam Paper{selectedFiles.length > 1 ? 's' : ''}
              </Button>
              <Button variant="outline" onClick={onClose}>
                Cancel
              </Button>
            </div>
          </div>
        )}

        {(stage === 'uploading' || stage === 'extracting' || stage === 'generating') && (
          <div className="space-y-4">
            <div className="flex items-center gap-3">
              <Loader2 className="w-6 h-6 animate-spin text-blue-600" />
              <span className="font-medium">{getStageMessage()}</span>
            </div>

            <Progress value={progress} className="w-full" />

            {extraction && stage === 'generating' && (
              <div className="bg-green-50 dark:bg-green-900/20 p-4 rounded-lg mt-4">
                <h3 className="font-semibold mb-2 flex items-center gap-2">
                  <CheckCircle className="w-4 h-4 text-green-600" />
                  Questions Extracted:
                </h3>
                <ul className="text-sm space-y-1">
                  <li>• Total Questions: {extraction.questions.length}</li>
                  <li>• Topics: {extraction.topics.join(', ')}</li>
                  <li>
                    • Difficulty: Easy ({extraction.questions.filter((q) => q.difficulty === 'easy').length}), Medium ({extraction.questions.filter((q) => q.difficulty === 'medium').length}), Hard ({extraction.questions.filter((q) => q.difficulty === 'hard').length})
                  </li>
                </ul>
              </div>
            )}
          </div>
        )}

        {stage === 'complete' && (
          <div className="text-center space-y-4">
            <CheckCircle className="w-16 h-16 mx-auto text-green-600" />
            <div>
              <h3 className="text-xl font-bold text-green-600">Success!</h3>
              <p className="text-gray-600 dark:text-gray-400 mt-2">
                Content generated successfully. Redirecting to review...
              </p>
            </div>
          </div>
        )}

        {stage === 'error' && (
          <div className="text-center space-y-4">
            <XCircle className="w-16 h-16 mx-auto text-red-600" />
            <div>
              <h3 className="text-xl font-bold text-red-600">Error</h3>
              <p className="text-gray-600 dark:text-gray-400 mt-2">
                Please try again or contact support if the problem persists.
              </p>
            </div>
            <Button onClick={() => setStage('idle')}>Try Again</Button>
          </div>
        )}
      </Card>
    </div>
  );
}
