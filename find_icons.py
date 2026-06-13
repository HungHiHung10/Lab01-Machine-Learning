import json

def has_emoji(text):
    for char in text:
        if 0x1F600 <= ord(char) <= 0x1F64F \
        or 0x1F300 <= ord(char) <= 0x1F5FF \
        or 0x1F680 <= ord(char) <= 0x1F6FF \
        or 0x1F700 <= ord(char) <= 0x1F77F \
        or 0x1F780 <= ord(char) <= 0x1F7FF \
        or 0x1F800 <= ord(char) <= 0x1F8FF \
        or 0x1F900 <= ord(char) <= 0x1F9FF \
        or 0x1FA00 <= ord(char) <= 0x1FA6F \
        or 0x1FA70 <= ord(char) <= 0x1FAFF \
        or 0x2600 <= ord(char) <= 0x26FF \
        or 0x2700 <= ord(char) <= 0x27BF \
        or char == '✅':
            return True
    return False

with open(r'a:\Lab01-Machine-Learning\notebooks\Slide81_126.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open('icons.txt', 'w', encoding='utf-8') as out:
    out.write("Found the following cells with emojis/icons:\n")
    for i, cell in enumerate(nb.get('cells', [])):
        if cell.get('cell_type') == 'code':
            source = "".join(cell.get('source', []))
            if has_emoji(source):
                out.write(f"\n--- Code Cell #{i} ---\n")
                lines = source.split('\n')
                for line in lines:
                    if has_emoji(line):
                        out.write(f"  {line.strip()}\n")
