<!-- OPENSPEC:START -->
# OpenSpec Instructions

These instructions are for AI assistants working in this project.

Always open `@/openspec/AGENTS.md` when the request:
- Mentions planning or proposals (words like proposal, spec, change, plan)
- Introduces new capabilities, breaking changes, architecture shifts, or big performance/security work
- Sounds ambiguous and you need the authoritative spec before coding

Use `@/openspec/AGENTS.md` to learn:
- How to create and apply change proposals
- Spec format and conventions
- Project structure and guidelines

Keep this managed block so 'openspec update' can refresh the instructions.

<!-- OPENSPEC:END -->

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **SG Learning**, an interactive educational platform for Singapore students from Secondary 1 to Junior College 2. The app provides animated lessons, exercises, and progress tracking for 4 core academic subjects (English, Chinese, Mathematics, Science) plus an AI Playground feature for exploring AI concepts through hands-on activities.

**Tech Stack**: React + TypeScript + Vite + shadcn/ui + Tailwind CSS + Zustand + React Router

**Grade Levels Supported**:
- Secondary 1-4 (Sec 1-4, ages 13-16)
- Junior College 1-2 (JC 1-2, ages 17-18, pre-university)

**Current Content**:
- English Language (6 chapters, 90 exercises) - Sec 1
- Chinese Language/华文 (6 chapters, 90 exercises) - Sec 1
- Mathematics (16 chapters, 240 exercises) - Sec 1
- Science (19 chapters, 257 exercises) - Sec 1
- Computing (6 chapters, 90 exercises) - Sec 3
- AI Playground (10 modules, 27 activities) - available to all grade levels

**Subjects**: 6 total across all grade levels

## Development Commands

```bash
# Install dependencies
npm i

# Start development server (runs on http://localhost:8080)
npm run dev

# Build for production
npm run build

# Build for development (includes component tagger)
npm run build:dev

# Lint code
npm run lint

# Preview production build
npm run preview
```

## Architecture Overview

### State Management (Zustand)

The app uses Zustand with persistence for global state management (`src/lib/store.ts`):

- **User State**: Authentication (login/logout), user profile, guest mode
- **Language & Theme**: Bilingual support (English/Chinese), theme switching
- **Grade Level Selection**: Current grade level (sec1, sec2, sec3, sec4, jc1, jc2)
- **Learning Progress**: Per-chapter tracking of sections completed, exercises completed, scores, time spent
- **AI Module Progress**: Separate tracking for AI Playground modules

Key store methods:
- `setGradeLevel(gradeLevel)`: Sets the current grade level (filters displayed chapters)
- `updateProgress()`: Updates chapter progress (sections/exercises/scores)
- `getChapterProgress(subjectId, chapterId)`: Retrieves progress for a specific chapter
- `toggleAIModuleComplete(moduleId)`: Marks AI modules as complete

Progress is persisted to localStorage under the key `sg-learning-app-storage`.

### Content Structure (JSON-driven)

The app uses **two content systems**:

1. **Academic Subjects** (`src/data/content.json`):
   - English, Chinese, Math, Science, Computing
   - Structure: `subjects[] → chapters[] → { sections[], exercises[] }`
   - Traditional lesson + exercise format

2. **AI Playground** (`src/data/ai-modules.json`):
   - Separate module system for AI learning
   - Structure: `modules[] → { activities[] }`
   - External tool links with suggested prompts
   - 10 modules covering: AI fundamentals, prompting, music/image/video generation, coding assistants, study tools, voice AI, ethics

**Subject Properties** (in content.json):
- `id`, `title`, `title_zh` (Chinese title)
- `description`, `description_zh`
- `color` (theme color)
- `isAIPlayground` (boolean) - flags AI Playground subject for special handling
  - When true, subject card links to `/ai` instead of `/subjects/:id`
  - Shows module count instead of chapter count
  - Uses purple gradient design with Brain icon

