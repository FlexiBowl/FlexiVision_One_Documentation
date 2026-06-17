from pathlib import Path
import re

base = Path('sources') / 'V. 0.20' / 'EN'
changed_files = []

for path in sorted(base.rglob('*.md')):
    text = path.read_text(encoding='utf-8')
    orig = text

    # normalize directive fences and list-table markers
    text = re.sub(r'(?m)^[ \t]*`{1,3}\{([^}]+)\}', r'```{\1}', text)
    text = re.sub(r'(?m)^`{4,}\s*$', '```', text)

    # fix list-table rows corrupted by translation
    text = re.sub(r'(?m)^([ \t]*)\* - \* - (Category|Parameter|Command)\b', r'\1* - \2', text)
    text = re.sub(r'(?m)^([ \t]*)\* -\s*\*\s*-\s*(Category|Parameter|Command)\b', r'\1* - \2', text)

    # remove duplicate header/width blocks left by broken translations
    text = re.sub(
        r'(?ms)^([ \t]*```\{list-table\}\n(?:[ \t]*:header-rows:.*\n)+[ \t]*:widths:.*\n\n)[ \t]*\* - \* - (Category|Parameter|Command)\n(?:[ \t]*:header-rows:.*\n)+[ \t]*:widths:.*\n\n',
        r'\1* - \2\n',
        text
    )

    # fix inline merged list-table rows
    text = re.sub(r'(?m)([^\n])\s+\* - ', r'\1\n* - ', text)

    # fix figure/note directive indentation inside list items
    text = re.sub(r'(?m)^([ \t]*):::\{figure\}', r'\1    :::{figure}', text)
    text = re.sub(r'(?m)^([ \t]*):::\{note\}', r'\1    :::{note}', text)

    # fix stray trailing triple backticks attached to text
    text = re.sub(r'(?m)([^\n])\s*```$', r'\1\n```', text)

    # fix a common broken Unboxing table creation line
    text = text.replace(
        '* - Component  - Technical Specifications  - Image  * - Camera  - Go to Camera Specifications',
        '```{list-table}\n:header-rows: 1\n:widths: 30 40 35\n\n* - **Component**\n  - **Technical Specifications**\n  - **Image**\n* - Camera\n  - [Go to Camera Specifications](specifiche_camera)'
    )

    if text != orig:
        path.write_text(text, encoding='utf-8')
        changed_files.append(str(path))

print(f'changed {len(changed_files)} files')
for p in changed_files:
    print(p)
