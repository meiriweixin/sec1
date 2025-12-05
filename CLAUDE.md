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
- English Language (12 chapters, 180 exercises) - Sec 1 (6 ch) + Sec 2 (6 ch)
- Chinese Language/华文 (12 chapters, 180 exercises) - Sec 1 (6 ch) + Sec 2 (6 ch)
- Mathematics (60 chapters, 900 exercises) - Sec 1 (16 ch) + Sec 2 (14 ch) + Sec 3 (8 ch) + Sec 4 (6 ch) + **JC 1 (8 ch)** + **JC 2 (8 ch)** ✅
- Science (49 chapters, 735 exercises) - Sec 1 (19 ch) + Sec 2 (15 ch) + Sec 3 (15 ch)
- Computing (18 chapters, 270 exercises) - Sec 1 (6 ch) + Sec 2 (6 ch) + Sec 3 (6 ch)
- **Physics (H2)** (8 chapters, 90 exercises) - **JC 1 (8 ch, complete)** ✅
- AI Playground (10 modules, 27 activities) - available to all grade levels

**Total**: 159 chapters, 2,327 exercises across 7 subjects and 6 grade levels

**Grade Level Distribution**:
- **Secondary 1-4**: Full coverage across all subjects
- **JC 1**: Mathematics (8 chapters, 120 exercises) ✅ | Physics (8 chapters, 90 exercises) ✅ COMPLETE
- **JC 2**: Mathematics (8 chapters, 120 exercises) ✅ COMPLETE

**All Sec 3 Science chapters now have comprehensive lesson content** (33 sections added across 11 chapters in late 2024)

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
- **Learning Progress**: **User-specific** per-chapter tracking of sections completed, exercises completed, scores, time spent
- **AI Module Progress**: **User-specific** tracking for AI Playground modules
- **Exercise Votes**: **User-specific** difficulty ratings (easy/hard/issue) for individual exercises

**CRITICAL: User-Specific Progress Architecture**

Progress data is stored separately for each user using their user ID as a key:

```typescript
// Store structure
allUsersProgress: Record<string, Progress[]>  // userId → Progress[]
allUsersAIProgress: Record<string, Record<string, AIModuleProgress>>  // userId → aiProgress
allUsersExerciseVotes: Record<string, ExerciseVote[]>  // userId → ExerciseVote[]
```

**When accessing progress in components:**
```typescript
// ✅ CORRECT - Get user-specific progress
const { user, allUsersProgress, allUsersAIProgress } = useStore();
const userId = user?.id;
const userProgress = userId ? (allUsersProgress[userId] || []) : [];
const userAIProgress = userId ? (allUsersAIProgress[userId] || {}) : {};

// ❌ WRONG - Do NOT access progress directly
const { progress, aiProgress } = useStore(); // These fields don't exist!
```

**Key store methods** (all automatically filter by current user):
- `setGradeLevel(gradeLevel)`: Sets the current grade level (filters displayed chapters)
- `updateProgress()`: Updates chapter progress for current user (sections/exercises/scores)
- `getChapterProgress(subjectId, chapterId)`: Retrieves progress for current user's specific chapter
- `getSubjectProgress(subjectId)`: Returns all chapter progress for current user in a subject
- `toggleAIModuleComplete(moduleId)`: Marks AI modules as complete for current user
- `voteExercise(subjectId, chapterId, exerciseId, vote)`: Records or updates user's difficulty vote for an exercise
- `getExerciseVote(subjectId, chapterId, exerciseId)`: Retrieves user's current vote for an exercise (returns 'easy' | 'hard' | 'issue' | null)

**Why user-specific?**
- Different users (email, Google, guest) maintain separate progress
- Re-login preserves user's own progress, not other users' data
- Supports multiple authentication methods with isolated data

Progress is persisted to localStorage under the key `sg-learning-app-storage` with automatic migration from legacy single-user format.

## Recent Major Updates

