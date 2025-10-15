// Script to integrate an expanded chapter into content.json
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Read the main content.json
const contentPath = path.join(__dirname, 'src', 'data', 'content.json');
const content = JSON.parse(fs.readFileSync(contentPath, 'utf8'));

// Read the expanded Forces & Motion chapter
const expandedChapterPath = path.join(__dirname, 'expanded-chapters', '05-forces-motion.json');
const expandedChapter = JSON.parse(fs.readFileSync(expandedChapterPath, 'utf8'));

// Find the science subject
const scienceSubject = content.subjects.find(s => s.id === 'science');

if (!scienceSubject) {
  console.error('❌ Science subject not found!');
  process.exit(1);
}

// Find the index of forces-motion chapter
const chapterIndex = scienceSubject.chapters.findIndex(c => c.id === 'forces-motion');

if (chapterIndex === -1) {
  console.error('❌ Forces & Motion chapter not found!');
  process.exit(1);
}

console.log('📖 Found Forces & Motion chapter at index:', chapterIndex);
console.log('📊 Current chapter has:');
console.log(`   - ${scienceSubject.chapters[chapterIndex].sections.length} sections`);
console.log(`   - ${scienceSubject.chapters[chapterIndex].exercises.length} exercises`);

console.log('\n📊 Expanded chapter has:');
console.log(`   - ${expandedChapter.sections.length} sections`);
console.log(`   - ${expandedChapter.exercises.length} exercises`);

// Replace the chapter
scienceSubject.chapters[chapterIndex] = expandedChapter;

// Create backup of original
const backupPath = path.join(__dirname, 'src', 'data', 'content-backup-' + Date.now() + '.json');
fs.writeFileSync(backupPath, fs.readFileSync(contentPath, 'utf8'));
console.log('\n💾 Backup created:', path.basename(backupPath));

// Write the updated content
fs.writeFileSync(contentPath, JSON.stringify(content, null, 2));
console.log('✅ Successfully integrated Forces & Motion chapter!');
console.log('\n🎯 Next steps:');
console.log('   1. Run: npm run dev');
console.log('   2. Navigate to Science > Forces & Motion');
console.log('   3. You should now see 7 lesson sections and 12 exercises!');
