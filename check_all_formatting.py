#!/usr/bin/env python3
"""
Check all lesson content for formatting issues
Identifies broken markdown, missing line breaks, malformed content
"""

import json
import re

def check_content_formatting(content, title):
    """Check content for common formatting issues"""
    issues = []

    if not content:
        return issues

    # Check for broken bold markdown (** without spaces)
    if re.search(r'\*\*[A-Z][a-z]+\*\*[a-z]', content):
        issues.append("Broken bold: ** followed by text without space")

    # Check for step numbers without content (e.g., "1.\n\nFind")
    if re.search(r'\d+\.\n\n[A-Z]', content):
        issues.append("Step number separated from content")

    # Check for missing line breaks between sentences
    if re.search(r'\.\n[A-Z]', content) and '\n\n' not in content:
        issues.append("Missing paragraph breaks (single \\n instead of \\n\\n)")

    # Check for steps that look malformed
    if 'Steps:' in content or '步骤' in content:
        # Should have numbered list after Steps:
        if not re.search(r'Steps:\*\*\n\n\d+\.', content) and not re.search(r'步骤：\*\*\n\n\d+', content):
            if re.search(r'Steps.*\n\n1\.\n\n', content) or re.search(r'Steps.*\d+\.\n\n[A-Z]', content):
                issues.append("Malformed steps: number separated from description")

    # Check for example sections
    if 'Example:' in content or '例子' in content:
        # Should have proper formatting
        if re.search(r'Example:\*\*\n\n [A-Z]', content):
            issues.append("Extra space after Example:**")

    # Check for periods followed by capitals without space
    if re.search(r'\.\n[0-9A-Z][a-z]', content) and 'Dr.' not in content:
        issues.append("Period followed by capital without paragraph break")

    return issues

def main():
    content_file = 'src/data/content.json'

    # Load content
    with open(content_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_sections = 0
    total_issues = 0
    issues_by_subject = {}

    print("="*80)
    print("CHECKING ALL LESSON CONTENT FOR FORMATTING ISSUES")
    print("="*80)
    print()

    # Check all subjects and chapters
    for subject in data['subjects']:
        subject_name = subject.get('title', 'Unknown')
        subject_issues = []

        for chapter in subject.get('chapters', []):
            chapter_name = chapter.get('title', 'Unknown')

            for section in chapter.get('sections', []):
                total_sections += 1
                section_title = section.get('title', 'Unknown')
                section_id = section.get('id', 'unknown')

                # Check English content
                if 'content' in section:
                    issues = check_content_formatting(section['content'], section_title)
                    if issues:
                        subject_issues.append({
                            'chapter': chapter_name,
                            'section': section_title,
                            'id': section_id,
                            'language': 'English',
                            'issues': issues
                        })
                        total_issues += len(issues)

                # Check Chinese content
                if 'content_zh' in section:
                    issues = check_content_formatting(section['content_zh'], section_title)
                    if issues:
                        subject_issues.append({
                            'chapter': chapter_name,
                            'section': section_title,
                            'id': section_id,
                            'language': 'Chinese',
                            'issues': issues
                        })
                        total_issues += len(issues)

        if subject_issues:
            issues_by_subject[subject_name] = subject_issues

    # Print results
    if issues_by_subject:
        print(f"⚠️  FOUND {total_issues} FORMATTING ISSUES IN {len(issues_by_subject)} SUBJECTS")
        print()

        for subject_name, issues_list in issues_by_subject.items():
            print(f"\n📚 {subject_name}")
            print("-" * 80)

            for item in issues_list:
                print(f"\n  Chapter: {item['chapter']}")
                print(f"  Section: {item['section']} ({item['id']})")
                print(f"  Language: {item['language']}")
                print(f"  Issues:")
                for issue in item['issues']:
                    print(f"    • {issue}")
    else:
        print("✅ NO FORMATTING ISSUES FOUND!")

    print("\n" + "="*80)
    print(f"Total sections checked: {total_sections}")
    print(f"Sections with issues: {len([i for issues in issues_by_subject.values() for i in issues])}")
    print(f"Total issues found: {total_issues}")
    print("="*80)

    # Show sample of problematic content
    if issues_by_subject:
        print("\n📋 SAMPLE PROBLEMATIC CONTENT:")
        print("-" * 80)

        with open(content_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        shown_samples = 0
        for subject in data['subjects']:
            if shown_samples >= 3:
                break

            subject_name = subject.get('title', 'Unknown')
            if subject_name not in issues_by_subject:
                continue

            for chapter in subject.get('chapters', []):
                if shown_samples >= 3:
                    break

                for section in chapter.get('sections', []):
                    if shown_samples >= 3:
                        break

                    section_id = section.get('id', '')

                    # Check if this section has issues
                    for item in issues_by_subject[subject_name]:
                        if item['id'] == section_id and item['language'] == 'English':
                            print(f"\n{subject_name} > {chapter.get('title')} > {section.get('title')}")
                            print(f"Content preview (first 300 chars):")
                            print("-" * 40)
                            content = section.get('content', '')
                            print(content[:300])
                            print("-" * 40)
                            shown_samples += 1
                            break

if __name__ == '__main__':
    main()
