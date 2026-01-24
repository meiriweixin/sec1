/**
 * Unified Content Data Export
 * Merges all content sources into a single export
 */

import baseContent from './content.json';
import sec2ScienceContent from './sec2-science.json';

// Merge subjects from all content sources
const contentData = {
    subjects: [
        ...baseContent.subjects,
        ...sec2ScienceContent.subjects,
    ],
};

export default contentData;
