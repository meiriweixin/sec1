const fs = require('fs');

// Read content.json
const data = JSON.parse(fs.readFileSync('src/data/content.json', 'utf8'));

const analysis = {
  totalChapters: 0,
  bySubject: {},
  chaptersCorrect: [],
  chaptersNeedUpdate: [],
  summary: {}
};

// Function to analyze section structure
function analyzeChapter(subject, chapter) {
  const result = {
    subjectTitle: subject.title,
    subjectId: subject.id,
    chapterId: chapter.id,
    chapterTitle: chapter.title,
    totalSections: chapter.sections.length,
    sectionTypes: [],
    hasConceptExamplePattern: false,
    issues: [],
    currentStructure: []
  };

  // Map section types
  chapter.sections.forEach((section, idx) => {
    result.sectionTypes.push(section.type);
    result.currentStructure.push({
      index: idx,
      type: section.type,
      contentPreview: section.type === 'text'
        ? section.content.substring(0, 100)
        : section.content,
      hasTitle: !!section.title
    });
  });

  // Check for concept + example pattern
  // Pattern: text sections followed by example/animation sections
  let hasTextSections = result.sectionTypes.includes('text');
  let hasExampleSections = result.sectionTypes.includes('example');
  let hasAnimations = result.sectionTypes.includes('animation');

  // Analyze structure pattern
  let textCount = result.sectionTypes.filter(t => t === 'text').length;
  let exampleCount = result.sectionTypes.filter(t => t === 'example').length;
  let animationCount = result.sectionTypes.filter(t => t === 'animation').length;
  let mathCount = result.sectionTypes.filter(t => t === 'math').length;

  result.counts = {
    text: textCount,
    example: exampleCount,
    animation: animationCount,
    math: mathCount
  };

  // Check if structure follows concept + example pattern
  // Look for alternating or grouped text->example/animation patterns
  let lastTextIndex = -1;
  let hasProperPairing = true;
  let conceptsWithoutExamples = 0;

  for (let i = 0; i < chapter.sections.length; i++) {
    const section = chapter.sections[i];

    if (section.type === 'text') {
      lastTextIndex = i;
      // Check if next section is example or animation
      if (i + 1 < chapter.sections.length) {
        const nextSection = chapter.sections[i + 1];
        if (nextSection.type !== 'example' && nextSection.type !== 'animation' && nextSection.type !== 'math') {
          conceptsWithoutExamples++;
        }
      } else {
        // Last section is text without example
        conceptsWithoutExamples++;
      }
    }
  }

  // Determine if chapter needs updating
  if (exampleCount === 0 && animationCount === 0 && mathCount === 0) {
    result.issues.push('No example, animation, or math sections found');
    result.hasConceptExamplePattern = false;
  } else if (conceptsWithoutExamples > 0) {
    result.issues.push(`${conceptsWithoutExamples} text section(s) without following examples`);
    result.hasConceptExamplePattern = false;
  } else {
    result.hasConceptExamplePattern = true;
  }

  // Additional checks
  if (textCount === 0) {
    result.issues.push('No text/concept sections found');
  }

  if (result.sectionTypes.length < 2) {
    result.issues.push('Only 1 section - needs more content');
  }

  return result;
}

// Analyze all subjects and chapters
data.subjects.forEach(subject => {
  if (subject.id === 'ai-playground') return; // Skip AI Playground

  analysis.bySubject[subject.title] = {
    subjectId: subject.id,
    totalChapters: subject.chapters.length,
    correct: [],
    needUpdate: []
  };

  subject.chapters.forEach(chapter => {
    analysis.totalChapters++;
    const chapterAnalysis = analyzeChapter(subject, chapter);

    if (chapterAnalysis.hasConceptExamplePattern && chapterAnalysis.issues.length === 0) {
      analysis.chaptersCorrect.push(chapterAnalysis);
      analysis.bySubject[subject.title].correct.push({
        id: chapter.id,
        title: chapter.title,
        sections: chapterAnalysis.totalSections
      });
    } else {
      analysis.chaptersNeedUpdate.push(chapterAnalysis);
      analysis.bySubject[subject.title].needUpdate.push({
        id: chapter.id,
        title: chapter.title,
        issues: chapterAnalysis.issues,
        counts: chapterAnalysis.counts,
        structure: chapterAnalysis.currentStructure
      });
    }
  });
});

// Generate summary
analysis.summary = {
  totalChapters: analysis.totalChapters,
  chaptersCorrect: analysis.chaptersCorrect.length,
  chaptersNeedUpdate: analysis.chaptersNeedUpdate.length,
  percentageCorrect: ((analysis.chaptersCorrect.length / analysis.totalChapters) * 100).toFixed(1) + '%'
};

