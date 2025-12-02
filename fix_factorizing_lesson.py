#!/usr/bin/env python3
"""
Fix Factorizing Expressions lesson formatting
"""

import json
import shutil
from datetime import datetime

def main():
    content_file = 'src/data/content.json'

    # Create backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f'src/data/content-backup-formatting-{timestamp}.json'
    shutil.copy(content_file, backup_file)
    print(f"Created backup: {backup_file}")

    # Load content
    with open(content_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Find and fix the Factorizing Expressions section
    for subject in data['subjects']:
        if subject['id'] == 'math':
            for chapter in subject['chapters']:
                if chapter['id'] == 'algebraic-expressions':
                    for section in chapter['sections']:
                        if section['id'] == 'factorizing':
                            # Fix English content
                            section['content'] = """Factorizing is **REVERSE** of expanding - take out common factors.

**Steps:**

1. Find **HCF** (Highest Common Factor) of all terms
2. Write **HCF** outside brackets
3. Divide each term by **HCF**
4. Check by expanding

**Example:**

Factorize 6x + 9

- **HCF** = 3
- Answer: 3(2x + 3)
- Check: 3(2x + 3) = 6x + 9 ✓"""

                            # Fix Chinese content
                            section['content_zh'] = """因式分解是展开的**逆过程** - 提取公因数。

**步骤：**

1. 找出所有项的**最大公因数（HCF）**
2. 将 **HCF** 写在括号外
3. 每项除以 **HCF**
4. 通过展开检查

**例子：**

因式分解 6x + 9

- **HCF** = 3
- 答案：3(2x + 3)
- 检查：3(2x + 3) = 6x + 9 ✓"""

                            print("✓ Fixed: Factorizing Expressions")

                        elif section['id'] == 'substitution':
                            # Fix substitution section too
                            section['content'] = """Substitution means replacing variables with numbers.

**Steps:**

1. Write the expression
2. Replace variables (use brackets for clarity!)
3. Follow order of operations (PEMDAS)
4. Calculate the result

**Example:**

Evaluate 3x + 5 when x = 4

- Answer: 3(4) + 5 = 12 + 5 = 17

**Important:** Always use brackets when substituting negative numbers!"""

                            section['content_zh'] = """代入意味着用数字替换变量。

**步骤：**

1. 写出表达式
2. 替换变量（使用括号以清晰！）
3. 遵循运算顺序
4. 计算结果

**例子：**

当 x = 4 时求值 3x + 5

- 答案：3(4) + 5 = 12 + 5 = 17

**重要：** 代入负数时始终使用括号！"""

                            print("✓ Fixed: Substitution and Evaluation")

    # Save updated content
    with open(content_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Formatting fixed!")
    print(f"Backup saved to: {backup_file}")
    print(f"Updated file:    {content_file}")

if __name__ == '__main__':
    main()