**Chapter Properties**:
- `id`, `title`, `title_zh`
- `description`, `description_zh`
- `gradeLevel`: Grade level designation (required) - one of: `"sec1"`, `"sec2"`, `"sec3"`, `"sec4"`, `"jc1"`, `"jc2"`
- `tag`, `tag_zh` (for Science: "Physics", "Chemistry", "Biology")
- `objectives[]`, `objectives_zh[]`
- `sections[]`: Content sections (text, animations, math formulas)
- `exercises[]`: Practice questions

**Section Types**:
- `text`: Plain text lessons
- `animation`: Interactive React components (see below)
- `math`: Mathematical expressions with explanations

**Exercise Types**:
- `mcq`: Multiple choice (single answer)
- `multi`: Multiple choice (multiple answers)
- `short`: Short answer (text input)
- `drag-order`: Drag to reorder items
- `match`: Match pairs

### Animation Components

Custom animated visualizations in `src/components/animations/`:

- `NumberLineReveal`: Animated number line for integers/rational numbers
- `TileCombine`: Visual algebra tiles for like terms
- `FractionVisual`: Interactive fraction visualization
- `EquationBalance`: Balance scale for equation solving
- `ParticlesInStates`: Kinetic particle theory (solid/liquid/gas)
- `ForceMotion`: Forces and motion simulation

**To add new animation**: Create component in `animations/`, then reference in `content.json` by component name (without `.tsx`).

### Routing Structure

Routes defined in `src/App.tsx`:

- `/` - Landing page (Index)
- `/login` - Authentication
- `/dashboard` - User dashboard with recent activity
- `/subjects` - Subject selection grid
- `/subjects/:subjectId` - Chapter list for a subject
- `/subjects/:subjectId/:chapterId` - Chapter view with lessons and exercises
- `/ai` - AI Playground landing
- `/ai/modules/:moduleId` - AI module detail
- `/ai/progress` - AI learning progress
- `/ai/safety` - AI safety education

### Bilingual Support (i18n)

Translations defined in `src/lib/i18n.ts`:

```typescript
const translations = { en: {...}, zh: {...} }
export const useTranslations = (language: 'en' | 'zh') => translations[language]
```

Usage in components:
```typescript
const { language } = useStore();
const t = useTranslations(language);
// Then use: t.login, t.dashboard, etc.
```

All user-facing content must have both `title` and `title_zh`, `description` and `description_zh`, etc.

### Grade Level System

The app supports multiple grade levels from Secondary 1 to Junior College 2. Students select their grade level using the **GradeLevelSelector** component in the header.

**Grade Level Types** (`src/lib/store.ts`):
```typescript
export type GradeLevel = 'sec1' | 'sec2' | 'sec3' | 'sec4' | 'jc1' | 'jc2';
```

**How It Works**:
1. User selects grade level from dropdown in AppHeader (only visible when logged in)
2. Selected grade level stored in Zustand store and persisted to localStorage
3. SubjectDetail page filters chapters based on `chapter.gradeLevel === user.gradeLevel`
4. If no chapters available for selected grade, shows empty state message

**Adding Content for New Grade Levels**:
1. Create new chapters in `src/data/content.json` with appropriate `gradeLevel` property
2. Set `gradeLevel` to one of: `"sec1"`, `"sec2"`, `"sec3"`, `"sec4"`, `"jc1"`, `"jc2"`
3. Chapters will automatically appear when users select that grade level
4. Progress tracking is separate per chapter regardless of grade level

**Example Chapter with Grade Level**:
```json
{
  "id": "advanced-algebra",
  "title": "Advanced Algebra",
  "title_zh": "高级代数",
  "gradeLevel": "sec3",
  "description": "Quadratic functions and inequalities",
  "sections": [...],
  "exercises": [...]
}
```

**Python Script for Bulk Grade Assignment**:
Use `add_grade_levels.py` to add `gradeLevel` property to existing chapters or update them in bulk.

**Current Status**:
- English, Chinese, Math, Science: All chapters designated as Secondary 1 (`"sec1"`)
- Computing: All chapters designated as Secondary 3 (`"sec3"`)
- Content for Sec 2, 4, JC 1-2 needs to be added in future

