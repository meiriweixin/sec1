import re

with open('chapters/sec1_adaptations_chapter.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all quotes in the file
quote_pattern = r'["\'""]'
matches = [(m.start(), m.group()) for m in re.finditer(quote_pattern, content)]

# Focus on the area around char 17577
error_pos = 17577
nearby_quotes = [(pos, char) for pos, char in matches if abs(pos - error_pos) < 500]

print(f"Quotes near error position (char {error_pos}):")
for pos, char in nearby_quotes:
    context_start = max(0, pos - 20)
    context_end = min(len(content), pos + 20)
    print(f"  Pos {pos}: {repr(char)} - Context: {repr(content[context_start:context_end])}")