// Output detailed report
console.log('='.repeat(80));
console.log('COMPREHENSIVE CHAPTER STRUCTURE ANALYSIS');
console.log('='.repeat(80));
console.log('\n📊 SUMMARY');
console.log('-'.repeat(80));
console.log(`Total Chapters Analyzed: ${analysis.summary.totalChapters}`);
console.log(`Chapters with Correct Structure: ${analysis.summary.chaptersCorrect} (${analysis.summary.percentageCorrect})`);
console.log(`Chapters Needing Updates: ${analysis.summary.chaptersNeedUpdate}`);
console.log('\n');

// Report by subject
console.log('📚 BY SUBJECT');
console.log('-'.repeat(80));
Object.keys(analysis.bySubject).forEach(subjectTitle => {
  const subject = analysis.bySubject[subjectTitle];
  console.log(`\n${subjectTitle.toUpperCase()}`);
  console.log(`  Total: ${subject.totalChapters} chapters`);
  console.log(`  ✅ Correct: ${subject.correct.length}`);
  console.log(`  ⚠️  Need Update: ${subject.needUpdate.length}`);
});

console.log('\n\n');
console.log('✅ CHAPTERS WITH CORRECT STRUCTURE (SKIP THESE)');
console.log('='.repeat(80));

Object.keys(analysis.bySubject).forEach(subjectTitle => {
  const subject = analysis.bySubject[subjectTitle];
  if (subject.correct.length > 0) {
    console.log(`\n${subjectTitle.toUpperCase()}`);
    subject.correct.forEach(ch => {
      console.log(`  ✓ ${ch.id}: ${ch.title} (${ch.sections} sections)`);
    });
  }
});

console.log('\n\n');
console.log('⚠️  CHAPTERS NEEDING UPDATES');
console.log('='.repeat(80));

Object.keys(analysis.bySubject).forEach(subjectTitle => {
  const subject = analysis.bySubject[subjectTitle];
  if (subject.needUpdate.length > 0) {
    console.log(`\n${'━'.repeat(80)}`);
    console.log(`${subjectTitle.toUpperCase()}`);
    console.log('━'.repeat(80));

    subject.needUpdate.forEach((ch, idx) => {
      console.log(`\n${idx + 1}. ${ch.id}: ${ch.title}`);
      console.log(`   Issues:`);
      ch.issues.forEach(issue => {
        console.log(`     • ${issue}`);
      });
      console.log(`   Current Content:`);
      console.log(`     - Text sections: ${ch.counts.text}`);
      console.log(`     - Example sections: ${ch.counts.example}`);
      console.log(`     - Animation sections: ${ch.counts.animation}`);
      console.log(`     - Math sections: ${ch.counts.math}`);
      console.log(`   Structure:`);
      ch.structure.forEach(s => {
        const preview = s.type === 'text' ? ' - ' + s.contentPreview.substring(0, 60) + '...' : '';
        console.log(`     [${s.index}] ${s.type}${preview}`);
      });
    });
  }
});

console.log('\n\n');
console.log('💡 RECOMMENDED ACTIONS');
console.log('='.repeat(80));

Object.keys(analysis.bySubject).forEach(subjectTitle => {
  const subject = analysis.bySubject[subjectTitle];
  if (subject.needUpdate.length > 0) {
    console.log(`\n${subjectTitle}:`);
    subject.needUpdate.forEach(ch => {
      console.log(`\n  ${ch.id} - ${ch.title}:`);

      if (ch.counts.example === 0 && ch.counts.animation === 0 && ch.counts.math === 0) {
        console.log(`    → Add example sections after each text/concept section`);
        console.log(`    → Suggested structure: [text] → [example] → [text] → [example] ...`);
      } else if (ch.issues.includes('text section(s) without following examples')) {
        console.log(`    → Reorder sections to pair concepts with examples`);
        console.log(`    → Each text section should be followed by example/animation/math`);
      }

      if (ch.counts.text === 0) {
        console.log(`    → Add text/concept sections to explain topics`);
      }

      if (ch.structure.length < 2) {
        console.log(`    → Expand content with more sections (minimum 2-3 concept+example pairs)`);
      }
    });
  }
});

console.log('\n\n');
console.log('📋 DETAILED ANALYSIS SAVED');
console.log('='.repeat(80));

// Save detailed JSON report
fs.writeFileSync('chapter-analysis-report.json', JSON.stringify(analysis, null, 2));
console.log('Full analysis saved to: chapter-analysis-report.json');
console.log('\nAnalysis complete! ✨');