### December 2024
- ✅ Smart answer validation (flexible matching, Unicode handling)
- ✅ AI exam upload with multiple file support
- ✅ Fixed 98 sections with formatting issues
- ✅ Math section explanations now render markdown
- ✅ All Sec 3 Science chapters have comprehensive lessons (33 sections added)
- ✅ **JC 1 Mathematics COMPLETE** (8 chapters, 24 sections, 120 exercises)
- ✅ **JC 1 Physics COMPLETE** (8 chapters, 24 sections, 90 exercises)
  - Measurement (15 exercises)
  - Kinematics (15 exercises)
  - Dynamics (10 exercises)
  - Forces (10 exercises)
  - Work, Energy, and Power (10 exercises)
  - Current of Electricity (10 exercises)
  - DC Circuits (10 exercises)
  - Waves (10 exercises)
- ✅ **JC 2 Mathematics COMPLETE** (8 chapters, 24 sections, 120 exercises)
  - Integration Techniques (15 exercises: substitution, by parts, partial fractions)
  - Definite Integrals & Applications (15 exercises: area, volumes, trapezium rule)
  - Differential Equations (15 exercises: separable, growth/decay, Newton's cooling)
  - Maclaurin Series (15 exercises: expansions, approximations, operations)
  - Permutations & Combinations (15 exercises: arrangements, selections, restrictions)
  - Probability & Distributions (15 exercises: rules, conditional, binomial)
  - Sampling & Hypothesis Testing (15 exercises: CLT, confidence intervals, tests)
  - Complex Numbers (15 exercises: operations, Argand, polar, De Moivre)

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

### Lesson Content Rendering

The `LessonPlayer` component (`src/components/lesson/lesson-player.tsx`) uses **ReactMarkdown** with `remark-gfm`, `remark-math`, and `rehype-katex` plugins to render lesson content with full markdown and math support.

**Supported markdown features:**
- Paragraphs (separated by `\n\n`)
- Headings (# ## ###)
- Bold (**text**) and italics (*text*)
- Numbered lists (1. 2. 3.)
- Bullet lists (- or *)
- Tables (GitHub-flavored markdown)
- Code blocks with syntax highlighting
- Inline code (`code`)
- **Math formulas**: Inline math `$x^2$` and display math `$$\frac{a}{b}$$` using KaTeX

**Custom styling:**
The component applies Tailwind prose classes with custom overrides for:
- Paragraph spacing (`mb-4`)
- Heading hierarchy with proper sizing
- List indentation and spacing
- Table borders and padding
- Code block styling with monospace font
- Dark mode support via `dark:prose-invert`

**Content storage format:**
All lesson content in `content.json` should be stored as markdown strings with proper escape sequences (`\n\n` for line breaks). The ReactMarkdown component will automatically render the markdown to HTML with appropriate styling.

**Math rendering in exercises:**
Exercise questions, choices, hints, and explanations also support math formulas using the same markdown + KaTeX system. The following components render math:
- `exercise-player.tsx` - Question prompts, hints, explanations
- `mcq-exercise.tsx` - Multiple choice options
- All exercise types support LaTeX math in their text fields

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
- English, Chinese: Sec 1 and Sec 2 content available
- Mathematics: Sec 1, Sec 2, Sec 3, Sec 4, **JC 1 (COMPLETE)**, and **JC 2 (COMPLETE)** content available
- Science: Sec 1, Sec 2, and Sec 3 content available (all chapters have lesson content)
- Computing: Sec 1, Sec 2, and Sec 3 content available
- **JC Mathematics 100% COMPLETE**: JC 1 has 8/8 chapters (120 exercises), JC 2 has 8/8 chapters (120 exercises) ✅

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

### Adding JC-Level Content

JC (Junior College) content requires higher mathematical rigor aligned with Singapore H2 Mathematics syllabus. Follow this workflow:

**1. Research syllabus** (document in `JC_MATH_SYLLABUS.md`)
- H2 Mathematics topics for JC 1-2
- JC 1: Functions, Calculus (Differentiation), Vectors, Sequences & Series
- JC 2: Integration, Differential Equations, Statistics, Complex Numbers

**2. Create chapters in batches** (save to `chapters/jc1_math_chapters.json`)
- Minimum 3 sections per chapter with comprehensive lesson content
- Include Singapore-specific examples (CPF interest rates, HDB pricing, MRT routes, NEWater calculations)
- Use proper mathematical notation with LaTeX support (inline `$...$` and display `$$...$$`)
- Bilingual content (English + Chinese) for all fields

**3. Generate exercises in batches** (e.g., `create_jc1_exercises_batch2.py`)
- **15 exercises per chapter**: 5 easy, 5 medium, 5 hard
- Use pedagogical 6-step explanation format:
  1. **Problem**: Restate the question
  2. **Key Concept**: Identify the main concept
  3. **Steps**: Show step-by-step solution
  4. **Answer**: State the final answer
  5. **Common Mistakes**: Address typical errors
  6. **Tip**: Provide helpful insight
- Smart answer validation for mathematical expressions (supports Unicode, symbols, fractions)
- Test exercises in batches before moving to next chapter

**4. Integrate into main content** (`integrate_jc1_math.py`)
- Script creates automatic backup: `content-backup-jc1-integration-{timestamp}.json`
- Loads `chapters/jc1_math_chapters.json` and `src/data/content.json`
- Appends JC chapters to appropriate subject's chapters array
- Saves updated content.json with proper formatting (ensure_ascii=False, indent=2)

**5. Test in app**
- Select JC 1 or JC 2 from grade level dropdown in header
- Navigate to subject (e.g., Mathematics)
- Verify chapters appear with correct gradeLevel filtering
- Test lesson rendering with proper LaTeX display
- Verify exercise validation works for mathematical inputs
- Check progress tracking and completion status

**Example chapter structure for JC content**:
```json
{
  "id": "functions-graphical-transformations-jc1",
  "title": "Functions & Graphical Transformations",
  "title_zh": "函数与图形变换",
  "gradeLevel": "jc1",
  "description": "Understanding function notation and graphical transformations",
  "description_zh": "理解函数符号和图形变换",
  "objectives": [
    "Understand function notation and domain/range",
    "Apply graphical transformations (translations, reflections, stretches)"
  ],
  "objectives_zh": ["理解函数符号和定义域/值域", "应用图形变换（平移、反射、拉伸）"],
  "sections": [
    {
      "id": "transformations-basics",
      "type": "text",
      "title": "Types of Transformations",
      "title_zh": "变换类型",
      "content": "**Graphical transformations** modify the position...\n\n**Example**: In Singapore's MRT fare system..."
    }
  ],
  "exercises": [...]
}
```

**Current JC Progress** (December 2024):
- ✅ **JC 1 Mathematics: COMPLETE** - 8 chapters, 24 sections, 120 exercises (100%)
  - All 8 chapters have comprehensive lessons and exercises
  - Integrated into main content.json
  - Tested and verified working
- ✅ **JC 1 Physics: COMPLETE** - 8 chapters, 24 sections, 90 exercises (100%)
  - **Chapter 1**: Measurement - 15 exercises ✓
  - **Chapter 2**: Kinematics - 15 exercises ✓
  - **Chapter 3**: Dynamics - 10 exercises ✓
  - **Chapter 4**: Forces - 10 exercises ✓
  - **Chapter 5**: Work, Energy, and Power - 10 exercises ✓
  - **Chapter 6**: Current of Electricity - 10 exercises ✓
  - **Chapter 7**: DC Circuits - 10 exercises ✓
  - **Chapter 8**: Waves - 10 exercises ✓
  - All chapters integrated into main content.json
- ✅ **JC 2 Mathematics: COMPLETE** - 8 chapters, 24 sections, 120 exercises (100%)
  - **Chapter 1**: Integration Techniques - 15 exercises ✓
  - **Chapter 2**: Definite Integrals & Applications - 15 exercises ✓
  - **Chapter 3**: Differential Equations - 15 exercises ✓
  - **Chapter 4**: Maclaurin Series - 15 exercises ✓
  - **Chapter 5**: Permutations & Combinations - 15 exercises ✓
  - **Chapter 6**: Probability & Distributions - 15 exercises ✓
  - **Chapter 7**: Sampling & Hypothesis Testing - 15 exercises ✓
  - **Chapter 8**: Complex Numbers - 15 exercises ✓
  - All chapters integrated into main content.json
- ⏳ Other subjects (English, Chinese): JC content not yet planned

**JC Mathematics Integration Scripts**:
- `create_jc1_exercises_batch4.py` through `batch6.py` - JC 1 Math exercise creation
- `integrate_jc1_exercises.py` - JC 1 Math integration script
- `create_jc2_chapter1_complete.py` through `chapter4_complete.py` - JC 2 Math exercise creation
- `integrate_jc2_complete.py` - Final JC 2 Math integration script
- `chapters/jc1_math_chapters.json` - Source file for JC 1 Math chapters
- `chapters/jc2_math_chapters.json` - Source file for JC 2 Math chapters

**JC Physics Integration Scripts**:
- `create_jc1_physics_exercises_batch1_complete.py` - Batch 1 (Measurement + Kinematics: 30 exercises)
- `create_jc1_physics_exercises_batch2_quick.py` - Batch 2 initial (Dynamics + Forces: 6 exercises)
- `expand_batch2.py` - Batch 2 expansion (added 14 more exercises to reach 20 total)
- `create_batch3.py` - Batch 3 (Work/Energy/Power + Current Electricity: 20 exercises)
- `create_batch4.py` - Batch 4 (DC Circuits + Waves: 20 exercises)
- `integrate_jc1_physics.py` - JC 1 Physics integration script
- `chapters/jc1_physics_chapters.json` - Source file for JC 1 Physics chapters

**JC Content Achievement Summary**:
- **Total JC chapters**: 24 (8 JC 1 Math + 8 JC 1 Physics + 8 JC 2 Math)
- **Total JC exercises**: 330 (120 JC 1 Math + 90 JC 1 Physics + 120 JC 2 Math)
- **Total JC sections**: 72 (24 JC 1 Math + 24 JC 1 Physics + 24 JC 2 Math)
- **Completion status**: 100% - Singapore H2 Mathematics and H2 Physics (JC1) syllabuses covered
- **Quality**: All exercises follow 6-step pedagogical format with Singapore context
- **Bilingual**: Full English and Chinese support throughout

**Note**: The subject IDs in content.json are `'math'` and `'physics-jc'`. Integration scripts find chapters by `gradeLevel: 'jc1'` or `'jc2'`.

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
- **Sec 1**: English (6 ch), Chinese (6 ch), Mathematics (16 ch), Science (19 ch)
- **Sec 2**: English (6 ch), Chinese (6 ch), Mathematics (14 ch), Science (15 ch), Computing (6 ch)
- **Sec 3**: Mathematics (8 ch), Science (15 ch), Computing (6 ch)
- **Sec 4**: Mathematics (6 ch)

All chapters are verified against official MOE syllabuses. Science Sec 3 content includes NEW 2024 syllabus updates (Electromagnetic Spectrum, Polymers & Recycling, updated Ecology topics).

**Important**: All 15 Sec 3 Science chapters now have comprehensive lesson content with 3-4 sections each, including Singapore-specific examples (NEWater, MRT, HDB, etc.). This was completed in late 2024 to address the gap where 11 chapters had exercises but no lessons.

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

- **Science**: 49 chapters across 3 disciplines and 3 grade levels
  - **Sec 1** (19 chapters):
    - Physics (7): Scientific Methods & Measurement, Physical Properties of Matter, Light & Reflection, Heat & Temperature, Forces and Motion, Electrical Systems, Pressure, Energy
    - Chemistry (4): Particulate Model of Matter, Mixtures & Separation Techniques, Elements/Compounds/Chemical Formulas, Acids & Bases
    - Biology (8): Structure & Functions of Cells, Digestive System, Respiratory System, Circulatory System, Human Reproduction, Classification, Food Chains & Food Webs, Adaptations
  - **Sec 2** (15 chapters):
    - Physics (5): Work/Energy/Power, Moments & Levers, Kinetic Particle Theory, Sound, Magnetism
    - Chemistry (5): Chemical Changes, Oxidation & Reduction, Rate of Reaction, Reactivity Series, Chemical Bonding
    - Biology (5): Photosynthesis, Transport in Plants, Respiration, Human Transport System, Coordination & Response
  - **Sec 3** (15 chapters):
    - Physics (6): Electromagnetic Spectrum (NEW), Current Electricity, Electromagnetism, Static Electricity, Turning Effects of Forces, Pressure in Fluids
    - Chemistry (5): Quantitative Chemistry, Salts & Neutralization, Polymers & Recycling (NEW), Atmosphere & Environment, Electrolysis
    - Biology (4): Reproduction & Cell Division (MERGED), Inheritance & Genetics, Ecology & Human Impact (UPDATED), Biotechnology

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
  - **Exercise Voting System**: Students can rate difficulty of each exercise
    - Three vote options: Easy, Hard, Issue
    - Vote buttons displayed in header row aligned with question title
    - Votes are user-specific and persisted to localStorage
    - Students can re-vote by clicking a different button
    - Selected vote is highlighted with filled button style

- **mcq-exercise.tsx**: Multiple choice (single answer)
  - Radio button selection
  - Shows correct/incorrect feedback with explanations

- **short-answer-exercise.tsx**: Text input questions
  - **Smart validation (default)**: Flexible answer matching with normalization
    - Unicode subscript/superscript handling (H₂O = H2O)
    - Whitespace normalization
    - Symbol equivalence (× = *, ÷ = /)
    - Article removal (the, a, an)
    - Punctuation handling
    - Word-based matching for multi-word answers
  - Specialized validators:
    - `"numeric"`: Float comparison with ±0.001 tolerance (41 exercises)
    - `"fraction"`: Fraction/decimal equivalence (2 exercises)
    - `"strict"`: Exact case-insensitive match (rare, for formatting-critical exercises)
    - `"equation"`: Special equation validation (1 exercise)
  - Case-insensitive by default
  - All previously "exact" validators updated to use smart default (146 exercises)

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

**Language Content**:
- **create-chinese-language-chapters.py**: Creates Chinese language chapters
- **create-all-language-chapters.py**: Creates English language chapters
- **integrate-language-subjects.py**: Integrates both English and Chinese subjects into `content.json`

**Subject Content Generation**:
- **create_sec1_*.py**, **create_sec2_*.py**, **create_sec3_*.py**, **create_sec4_*.py**: Generate chapters for specific grade levels and subjects
- **create_sec*_exercises.py**: Add exercises to generated chapters
- **integrate_sec*.py**: Merge generated chapters into `content.json`
- **generate-content.py**: Generates expanded chapter content from templates
- **integrate-all-chapters.py**: Merges generated chapters into `content.json`

**Lesson Content Creation**:
- **create_sec3_science_lessons.py**: Creates comprehensive lesson content for Sec 3 Science chapters
- **complete_sec3_science_lessons.py**: Adds lessons for additional Sec 3 Science chapters
- **final_sec3_science_lessons.py**: Completes remaining Sec 3 Science lesson content
- **absolute_final_sec3_science.py**: Final batch of Sec 3 Science lessons (Reproduction, Salts, Forces)

**Content Enhancement**:
- **enhance_exercise_explanations.py**: Transforms exercise explanations to pedagogical 6-step format
- **enhance_science_singapore_context.py**: Adds Singapore-specific examples to Science lessons
- **fix_lesson_formatting.py**: Fixes broken markdown and enhances lesson structure

**Utilities**:
- **randomize_answers.py**: Randomizes MCQ answer positions across all chapters to ensure even distribution
- **add_grade_levels.py**: Bulk assigns `gradeLevel` property to chapters

**Important**: All chapter files are stored in `chapters/` directory with naming convention:
- English: `english-*.json` or `sec*-english-*.json`
- Chinese: `chinese-*.json` or `sec*-chinese-*.json`
- Math: `math-*.json` or `sec*-math-*.json`
- Science: `science-*.json` or `sec*-science-*.json`
- Computing: `computing-*.json` or `sec*-computing-*.json`

**Workflow for bulk content additions**:
1. Create individual chapter JSON files in `chapters/` directory
2. Run integration script to merge into `src/data/content.json`
3. **Always backup** before integration: Scripts auto-create `src/data/content-backup-{timestamp}.json`
4. Test in dev environment with `npm run dev` before committing

**Exercise Difficulty Levels**:
Exercises should include a `difficulty` field with values: `"easy"`, `"medium"`, or `"hard"` to support progressive learning. Aim for 10-15 exercises per chapter with graded difficulty (e.g., 4 easy, 5 medium, 5 hard).

**Answer Randomization**:
MCQ exercises should have answers distributed across all choice positions (0, 1, 2, 3) to avoid patterns. Use `randomize_answers.py` script to shuffle answer positions while maintaining correct answers. Target distribution: roughly 25% per position, with no single position >50%. This prevents students from gaming the system by always selecting the first option.

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

## Content Formatting Requirements

### Lesson Content Must Use Markdown

Lesson content in `content.json` must be formatted with proper markdown syntax to display correctly in the app. The `LessonPlayer` component uses ReactMarkdown to render content.

**Required markdown formatting:**
- Use `\n\n` for paragraph breaks
- Use numbered lists: `1. Item one\n2. Item two`
- Use `**bold**` for emphasis and section headers
- Use proper spacing between sections

**Example of properly formatted content:**
```json
{
  "type": "text",
  "content": "To solve simultaneous equations by substitution:\n\n1. Make one variable the subject in one equation\n2. Substitute into the other equation\n3. Solve for the remaining variable\n4. Find the other variable\n\n**Example: Singapore hawker stalls**\n\nIf 2 plates of chicken rice and 3 drinks cost $12, and 1 plate costs $2 more than a drink, find the prices."
}
```

**Formatting Script:**
Use `format_content_markdown.py` to automatically add markdown formatting to plain text content. The script:
- Creates automatic backups before making changes
- Converts numbered lists to proper markdown format
- Adds paragraph breaks at sentence boundaries
- Bolds section headers (Example:, Key Terms:, etc.)
- Processes all text sections and explanations

Run with: `python format_content_markdown.py`

## Common Issues and Troubleshooting

### Lesson Content Displays as One Paragraph

**Symptom**: Lesson text appears as one long paragraph without line breaks, bullet points, or proper formatting.

**Cause**: Content in `content.json` is stored as plain text without markdown formatting (no `\n\n` for paragraphs, no list markers).

**Fix**: Add proper markdown syntax to the content field:
1. Use the `format_content_markdown.py` script to automatically format existing content
2. Or manually add markdown: `\n\n` for paragraph breaks, `1. 2. 3.` for numbered lists, `**bold**` for headers

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

## AI Exam Upload Feature (NEW)

The app now supports AI-powered exam paper analysis using Azure OpenAI GPT-4o Vision. Students can upload scanned exam images, and the system automatically generates comprehensive lesson content and exercises.

### Architecture

**Core Services** (`src/lib/`):
- **azure-openai.ts**: Azure OpenAI GPT-4o integration
  - `extractQuestionsFromImage()`: Vision API to extract questions from images
  - `generateLessonContent()`: Creates lessons, exercises, and objectives
  - `isConfigured()`: Checks if Azure credentials are set
- **ai-content-store.ts**: localStorage-based storage for AI-generated chapters
  - User-specific storage using `userId` as key
  - CRUD operations: `getChapters()`, `saveChapter()`, `updateChapter()`, `deleteChapter()`
  - Storage key: `'sg-learning-ai-chapters'`

**UI Components** (`src/components/`):
- **ExamUpload.tsx**: Modal for uploading and processing exam images
  - **Multiple file upload support**: Students can upload multiple exam pages at once
  - File validation (JPG, PNG, WEBP, PDF, max 10MB per file, 50MB total)
  - Multi-stage progress: uploading → extracting → generating → complete
  - Sequential processing to avoid API rate limits
  - Merges questions from all images into single comprehensive lesson
  - Preview grid showing thumbnails of all selected images
  - Shows extracted question summary before generation
- **ContentReview.tsx**: Modal for reviewing and editing AI-generated content
  - Tabbed interface: Sections | Exercises | Objectives
  - Inline editing with markdown preview
  - Content validation before saving

**Integration Points**:
- **SubjectDetail.tsx**: "Upload Exam Paper" button, modals for upload and review
- **ChapterCard.tsx**: Purple "AI Generated" badge with Sparkles icon
- **ChapterView.tsx**: Loads AI chapters from `aiContentStore` if not found in `content.json`

### Environment Configuration

Required variables in `.env` (see `.env.example`):
```bash
VITE_AZURE_OPENAI_API_KEY=your-api-key
VITE_AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
VITE_AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
```

Get credentials from: https://portal.azure.com

### Workflow

1. Student selects grade level and subject
2. Clicks "Upload Exam Paper" button in SubjectDetail page
3. Uploads one or more exam images (supports multiple pages) → AI extracts questions from each image
4. System merges all extracted questions and analyzes difficulty
5. AI generates bilingual lesson content with Singapore context based on combined questions
6. Student reviews and edits content in ContentReview modal
7. Saves as new chapter → appears in chapter list with "AI Generated" badge

### Data Structures

**ExamExtraction**:
```typescript
{
  title: string;
  gradeLevel: string;
  subject: string;
  questions: ExtractedQuestion[];
  topics: string[];
}
```

**GeneratedContent** (extends AIGeneratedChapter):
```typescript
{
  chapterId: string;
  title: string;
  title_zh: string;
  description: string;
  description_zh: string;
  gradeLevel: string;
  objectives: string[];
  objectives_zh: string[];
  sections: Section[];
  exercises: Exercise[];
  isAIGenerated: true;
  createdAt: string;
  createdBy: string; // userId
  subjectId: string;
}
```

### Content Generation

AI generates:
- **3-4 lesson sections** with markdown formatting
- **10-15 exercises** matching exam difficulty (easy/medium/hard)
- **Bilingual content** (English and Chinese)
- **Singapore context** (NEWater, MRT, HDB, hawker centers)
- **Pedagogical explanations** (6-step format: Problem → Key Concept → Steps → Answer → Common Mistakes → Tips)

### Important Notes

- **Cost**: Each upload costs ~$0.02-0.10 depending on image complexity
- **Rate Limits**: Azure OpenAI has rate limits; consider client-side throttling
- **Content Quality**: AI-generated content should be reviewed before student use
- **User-Specific**: AI chapters are stored per user ID, not globally shared
- **Grade Filtering**: AI chapters are filtered by selected grade level like regular chapters
- **Progress Tracking**: AI chapters use same progress tracking as regular chapters

### Testing

1. Add Azure credentials to `.env` file
2. Restart dev server: `npm run dev`
3. Login and select a grade level
4. Navigate to any subject
5. Click "Upload Exam Paper"
6. Upload one or more test exam images (try multiple pages to test merging)
7. Verify preview grid shows all selected images
8. Wait for processing (30-60 seconds for single image, longer for multiple)
9. Review generated content with merged questions from all images
10. Save and verify chapter appears with AI badge

### Troubleshooting

**"Azure OpenAI is not configured"**:
- Check `.env` file has all three `VITE_AZURE_OPENAI_*` variables
- Restart dev server after adding variables
- Verify variables start with `VITE_` prefix

**Upload fails or times out**:
- Check Azure OpenAI API key is valid
- Verify endpoint URL is correct
- Ensure each image file size < 10MB (50MB total for multiple files)
- Check stable internet connection
- For multiple files, processing time increases (sequential to avoid rate limits)
- Reduce number of files if timing out

**AI chapters don't appear**:
- Verify user is logged in
- Check browser localStorage for `'sg-learning-ai-chapters'`
- Clear localStorage if corrupted: `localStorage.removeItem('sg-learning-ai-chapters')`
- **Store hydration timing**: AI chapters load in SubjectDetail.tsx only after `_hasHydrated` is true
- Check browser console for debug logs:
  - `[AI Store] Total chapters in storage: N` - Shows total chapters saved
  - `Loaded AI chapters: N for user: [userId] subject: [subjectId]` - Shows filtered chapters loaded
  - If chapters aren't loading, verify user ID matches between save and load operations
- **User ID consistency**:
  - Email/password login: Always uses `id: "user1"` (hardcoded in Login.tsx)
  - Google login: Uses `id: "google_[sub]"` (consistent per Google account)
  - Guest mode: Uses `id: "guest"`
  - AI chapters are user-specific, so different users won't see each other's chapters

See [AI_EXAM_UPLOAD_INTEGRATION.md](AI_EXAM_UPLOAD_INTEGRATION.md) for detailed integration guide.

### Known Issue: AI Chapters and Store Hydration

**Problem**: AI-generated chapters may not appear after page refresh if loaded before Zustand store hydration completes.

**Solution**: The `SubjectDetail.tsx` useEffect that loads AI chapters now depends on `_hasHydrated`:
```typescript
useEffect(() => {
  if (_hasHydrated && user && subjectId) {
    const chapters = aiContentStore.getChapters(user.id, subjectId);
    setAIChapters(chapters);
  }
}, [_hasHydrated, user, subjectId]);
```

This ensures user data is fully loaded from localStorage before attempting to retrieve AI chapters. Debug logging has been added to both `ai-content-store.ts` and `SubjectDetail.tsx` to help diagnose persistence issues.