**AI Playground**: The AI Playground subject does not have chapters and is available to all grade levels.

### Component Organization

```
src/components/
├── animations/      # Interactive lesson animations
├── cards/          # SubjectCard, ChapterCard (display subjects/chapters)
├── exercises/      # ExerciseRenderer, question type components
├── layout/         # AppHeader (navigation bar)
├── lesson/         # SectionRenderer, content display
└── ui/             # shadcn/ui components (Button, Card, Badge, etc.)
```

### Key Pages

- **ChapterView** (`src/pages/ChapterView.tsx`): Main learning experience
  - Renders sections sequentially
  - Tracks progress as user completes sections/exercises
  - Shows objectives, progress ring, celebration confetti

- **SubjectDetail** (`src/pages/SubjectDetail.tsx`):
  - Grid of chapter cards for a subject
  - Shows progress for each chapter (completed/in-progress/not-started)
  - For Science, displays tags (Physics/Chemistry/Biology)

- **AIPlayground** (`src/pages/AIPlayground.tsx`):
  - Special subject with interactive AI modules
  - Categories: Fundamentals, Text & Language, Images & Vision, Audio & Music, Video & Animation, AI Tools

## Adding Content

### Adding a New Chapter

1. Edit `src/data/content.json`
2. Add chapter object to the appropriate subject's `chapters[]` array
3. Include: id, title, title_zh, description, description_zh, tag (for Science), objectives, sections, exercises
4. If using animations, ensure component exists in `src/components/animations/`

### Adding a New Animation

1. Create React component in `src/components/animations/` (e.g., `my-animation.tsx`)
2. Export default component with props interface
3. Reference in `content.json` section: `"content": "MyAnimation"` (match component filename)
4. Pass props via section's `props` field

### Science Chapter Tags

Science chapters must include `tag` and `tag_zh`:
- Physics: `"tag": "Physics"`, `"tag_zh": "物理"`
- Chemistry: `"tag": "Chemistry"`, `"tag_zh": "化学"`
- Biology: `"tag": "Biology"`, `"tag_zh": "生物"`
- General: `"tag": "General"`, `"tag_zh": "综合"`

Tags are color-coded in ChapterCard:
- Physics: Blue (`border-blue-500`)
- Chemistry: Green (`border-green-500`)
- Biology: Purple (`border-purple-500`)

## Styling

- **Tailwind CSS** with custom theme in `tailwind.config.ts`
- **CSS variables** in `src/index.css` for theme colors
- **shadcn/ui** components use `cn()` utility for class merging
- Custom animations use **Framer Motion**
- Progress visualizations use **Recharts**

## Path Aliases

`@/` maps to `src/` directory (configured in `vite.config.ts` and `tsconfig.json`)

Examples:
- `@/components/ui/button` → `src/components/ui/button`
- `@/lib/store` → `src/lib/store`
- `@/data/content.json` → `src/data/content.json`

## Authentication System

The app supports **three authentication methods**:

1. **Email/Password Login** (Demo Mode)
   - Any email/password combination works
   - Sets `user.provider = 'email'`
   - For demonstration and testing purposes

2. **Google OAuth Sign-In** (Real Authentication)
   - Uses `@react-oauth/google` library
   - Requires `VITE_GOOGLE_CLIENT_ID` environment variable
   - Fetches real user data from Google (name, email, profile picture)
   - Sets `user.provider = 'google'`
   - See [GOOGLE_AUTH_SETUP.md](GOOGLE_AUTH_SETUP.md) or [QUICK_SETUP.md](QUICK_SETUP.md) for setup

3. **Guest Mode**
   - No authentication required
   - Sets `user.isGuest = true` and `user.provider = 'guest'`
   - Full app functionality with local progress tracking

**User Object Structure**:
```typescript
interface User {
  id: string;
  email: string;
  name: string;
  isGuest?: boolean;
  provider?: 'email' | 'google' | 'guest';
  photoURL?: string; // For Google users
}
```

