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

This is **SG Learning**, an interactive educational platform for Singapore Secondary 1 students. The app provides animated lessons, exercises, and progress tracking for Mathematics and Science (Physics, Chemistry, Biology), plus an AI Playground feature for exploring AI concepts.

**Tech Stack**: React + TypeScript + Vite + shadcn/ui + Tailwind CSS + Zustand + React Router

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
- **Learning Progress**: Per-chapter tracking of sections completed, exercises completed, scores, time spent
- **AI Module Progress**: Separate tracking for AI Playground modules

Key store methods:
- `updateProgress()`: Updates chapter progress (sections/exercises/scores)
- `getChapterProgress(subjectId, chapterId)`: Retrieves progress for a specific chapter
- `toggleAIModuleComplete(moduleId)`: Marks AI modules as complete

Progress is persisted to localStorage under the key `sg-learning-app-storage`.

### Content Structure (JSON-driven)

All educational content lives in `src/data/content.json`. Structure:

```
subjects[] → chapters[] → { sections[], exercises[] }
```

**Subject Properties**:
- `id`, `title`, `title_zh` (Chinese title)
- `description`, `description_zh`
- `color` (theme color)
- `isAIPlayground` (boolean, special handling for AI Playground)

**Chapter Properties**:
- `id`, `title`, `title_zh`
- `description`, `description_zh`
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

## Important Notes

- **Guest Mode**: Users can continue as guest without authentication (sets `user.isGuest = true`)
- **Progress Persistence**: All progress stored in localStorage, survives page refresh
- **Responsive Design**: Mobile-first approach, test on various screen sizes
- **Dark Mode**: Supports light/dark/system themes via `next-themes`
- **Animation Performance**: Use `framer-motion` for smooth animations, optimize for 60fps
- **Content Validation**: Ensure exercise `answer` field matches choice index (0-based) for MCQ

## Singapore MOE Curriculum Alignment

**Current Status**: The app fully covers all 4 core academic subjects required for Singapore MOE Secondary 1 curriculum (English, Chinese, Mathematics, Science). As of the latest update, all chapters are complete and verified against official MOE syllabuses.

Content aligned with Singapore Ministry of Education Secondary 1 syllabus:

- **English Language**: 6 chapters
  - Grammar Foundations, Vocabulary Building, Sentence Construction
  - Narrative Writing, Reading Comprehension, Editing & Proofreading

- **Chinese Language (华文)**: 6 chapters
  - Grammar Fundamentals (语法基础), Vocabulary Building (词汇积累), Idioms & Proverbs (成语与俗语)
  - Composition Writing (作文写作), Reading Comprehension (阅读理解), Sentence Correction (修改病句)

- **Mathematics**: 15 chapters
  - **Numbers & Algebra** (7): Integers & Rational Numbers, Factors/Multiples/Primes, Approximations & Estimations, Algebraic Expressions, Simple Linear Equations, Ratio/Rate/Proportion, Percentage Applications
  - **Geometry & Measurement** (7): Patterns & Sequences, Coordinates & Linear Graphs, Simple Inequalities, Angles & Basic Geometry, Triangles & Polygons, Perimeter & Area, Volume & Surface Area
  - **Statistics** (1): Statistics & Data Analysis

- **Science**: 17 chapters across 3 disciplines
  - **Physics** (7): Scientific Methods & Measurement, Light & Reflection, Heat & Temperature, Forces and Motion, Pressure, Energy
  - **Chemistry** (4): Particulate Model of Matter, Mixtures & Separation Techniques, Elements/Compounds/Chemical Formulas, Acids & Bases
  - **Biology** (6): Structure & Functions of Cells, Digestive System, Respiratory System, Circulatory System, Human Reproduction, Classification, Food Chains & Food Webs

- Includes local Singapore context (e.g., GST at 9%, HDB buildings, MRT trains, tropical plant adaptations, Singapore's linguistic diversity)

## Exercise Component Architecture

Exercise components in `src/components/exercises/`:

- **exercise-player.tsx**: Main orchestrator for exercise flow
  - Handles exercise navigation (previous/next)
  - Manages score calculation and submission
  - Persists progress to Zustand store

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
