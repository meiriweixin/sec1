/**
 * Azure OpenAI service for evaluating humanities subject answers
 * Supports: History, English, Chinese, Geography, and other text-based subjects
 */

interface EvaluationRequest {
  subject: string; // 'history', 'english', 'chinese', 'geography'
  questionType: string; // 'short', 'sbq-inference', 'sbq-utility', 'sbq-reliability'
  prompt: string;
  prompt_zh?: string;
  studentAnswer: string;
  modelAnswer?: string;
  sampleAnswers?: string[];
  sourceText?: string; // For SBQ questions
  markingCriteria?: {
    level2?: string;
    level1?: string;
  };
  gradeLevel?: string; // 'sec1', 'sec2', etc.
  language?: 'en' | 'zh';
}

interface EvaluationResult {
  score: number; // 0-100
  isCorrect: boolean;
  level?: 1 | 2; // For marking criteria
  feedback: string;
  feedback_zh?: string;
  strengths?: string[];
  improvements?: string[];
}

const API_KEY = import.meta.env.VITE_AZURE_OPENAI_API_KEY;
const ENDPOINT = import.meta.env.VITE_AZURE_OPENAI_ENDPOINT;
const DEPLOYMENT_NAME = import.meta.env.VITE_AZURE_OPENAI_DEPLOYMENT_NAME || 'gpt-4o';

export const isConfigured = (): boolean => {
  return !!(API_KEY && ENDPOINT && DEPLOYMENT_NAME);
};

