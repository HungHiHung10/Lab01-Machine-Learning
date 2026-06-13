import json

emojis_to_remove = ['✅', '❌', '🎬', '⚠️', '⚠', '📁', '📍', '📊']

file_path = r'a:\Lab01-Machine-Learning\notebooks\Slide81_126.ipynb'

with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        source = cell.get('source', [])
        new_source = []
        for line in source:
            for emoji in emojis_to_remove:
                # Replace emoji followed by a space first, to avoid double spaces
                line = line.replace(emoji + ' ', '')
                # Replace any remaining standalone emojis
                line = line.replace(emoji, '')
            new_source.append(line)
        cell['source'] = new_source

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Icons removed successfully!")
