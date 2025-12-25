/**
 * Azure OpenAI Service
 * Handles exam question extraction and content generation using GPT-4o
 */

interface AzureOpenAIConfig {
  apiKey: string;
  endpoint: string;
  deploymentName: string;
}

interface ExtractedQuestion {
  questionNumber: number;
  questionText: string;
  questionType: 'mcq' | 'short' | 'long' | 'calculation';
  difficulty: 'easy' | 'medium' | 'hard';
  topic: string;
  choices?: string[];
  answer?: string | number;
}

interface ExamExtraction {
  title: string;
  gradeLevel: string;
  subject: string;
  questions: ExtractedQuestion[];
  topics: string[];
}

interface GeneratedContent {
  chapterId: string;
  title: string;
  title_zh: string;
  description: string;
  description_zh: string;
  gradeLevel: string;
  objectives: string[];
  objectives_zh: string[];
  sections: Array<{
    id: string;
    title: string;
    title_zh: string;
    type: 'text';
    content: string;
    content_zh: string;
  }>;
  exercises: Array<{
    id: string;
    type: 'mcq' | 'multi' | 'short' | 'drag-order' | 'match';
    difficulty: 'easy' | 'medium' | 'hard';
    prompt: string;
    prompt_zh: string;
    choices?: string[];
    choices_zh?: string[];
    answer: number | number[] | string;
    explanation: string;
    explanation_zh: string;
  }>;
}

class AzureOpenAIService {
  private config: AzureOpenAIConfig;

  constructor() {
    this.config = {
      apiKey: import.meta.env.VITE_AZURE_OPENAI_API_KEY || '',
      endpoint: import.meta.env.VITE_AZURE_OPENAI_ENDPOINT || '',
      deploymentName: import.meta.env.VITE_AZURE_OPENAI_DEPLOYMENT_NAME || 'gpt-4o',
    };
  }

  /**
   * Check if Azure OpenAI is properly configured
   */
  isConfigured(): boolean {
    return !!(this.config.apiKey && this.config.endpoint && this.config.deploymentName);
  }

  /**
   * Extract exam questions from image using GPT-4o Vision
   */
  async extractQuestionsFromImage(
    imageFile: File,
    subject: string,
    gradeLevel: string
  ): Promise<ExamExtraction> {
    if (!this.isConfigured()) {
      throw new Error('Azure OpenAI is not configured. Please set environment variables.');
    }

    // Convert image to base64
    const base64Image = await this.fileToBase64(imageFile);

    const systemPrompt = `You are an expert education content analyzer specializing in Singapore MOE curriculum.
Analyze the exam paper image and extract all questions with their details.

Focus on:
1. Question numbering and text
2. Question type (MCQ, short answer, long answer, calculation)
3. Difficulty level based on Singapore exam standards
4. Topic/concept being tested
5. For MCQs, extract all choices and identify the correct answer if visible

Return a structured JSON format.`;

    const userPrompt = `Analyze this ${gradeLevel} ${subject} exam paper from Singapore.
Extract all questions with:
- Question number
- Full question text
- Question type
- Estimated difficulty (easy/medium/hard)
- Topic/concept
- For MCQs: all choices and answer if marked

Format as JSON matching this structure:
{
  "title": "Exam title or topic",
  "gradeLevel": "${gradeLevel}",
  "subject": "${subject}",
  "questions": [
    {
      "questionNumber": 1,
      "questionText": "...",
      "questionType": "mcq",
      "difficulty": "medium",
      "topic": "...",
      "choices": ["A. ...", "B. ...", "C. ...", "D. ..."],
      "answer": "..."
    }
  ],
  "topics": ["topic1", "topic2"]
}`;

    try {
      const response = await fetch(
        `${this.config.endpoint}openai/deployments/${this.config.deploymentName}/chat/completions?api-version=2024-02-15-preview`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'api-key': this.config.apiKey,
          },
          body: JSON.stringify({
            messages: [
              {
                role: 'system',
                content: systemPrompt,
              },
              {
                role: 'user',
                content: [
                  {
                    type: 'text',
                    text: userPrompt,
                  },
                  {
                    type: 'image_url',
                    image_url: {
                      url: `data:${imageFile.type};base64,${base64Image}`,
                    },
                  },
                ],
              },
            ],
            max_tokens: 4000,
            temperature: 0.3,
            response_format: { type: 'json_object' },
          }),
        }
      );

