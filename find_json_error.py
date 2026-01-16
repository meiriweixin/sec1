with open('chapters/sec1_adaptations_chapter.json', 'r', encoding='utf-8') as f:
    content = f.read()
    
# Error at char 17577
error_pos = 17577
start = max(0, error_pos - 100)
end = min(len(content), error_pos + 100)

print(f"Content around error position (char {error_pos}):")
print("=" * 80)
print(content[start:end])
print("=" * 80)
print(f"\nExact character at position {error_pos}: '{content[error_pos]}'")
print(f"Context: ...{content[error_pos-10:error_pos+10]}...")