**Google OAuth Setup**:
- Set `VITE_GOOGLE_CLIENT_ID` in `.env` file
- Get Client ID from Google Cloud Console (https://console.cloud.google.com/)
- App wrapped with `GoogleOAuthProvider` in `src/App.tsx`
- Login implementation in `src/pages/Login.tsx` uses `useGoogleLogin` hook
- If Client ID not configured, button shows helpful error with setup instructions

**Environment Variables**:
- `.env` - Local configuration (gitignored, set `VITE_GOOGLE_CLIENT_ID` here)
- `.env.example` - Template for developers
- After changing `.env`, restart dev server: `npm run dev`

**Google OAuth Public Access**:
- By default, OAuth apps are in "Testing" mode (only specific test users can sign in)
- Students seeing "Social Account is not yet connected to any Vercel user" error means they're not authorized
- **Solution**: Publish the OAuth app or add students as test users
- See [GOOGLE_OAUTH_PUBLIC_ACCESS.md](GOOGLE_OAUTH_PUBLIC_ACCESS.md) for detailed instructions
- Three options:
  1. Add test users (up to 100) in Google Cloud Console
  2. Publish the app for public use (recommended, no verification needed for basic scopes)
  3. Use Internal user type (Google Workspace organizations only)

## Important Notes

- **Guest Mode**: Users can continue as guest without authentication (sets `user.isGuest = true`)
- **Progress Persistence**: All progress stored in localStorage, survives page refresh
- **Responsive Design**: Mobile-first approach, test on various screen sizes
- **Dark Mode**: Supports light/dark/system themes via `next-themes`
- **Animation Performance**: Use `framer-motion` for smooth animations, optimize for 60fps
- **Content Validation**: Ensure exercise `answer` field matches choice index (0-based) for MCQ

### Critical: Store Hydration and Page Refresh
The app uses Zustand with localStorage persistence. Components must wait for store hydration before checking authentication:

**Store hydration flag**: `_hasHydrated` boolean in store
- Set to `false` on initialization
- Set to `true` after `onRehydrateStorage` completes
- Components check this flag before redirecting unauthenticated users

**Protected pages pattern**:
```typescript
const { user, _hasHydrated } = useStore();

useEffect(() => {
  // Wait for hydration before checking auth
  if (_hasHydrated && !user) {
    navigate('/login');
  }
}, [user, _hasHydrated, navigate]);
```

This prevents premature redirects when users refresh the page.

### Critical: URL-Based State Persistence
Lesson and exercise positions are preserved across page refreshes using URL search parameters:

**LessonPlayer** (`src/components/lesson/lesson-player.tsx`):
- Current section stored in `?section=N` URL parameter
- Reads from URL on mount, writes on section change
- Students stay on same lesson after refresh

**ExercisePlayer** (`src/components/exercises/exercise-player.tsx`):
- Current exercise stored in `?exercise=N` URL parameter
- Reads from URL on mount, writes on exercise change
- Students stay on same exercise after refresh

**Implementation pattern**:
```typescript
const [searchParams, setSearchParams] = useSearchParams();
const sectionParam = searchParams.get('section');
const initialSection = sectionParam ? parseInt(sectionParam, 10) : 0;
const [currentSection, setCurrentSection] = useState(initialSection);

useEffect(() => {
  setSearchParams({ section: currentSection.toString() }, { replace: true });
}, [currentSection, setSearchParams]);
```

The `{ replace: true }` option prevents creating browser history entries for each navigation.

### Critical: Exercise Field Names and Data Structures

**1. Use `prompt` not `question`**:
All exercises MUST use `prompt` and `prompt_zh` fields for question text, NOT `question` and `question_zh`. The exercise components expect the `prompt` field.

**Correct MCQ:**
```json
{
  "id": "ex1",
  "type": "mcq",
  "prompt": "What is the capital of France?",
  "prompt_zh": "法国的首都是什么？",
  "choices": ["Paris", "London", "Berlin"],
  "answer": 0
}
```

**2. Drag-Order Exercise `answer` Field**:
The `answer` field must contain an array of **ordered item strings**, NOT indices.

**Correct:**
```json
{
  "type": "drag-order",
  "items": ["Cell", "Tissue", "Organ"],
  "answer": ["Cell", "Tissue", "Organ"]  // Strings, not [0, 1, 2]
}
```

**Incorrect:**
```json
{
  "type": "drag-order",
  "items": ["Cell", "Tissue", "Organ"],
  "correctOrder": [0, 1, 2]  // Wrong field name and wrong format
}
```

**3. Matching Exercise `pairs` Field**:
The `pairs` field must contain objects with `left`, `right`, `left_zh`, `right_zh` properties, NOT tuples.

**Correct:**
```json
{
  "type": "match",
  "pairs": [
    {
      "left": "H₂O",
      "left_zh": "H₂O",
      "right": "Water",
      "right_zh": "水"
    }
  ]
}
```

**Incorrect:**
```json
{
  "type": "match",
  "pairs": [["H₂O", "Water"]]  // Tuples not supported
}
```

### Critical: Progress Data Preservation
When updating chapter progress with `updateProgress()`, ALWAYS preserve existing progress fields:

**When completing lessons** (in ChapterView.tsx):
```typescript
updateProgress({
  subjectId,
  chapterId,
  sectionsCompleted: chapter.sections.map(s => s.id),
  exercisesCompleted: progress?.exercisesCompleted || [], // Preserve existing
  exerciseScores: progress?.exerciseScores || {},         // Preserve existing
  // ... other fields
});
```

**When completing exercises** (in ChapterView.tsx):
```typescript
updateProgress({
  subjectId,
  chapterId,
  sectionsCompleted: progress?.sectionsCompleted || [], // Preserve existing
  exercisesCompleted: Object.keys(scores),
  exerciseScores: { ...exerciseScores, ...scores },
  // ... other fields
});
```

Failing to preserve existing fields will cause progress data to be reset, leading to inconsistent display in ChapterCard (e.g., showing "Completed" badge but "0/2" lessons).

## Singapore MOE Curriculum Alignment

**Current Status**: The app covers 5 core academic subjects aligned with Singapore MOE curriculum:
- **Sec 1**: English, Chinese, Mathematics, Science (all complete)
- **Sec 3**: Computing (complete, based on Skills of Computing syllabus)

All chapters are verified against official MOE syllabuses.

Content aligned with Singapore Ministry of Education Secondary 1 syllabus:

- **English Language**: 6 chapters
  - Grammar Foundations, Vocabulary Building, Sentence Construction
  - Narrative Writing, Reading Comprehension, Editing & Proofreading

- **Chinese Language (华文)**: 6 chapters
  - Grammar Fundamentals (语法基础), Vocabulary Building (词汇积累), Idioms & Proverbs (成语与俗语)
  - Composition Writing (作文写作), Reading Comprehension (阅读理解), Sentence Correction (修改病句)

- **Mathematics**: 16 chapters (240 exercises total, 15 per chapter)
  - **Numbers & Algebra** (8): Integers & Rational Numbers, Factors/Multiples/Primes, Approximations & Estimations, Algebraic Expressions, Simple Linear Equations, Quadratic Equations, Ratio/Rate/Proportion, Percentage Applications
  - **Geometry & Measurement** (7): Patterns & Sequences, Coordinates & Linear Graphs, Simple Inequalities, Angles & Basic Geometry, Triangles & Polygons, Perimeter & Area, Volume & Surface Area
  - **Statistics** (1): Statistics & Data Analysis

- **Science**: 19 chapters across 3 disciplines
  - **Physics** (7): Scientific Methods & Measurement, Physical Properties of Matter, Light & Reflection, Heat & Temperature, Forces and Motion, Electrical Systems, Pressure, Energy
  - **Chemistry** (4): Particulate Model of Matter, Mixtures & Separation Techniques, Elements/Compounds/Chemical Formulas, Acids & Bases
  - **Biology** (8): Structure & Functions of Cells, Digestive System, Respiratory System, Circulatory System, Human Reproduction, Classification, Food Chains & Food Webs, Adaptations

**Computing** (Secondary 3 - Skills of Computing syllabus): 6 chapters (90 exercises total, 15 per chapter)
- **Introduction to Computing**: Computer hardware/software, computing in society, Singapore Smart Nation, careers
- **Computational Thinking**: Decomposition, pattern recognition, abstraction, algorithms
- **Introduction to Programming**: Programs and languages, sequences, visual programming (Scratch/Blockly), debugging
- **Data and Information**: Binary system, data types, file formats, databases, storage units
- **Networks and the Internet**: Computer networks, WWW, browsers, URLs, IP addresses, online safety, cloud storage
- **Digital Citizenship and Ethics**: Cyberbullying, intellectual property, copyright, PDPA, screen time, digital wellbeing

- Includes local Singapore context (e.g., GST at 9%, HDB buildings, MRT trains, tropical plant adaptations, Singapore's linguistic diversity, PDPA, Smart Nation)

## Exercise Component Architecture

Exercise components in `src/components/exercises/`:

- **exercise-player.tsx**: Main orchestrator for exercise flow
  - Handles exercise navigation (previous/next)
  - Manages score calculation and submission
  - Persists progress to Zustand store
  - **Scoring system**:
    - 100% for correct answer on first attempt
    - 80% for correct answer on second attempt
    - 60% for correct answer on third or later attempts
    - 0% if skipped without correct answer
  - **Average score**: Displayed as "X% Average" badge, calculated as sum of all exercise scores divided by number of completed exercises

- **mcq-exercise.tsx**: Multiple choice (single answer)
  - Radio button selection
  - Shows correct/incorrect feedback with explanations

- **short-answer-exercise.tsx**: Text input questions
  - Supports validators: `"fraction"`, `"equation"`, `"exact"`, `"numeric"`
  - Case-insensitive matching for text answers

- **drag-order-exercise.tsx**: Drag-and-drop ordering
  - Uses `react-dnd` with HTML5Backend
  - Validates item order against correct sequence

- **matching-exercise.tsx**: Pair matching
  - Two-column layout with drag-and-drop
  - Validates all pairs match correctly

**To add new exercise type**:
1. Create component in `exercises/` following existing pattern (props: question, onAnswer, showHint)
2. Add type to exercise type union in `content.json` schema
3. Import and handle in `exercise-player.tsx`

## Content Generation Scripts

Several Python scripts exist for content generation (in root directory):

- **create-chinese-language-chapters.py**: Creates Chinese language chapters
- **create-all-language-chapters.py**: Creates English language chapters
- **integrate-language-subjects.py**: Integrates both English and Chinese subjects into `content.json`
- **generate-content.py**: Generates expanded chapter content from templates
- **integrate-all-chapters.py**: Merges generated chapters into `content.json`

**Important**: All chapter files are stored in `chapters/` directory with naming convention:
- English: `english-*.json`
- Chinese: `chinese-*.json`
- Math: `math-*.json`
- Science: `science-*.json`
- Computing: `computing-*.json`

**Workflow for bulk content additions**:
1. Create individual chapter JSON files in `chapters/` directory
2. Run integration script to merge into `src/data/content.json`
3. **Always backup** before integration: Scripts auto-create `src/data/content-backup-{timestamp}.json`
4. Test in dev environment with `npm run dev` before committing

**Exercise Difficulty Levels**:
Exercises should include a `difficulty` field with values: `"easy"`, `"medium"`, or `"hard"` to support progressive learning. Aim for 10-15 exercises per chapter with graded difficulty (e.g., 4 easy, 5 medium, 5 hard).

## Lovable Integration

This project integrates with Lovable (https://lovable.dev):
- Changes made via Lovable are auto-committed to the repository
- The `lovable-tagger` plugin enables component tracking in dev mode
- Build with `npm run build:dev` includes component tagging for Lovable

## Common Development Workflows

### Testing a New Animation

1. Create animation component: `src/components/animations/my-animation.tsx`
2. Add to a test chapter in `content.json`:
   ```json
   {
     "type": "animation",
     "content": "MyAnimation",
     "props": { "param": "value" }
   }
   ```
3. Run `npm run dev` and navigate to the chapter
4. Verify animation renders and behaves correctly

### Debugging Progress Tracking

Progress is stored in localStorage. To inspect or reset:
```javascript
// In browser console:
localStorage.getItem('sg-learning-app-storage') // View current state
localStorage.removeItem('sg-learning-app-storage') // Reset all progress
```

### Adding Bilingual Content

All user-facing strings need both English and Chinese:
- In `content.json`: `title` + `title_zh`, `description` + `description_zh`, etc.
- In `src/lib/i18n.ts`: Add to both `en` and `zh` translation objects
- Test language switching with the language toggle in AppHeader

### Deploying

Deploy via Lovable dashboard:
1. Open project at https://lovable.dev/projects/46d2181b-ace3-4886-b550-bc9746762717
2. Click Share → Publish
3. Optionally connect custom domain in Project > Settings > Domains

## Common Issues and Troubleshooting

### Exercise Questions Not Displaying

**Symptom**: Exercise shows "Question 1" but no actual question text, only answer choices visible.

**Cause**: Exercise uses `question` field instead of `prompt` field.

**Fix**:
```python
# Find and fix all exercises with 'question' field
python -c "
import json
with open('src/data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
for subject in data['subjects']:
    for chapter in subject['chapters']:
        for exercise in chapter.get('exercises', []):
            if 'question' in exercise:
                exercise['prompt'] = exercise.pop('question')
            if 'question_zh' in exercise:
                exercise['prompt_zh'] = exercise.pop('question_zh')
with open('src/data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
"
```

### Progress Display Inconsistency

**Symptom**: Chapter card shows "Completed" badge but "0/2" lessons or incorrect progress percentage.

**Cause**: `updateProgress()` called without preserving existing `sectionsCompleted` or `exercisesCompleted` arrays.

**Fix**: Always include existing progress when updating (see "Critical: Progress Data Preservation" section above).

### Content.json Too Large to Read

**Symptom**: Read tool fails with "File content exceeds maximum allowed size (256KB)".

**Solution**: Use targeted searches instead:
```bash
# Use Grep to find specific content
grep -r "chapter-id" src/data/content.json

# Or use Python for complex queries
python -c "import json; ..."
```

## Key Architectural Decisions

- **Why Zustand over Redux**: Simpler API, less boilerplate, built-in TypeScript support, and localStorage persistence via middleware
- **Why JSON-driven content**: Non-developers can contribute educational content without touching code
- **Why React Router**: Standard routing library, excellent TypeScript support, and nested routes for subject/chapter hierarchy
- **Why shadcn/ui**: Accessible components, customizable with Tailwind, copy-paste approach (no package bloat)
- **Why Vite over CRA**: Faster dev server with HMR, smaller bundle size, native ESM support

## Language Subjects (English & Chinese)

### English Language Chapters
1. **Grammar Foundations**: Parts of speech, sentence structure, subject-verb agreement
2. **Vocabulary Building**: Context clues, prefixes/suffixes, word families
3. **Sentence Construction**: Avoiding fragments and run-ons, sentence variety
4. **Narrative Writing**: Story structure (exposition, rising action, climax, falling action, resolution), show don't tell
5. **Reading Comprehension**: Main ideas, inferences, author's purpose, text analysis
6. **Editing & Proofreading**: Common errors, punctuation, homophones

### Chinese Language (华文) Chapters
1. **Grammar Fundamentals (语法基础)**: Sentence structure (主谓宾), measure words (量词), word order
2. **Vocabulary Building (词汇积累)**: Word combinations (词语搭配), radicals (部首), character analysis
3. **Idioms & Proverbs (成语与俗语)**: Common 4-character idioms, meanings and origins
4. **Composition Writing (作文写作)**: Narrative essays (记叙文), descriptive techniques, 5W1H method
5. **Reading Comprehension (阅读理解)**: Main ideas, context inference, transition words
6. **Sentence Correction (修改病句)**: Common error types, word order, word collocation

### Language-Specific Features

- **Drag-Order Exercises**: Used in Chinese for word order practice (Subject + Time + Verb + Object)
- **Context-Based Questions**: Both subjects emphasize real-world Singapore examples
- **Show vs. Tell**: English narrative writing focuses on descriptive techniques
- **Bilingual Support**: All content has both English and Chinese versions for accessibility

### Future Interactive Component Ideas for Language Learning

Consider creating these animation components for enhanced language learning:

1. **SentenceDiagram**: Visual sentence structure tree (Subject-Verb-Object breakdown)
2. **CharacterStrokeOrder**: Animated Chinese character writing with stroke sequence
3. **GrammarMatcher**: Interactive matching game for parts of speech
4. **PunctuationPlayground**: Interactive punctuation placement practice
5. **StoryStructureArc**: Visual narrative arc showing plot progression
6. **WordBuildingTree**: Animated word family tree from root words
7. **IdiomStoryAnimation**: Illustrated stories behind Chinese idioms (成语故事)
8. **VocabularyContextClues**: Interactive highlighting of context clues in passages
9. **SentenceExpander**: Step-by-step sentence combining and expansion
10. **CompositionPlanner**: Interactive mind map for essay planning

To implement new language animation:
1. Create component in `src/components/animations/`
2. Export as default with clear props interface
3. Add to `content.json` section with `"type": "animation"` and component name
4. Test with different language settings (en/zh)

## AI Playground Module System

The AI Playground uses a **different architecture** from academic subjects:

### Structure (`src/data/ai-modules.json`)

```json
{
  "modules": [
    {
      "id": "module-id",
      "title": "Module Title",
      "emoji": "🎨",
      "concept": "One-sentence concept explanation",
      "activities": [
        {
          "label": "Activity name",
          "url": "https://external-tool.com",
          "prompt": "Suggested prompt for the tool"
        }
      ]
    }
  ]
}
```

### Current AI Modules (10 total, 27 activities)

1. **What is AI?** (🤖) - ChatGPT, Gemini
2. **Prompt Magic** (✨) - Prompt engineering, few-shot learning
3. **Music Generation** (🎵) - Suno, Mubert
4. **Image Generation** (🎨) - DALL·E, Stable Diffusion, Leonardo AI, Midjourney
5. **Video Generation** (🎬) - Sora, Kling AI, Runway, Pika
6. **AI Coding Assistant** (💻) - Replit, Cursor, Copilot
7. **AI Study Notes** (📝) - NotebookLM, ChatPDF, Perplexity
8. **Local AI (Offline)** (💾) - LM Studio, Ollama
9. **Voice & TTS** (🎤) - ElevenLabs, OpenAI TTS, Descript
10. **AI & the Future (Safety)** (🌍) - Ethics, deepfakes, UNESCO resources

### Progress Tracking

AI module progress is tracked separately in Zustand store:
```typescript
aiProgress: Record<string, { done: boolean }> // moduleId → completion status
```

Methods:
- `toggleAIModuleComplete(moduleId)`: Marks a module as complete/incomplete
- Progress displayed on AI Playground card and `/ai/progress` page

### Adding New AI Modules

1. Edit `src/data/ai-modules.json`
2. Add new module object with id, title, emoji, concept, activities
3. No code changes needed - UI reads JSON dynamically
4. Update count in `SubjectCard.tsx` if total modules change (currently hardcoded as 10)

### AI Playground Pages

- **AIPlayground.tsx** (`/ai`): Main landing page with module grid
- **AIModuleDetail.tsx** (`/ai/modules/:moduleId`): Module detail with activities
- **AIProgress.tsx** (`/ai/progress`): Progress tracking dashboard
- **AISafety.tsx** (`/ai/safety`): Safety guidelines and tips

### Special UI Features

- Purple gradient design theme (distinct from academic subjects)
- Safety notice banner on all AI pages
- External link warnings
- Progress tracking with completion badges
- Responsive grid layout for module cards
