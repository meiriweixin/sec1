# Project Context

## Purpose
**SG Learning** is an interactive educational platform for Singapore Secondary 1 students. The app provides animated lessons, interactive exercises, and progress tracking for all 4 core academic subjects (English, Chinese, Mathematics, Science), plus an AI Playground feature for exploring AI concepts. Content is fully aligned with Singapore MOE curriculum and supports bilingual learning (English/Chinese).

## Tech Stack
- **Frontend Framework**: React 18 with TypeScript
- **Build Tool**: Vite
- **UI Library**: shadcn/ui components with Tailwind CSS
- **State Management**: Zustand with localStorage persistence
- **Routing**: React Router v6
- **Animations**: Framer Motion
- **Data Visualization**: Recharts
- **Styling**: Tailwind CSS with CSS variables for theming
- **Package Manager**: npm
- **Deployment**: Lovable (https://lovable.dev)

## Project Conventions

### Code Style
- **TypeScript**: Strict mode enabled, no implicit any
- **Component Pattern**: Functional components with hooks only (no class components)
- **File Naming**: kebab-case for files (`chapter-view.tsx`), PascalCase for component names
- **Import Aliases**: Use `@/` prefix for all imports (maps to `src/`)
- **Styling**: Tailwind utility classes; use `cn()` helper for class merging
- **No Emojis**: Avoid emojis in code/UI unless explicitly requested by user
- **Bilingual**: All user-facing content requires both English (`title`) and Chinese (`title_zh`) versions

### Architecture Patterns
- **Content-Driven**: All educational content lives in `src/data/content.json` (JSON-driven architecture)
- **State Management**: Single Zustand store (`src/lib/store.ts`) with persistence middleware
- **Translations**: Centralized in `src/lib/i18n.ts` using `useTranslations(language)` hook
- **Routing**: Hierarchical routes (`/subjects/:subjectId/:chapterId`)
- **Component Organization**:
  - `animations/` - Interactive lesson visualizations
  - `cards/` - Subject and chapter display cards
  - `exercises/` - Exercise player and question types
  - `layout/` - Navigation and headers
  - `lesson/` - Content section renderers
  - `ui/` - shadcn/ui primitives

### Testing Strategy
- Prefer manual testing in development mode (`npm run dev`)
- Validate content.json structure before integration
- Test both language modes (en/zh) for all new features
- Test responsive layouts on mobile and desktop
- Verify progress persistence in localStorage after page refresh

### Git Workflow
- **Main Branch**: `main` (production-ready)
- **Commit Style**: Descriptive messages focusing on "why" rather than "what"
- **Pre-commit**: Lint with `npm run lint` before commits
- **Backup Policy**: Auto-backup `content.json` before bulk changes (timestamped backups in `src/data/`)
- **Lovable Integration**: Changes via Lovable auto-commit to repository

## Domain Context

### Singapore MOE Curriculum Alignment
Content must align with Singapore Ministry of Education Secondary 1 syllabus:
- **English**: 6 chapters (Grammar, Vocabulary, Writing, Reading, Editing)
- **Chinese (华文)**: 6 chapters (语法, 词汇, 成语, 作文, 阅读, 修改病句)
- **Mathematics**: 15 chapters (Numbers, Algebra, Geometry, Statistics)
- **Science**: 17 chapters across Physics (7), Chemistry (4), Biology (6)

### Educational Design Principles
- **Progressive Learning**: Exercises graded by difficulty (easy → medium → hard)
- **Show, Don't Tell**: Prefer interactive animations over static text
- **Context-Based**: Use Singapore-specific examples (HDB, MRT, GST at 9%)
- **Bilingual Support**: All content accessible in English and Chinese
- **Guest Mode**: Allow learning without authentication

### Content Structure
```
subjects[] → chapters[] → { sections[], exercises[] }
```
- **Sections**: Types = text, animation, math
- **Exercises**: Types = mcq, multi, short, drag-order, match
- **Progress Tracking**: Per-chapter (sections completed, exercises completed, scores, time spent)

## Important Constraints

### Performance
- Bundle size optimization (Vite tree-shaking)
- 60fps for all animations (use Framer Motion)
- Fast HMR in development (<200ms)

### Accessibility
- shadcn/ui components are WCAG 2.1 AA compliant
- Use semantic HTML (`<section>`, `<article>`, `<nav>`)
- Keyboard navigation support for all interactive elements

### Browser Support
- Modern browsers (Chrome, Firefox, Safari, Edge - latest 2 versions)
- Mobile-first responsive design (breakpoints: sm, md, lg, xl)

### Content Integrity
- Never modify `content.json` directly without backup
- Validate JSON structure after generation (`npx jsonlint`)
- Ensure all exercise answers are zero-indexed
- All animations must have corresponding component in `src/components/animations/`

## External Dependencies

### MCP Servers (Claude Code)
- **context7**: Library documentation lookup
- **cloudflare-docs**: Cloudflare documentation search
- **cloudflare-bindings**: Cloudflare Workers/Pages management
- **playwright**: Browser automation testing
- **chrome-devtools**: Browser dev tools integration

### Key npm Packages
- `react-router-dom` - Client-side routing
- `zustand` - State management
- `framer-motion` - Animations
- `recharts` - Data visualization
- `lucide-react` - Icon library
- `react-dnd` - Drag-and-drop (for drag-order exercises)
- `tailwindcss` - Utility-first CSS
- `@radix-ui/*` - Accessible UI primitives (via shadcn/ui)

### Lovable Platform
- Project URL: https://lovable.dev/projects/46d2181b-ace3-4886-b550-bc9746762717
- Deployment: Via Lovable dashboard (Share → Publish)
- Component Tagging: Enabled in dev mode via `lovable-tagger` plugin

## Path Conventions
- Use `@/` import alias for all internal imports (e.g., `@/components/ui/button`)
- Absolute paths in configs: `src/components`, not `./components`
- File references in docs: Use markdown links `[file.ts](src/file.ts)` or `file.ts:line` format

## Content Generation Workflow
1. Create chapter JSON files in `chapters/` directory (naming: `{subject}-*.json`)
2. Run integration script to merge into `src/data/content.json`
3. Auto-backup created as `content-backup-{timestamp}.json`
4. Test in dev mode with `npm run dev`
5. Validate JSON with `npx jsonlint src/data/content.json`
6. Commit only after manual verification