export async function evaluateHumanitiesAnswer(
  request: EvaluationRequest
): Promise<EvaluationResult> {
  if (!isConfigured()) {
    throw new Error('Azure OpenAI is not configured. Please set environment variables.');
  }

  // Build evaluation prompt based on subject and question type
  const systemPrompt = buildSystemPrompt(request);
  const userPrompt = buildUserPrompt(request);

  try {
    const url = `${ENDPOINT}/openai/deployments/${DEPLOYMENT_NAME}/chat/completions?api-version=2024-08-01-preview`;

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'api-key': API_KEY,
      },
      body: JSON.stringify({
        messages: [
          { role: 'system', content: systemPrompt },
          { role: 'user', content: userPrompt }
        ],
        temperature: 0.3, // Lower temperature for consistent grading
        max_tokens: 800,
        response_format: { type: 'json_object' }
      }),
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('Azure OpenAI API error:', errorText);
      throw new Error(`API request failed: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    const content = data.choices[0]?.message?.content;

    if (!content) {
      throw new Error('No response from API');
    }

    const result: EvaluationResult = JSON.parse(content);
    return result;

  } catch (error) {
    console.error('Error evaluating answer:', error);
    throw error;
  }
}

function buildSystemPrompt(request: EvaluationRequest): string {
  const { subject, questionType, gradeLevel } = request;

  // Base system prompt
  let prompt = `You are an experienced ${getSubjectName(subject)} teacher in Singapore, evaluating ${gradeLevel || 'Secondary'} student answers.

Your task is to:
1. Assess the student's answer against the model answer and marking criteria
2. Provide constructive feedback in a supportive tone
3. Identify strengths and areas for improvement
4. Assign an appropriate score and level

`;

  // Subject-specific guidelines
  switch (subject) {
    case 'history':
      prompt += `**History Assessment Guidelines:**
- For Sec 1: Focus on "identify" and "describe" level (AO1/AO2), NOT advanced causation analysis
- Check if student uses EVIDENCE from sources (if provided)
- Evaluate historical understanding, not just factual recall
- For SBQ: Apply ONPC framework (Origin, Nature, Purpose, Content)
- Look for: use of source quotes, contextual understanding, inference skills

`;
      break;

    case 'english':
      prompt += `**English Assessment Guidelines:**
- Check grammar, vocabulary, sentence structure
- Evaluate clarity and coherence of expression
- Look for appropriate use of literary devices (if relevant)
- Assess understanding of passage/text (if provided)
- Consider spelling and punctuation

`;
      break;

    case 'chinese':
    case '华文':
      prompt += `**Chinese/华文 Assessment Guidelines:**
- Check proper use of 成语 (idioms) if relevant
- Evaluate sentence structure (主谓宾)
- Look for appropriate 词语搭配 (word collocation)
- Assess understanding of text (if provided)
- Consider character accuracy and expression clarity

`;
      break;

    case 'geography':
      prompt += `**Geography Assessment Guidelines:**
- Check for specific geographical terminology
- Evaluate understanding of concepts (physical/human geography)
- Look for examples and case studies (Singapore or global)
- Assess map/diagram interpretation skills (if relevant)

`;
      break;
  }

  // Question type-specific guidelines
  if (questionType.startsWith('sbq')) {
    prompt += `**Source-Based Question (SBQ) Specific:**
- The student MUST reference the source in their answer
- Check for direct quotes or paraphrasing from source
- Evaluate inference/interpretation quality
- For Utility/Reliability: Check if student considers ONPC
- Don't penalize for not using exact model answer wording - look for understanding

`;
  }

  prompt += `
**Response Format:**
Return a JSON object with this structure:
{
  "score": <number 0-100>,
  "isCorrect": <boolean>,
  "level": <1 or 2 or null>,
  "feedback": "<English feedback, 2-3 sentences>",
  "feedback_zh": "<Chinese feedback, 2-3 sentences>",
  "strengths": ["<strength 1>", "<strength 2>"],
  "improvements": ["<improvement suggestion 1>", "<improvement suggestion 2>"]
}

**Scoring Guide:**
- 90-100: Excellent answer, meets Level 2 criteria fully
- 70-89: Good answer, meets Level 2 with minor gaps
- 50-69: Acceptable answer, meets Level 1 criteria
- 30-49: Partial understanding, some valid points
- 0-29: Minimal understanding or major errors

**Important:**
- Be encouraging and supportive (these are students learning)
- Focus on what they DID right first, then areas to improve
- Accept alternative phrasings if the core understanding is correct
- If student answer is in Chinese, provide feedback_zh in Chinese
- If student answer is in English, provide feedback in English
`;

  return prompt;
}

function buildUserPrompt(request: EvaluationRequest): string {
  const {
    prompt,
    prompt_zh,
    studentAnswer,
    modelAnswer,
    sampleAnswers,
    sourceText,
    markingCriteria,
    language
  } = request;

  let userPrompt = `**Question:**\n${language === 'zh' && prompt_zh ? prompt_zh : prompt}\n\n`;

  if (sourceText) {
    userPrompt += `**Source Text:**\n${sourceText}\n\n`;
  }

  userPrompt += `**Student's Answer:**\n"${studentAnswer}"\n\n`;

  if (modelAnswer) {
    userPrompt += `**Model Answer:**\n${modelAnswer}\n\n`;
  }

  if (sampleAnswers && sampleAnswers.length > 0) {
    userPrompt += `**Sample Acceptable Answers:**\n`;
    sampleAnswers.forEach((answer, idx) => {
      userPrompt += `${idx + 1}. ${answer}\n`;
    });
    userPrompt += '\n';
  }

  if (markingCriteria) {
    userPrompt += `**Marking Criteria:**\n`;
    if (markingCriteria.level2) {
      userPrompt += `Level 2 (Higher): ${markingCriteria.level2}\n`;
    }
    if (markingCriteria.level1) {
      userPrompt += `Level 1 (Basic): ${markingCriteria.level1}\n`;
    }
    userPrompt += '\n';
  }

  userPrompt += `Please evaluate the student's answer and provide feedback in the specified JSON format.`;

  return userPrompt;
}

function getSubjectName(subjectId: string): string {
  const names: Record<string, string> = {
    history: 'History',
    english: 'English Language',
    chinese: 'Chinese Language',
    '华文': 'Chinese Language',
    geography: 'Geography',
    literature: 'Literature'
  };
  return names[subjectId] || 'Humanities';
}

// Utility function to check if a subject should use AI evaluation
export function shouldUseAIEvaluation(subjectId: string, questionType: string): boolean {
  const humanitiesSubjects = ['history', 'english', 'chinese', '华文', 'geography', 'literature'];
  const aiQuestionTypes = ['short', 'sbq', 'sbq-inference', 'sbq-utility', 'sbq-reliability', 'sbq-comparison'];

  return humanitiesSubjects.includes(subjectId.toLowerCase()) &&
         aiQuestionTypes.some(type => questionType.includes(type));
}