      if (!response.ok) {
        const error = await response.json();
        throw new Error(`Azure OpenAI API error: ${error.error?.message || response.statusText}`);
      }

      const data = await response.json();
      const content = data.choices[0].message.content;
      return JSON.parse(content);
    } catch (error) {
      console.error('Error extracting questions:', error);
      throw error;
    }
  }

  /**
   * Generate comprehensive lesson content from extracted questions
   */
  async generateLessonContent(
    extraction: ExamExtraction,
    subject: string
  ): Promise<GeneratedContent> {
    if (!this.isConfigured()) {
      throw new Error('Azure OpenAI is not configured.');
    }

    const systemPrompt = `You are an expert Singapore MOE curriculum content creator.
Create comprehensive, exam-focused lesson content that prepares students for the difficulty level shown in the exam questions.

Requirements:
1. Content must match Singapore MOE ${extraction.gradeLevel} ${subject} syllabus
2. Include Singapore-specific examples (NEWater, MRT, HDB, hawker centers, etc.)
3. Use proper markdown formatting (\n\n for paragraphs, **bold**, numbered lists)
4. Use LaTeX for math equations (e.g., $x^2$, $\frac{1}{2}$)
5. Create 3-4 lesson sections covering the exam topics
5. Generate 15 practice exercises matching exam difficulty
6. Provide bilingual content (English and Chinese)
7. Explanations must use pedagogical 6-step format:
   - Problem statement
   - Key concept
   - Step-by-step solution
   - Final answer
   - Common mistakes
   - Quick tips`;

    const topicsStr = extraction.topics.join(', ');
    const questionsPreview = extraction.questions
      .slice(0, 5)
      .map((q) => `Q${q.questionNumber}: ${q.questionText.slice(0, 100)}...`)
      .join('\n');

    const userPrompt = `Based on this ${extraction.gradeLevel} ${subject} exam:

Topics: ${topicsStr}

Sample Questions:
${questionsPreview}

Total Questions: ${extraction.questions.length}
Difficulty Distribution:
- Easy: ${extraction.questions.filter((q) => q.difficulty === 'easy').length}
- Medium: ${extraction.questions.filter((q) => q.difficulty === 'medium').length}
- Hard: ${extraction.questions.filter((q) => q.difficulty === 'hard').length}

Generate:
1. Chapter title (descriptive, exam-focused)
2. Chapter description
3. Learning objectives (3-5 objectives)
4. 3-4 lesson sections with comprehensive content
5. 15 practice exercises matching exam difficulty

Return JSON matching this structure:
{
  "chapterId": "generated-chapter-id",
  "title": "Chapter Title",
  "title_zh": "章节标题",
  "description": "...",
  "description_zh": "...",
  "gradeLevel": "${extraction.gradeLevel}",
  "objectives": ["...", "..."],
  "objectives_zh": ["...", "..."],
  "sections": [
    {
      "id": "section-1",
      "title": "Section Title",
      "title_zh": "部分标题",
      "type": "text",
      "content": "Markdown formatted content with \\n\\n paragraphs...",
      "content_zh": "中文内容..."
    }
  ],
  "exercises": [
    {
      "id": "ex-1",
      "type": "mcq",
      "difficulty": "medium",
      "prompt": "Question text",
      "prompt_zh": "问题文本",
      "choices": ["A", "B", "C", "D"],
      "choices_zh": ["A", "B", "C", "D"],
      "answer": 0,
      "explanation": "**Problem:** ...\\n\\n**Key Concept:** ...\\n\\n**Steps:** ...\\n\\n✔ **Final Answer:** ...",
      "explanation_zh": "..."
    }
  ]
}`;

    try {
      const response = await fetch(
        `${this.config.endpoint}openai/deployments/${this.config.deploymentName}/chat/completions?api-version=2024-02-15-preview`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'api-key': this.config.apiKey,
          },
          body: JSON.stringify({
            messages: [
              {
                role: 'system',
                content: systemPrompt,
              },
              {
                role: 'user',
                content: userPrompt,
              },
            ],
            max_tokens: 8000,
            temperature: 0.7,
            response_format: { type: 'json_object' },
          }),
        }
      );

      if (!response.ok) {
        const error = await response.json();
        throw new Error(`Azure OpenAI API error: ${error.error?.message || response.statusText}`);
      }

      const data = await response.json();
      const content = data.choices[0].message.content;
      return JSON.parse(content);
    } catch (error) {
      console.error('Error generating content:', error);
      throw error;
    }
  }

  /**
   * Convert File to base64 string
   */
  private async fileToBase64(file: File): Promise<string> {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => {
        const result = reader.result as string;
        // Remove data URL prefix
        const base64 = result.split(',')[1];
        resolve(base64);
      };
      reader.onerror = reject;
      reader.readAsDataURL(file);
    });
  }

  /**
   * Generate similar practice questions based on an original question
   */
  async generateSimilarQuestions(
    originalQuestion: {
      prompt: string;
      type: 'mcq' | 'multi' | 'short' | 'drag-order' | 'match';
      choices?: string[];
      answer: number | number[] | string | string[];
      explanation?: string;
    },
    subject: string,
    gradeLevel: string,
    count: number = 3
  ): Promise<Array<{
    id: string;
    type: 'mcq' | 'multi' | 'short';
    prompt: string;
    prompt_zh: string;
    choices?: string[];
    choices_zh?: string[];
    answer: number | string;
    explanation: string;
    explanation_zh: string;
  }>> {
    if (!this.isConfigured()) {
      throw new Error('Azure OpenAI is not configured. Please set environment variables.');
    }

    const systemPrompt = `You are an expert Singapore MOE curriculum teacher.
Generate ${count} similar practice questions based on the original question provided.
The new questions should:
1. Test the same concept but with different numbers, contexts, or scenarios
2. Match the difficulty level of the original question
3. Be appropriate for ${gradeLevel} ${subject} students
4. Include Singapore-specific contexts where appropriate (NEWater, MRT, HDB, hawker centres, etc.)
5. Have clear, educational explanations

Return valid JSON only.`;

    const userPrompt = `Original Question:
${originalQuestion.prompt}

Type: ${originalQuestion.type}
${originalQuestion.choices ? `Choices: ${originalQuestion.choices.join(', ')}` : ''}
Answer: ${JSON.stringify(originalQuestion.answer)}
${originalQuestion.explanation ? `Explanation: ${originalQuestion.explanation}` : ''}

Generate ${count} similar questions in this exact JSON format:
{
  "questions": [
    {
      "id": "similar-1",
      "type": "${originalQuestion.type === 'multi' ? 'mcq' : originalQuestion.type}",
      "prompt": "Question text in English",
      "prompt_zh": "问题文本（中文）",
      "choices": ["Option A", "Option B", "Option C", "Option D"],
      "choices_zh": ["选项A", "选项B", "选项C", "选项D"],
      "answer": 0,
      "explanation": "Clear explanation of the answer...",
      "explanation_zh": "答案解释（中文）..."
    }
  ]
}

For short answer questions, omit choices and use string answer.`;

    try {
      const response = await fetch(
        `${this.config.endpoint}openai/deployments/${this.config.deploymentName}/chat/completions?api-version=2024-02-15-preview`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'api-key': this.config.apiKey,
          },
          body: JSON.stringify({
            messages: [
              { role: 'system', content: systemPrompt },
              { role: 'user', content: userPrompt },
            ],
            max_tokens: 3000,
            temperature: 0.7,
            response_format: { type: 'json_object' },
          }),
        }
      );

      if (!response.ok) {
        const error = await response.json();
        throw new Error(`Azure OpenAI API error: ${error.error?.message || response.statusText}`);
      }

      const data = await response.json();
      const content = data.choices[0].message.content;
      const parsed = JSON.parse(content);
      return parsed.questions || [];
    } catch (error) {
      console.error('Error generating similar questions:', error);
      throw error;
    }
  }
}

// Export singleton instance
export const azureOpenAIService = new AzureOpenAIService();

// Export types
export type { ExamExtraction, ExtractedQuestion, GeneratedContent };
