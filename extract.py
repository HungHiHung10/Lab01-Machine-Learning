import json
import glob
import os

with open('output.txt', 'w', encoding='utf-8') as out:
    for f in glob.glob('*.ipynb'):
        out.write(f'\n--- {f} ---\n')
        try:
            with open(f, 'r', encoding='utf-8') as file:
                nb = json.load(file)
                for cell in nb.get('cells', []):
                    if cell.get('cell_type') == 'markdown':
                        src = cell.get('source', [])
                        src_str = ''.join(src) if isinstance(src, list) else src
                        if src_str.strip().startswith('#'):
                            out.write('  ' + src_str.strip().split('\n')[0][:100] + '\n')
        except Exception as e:
            out.write(f"Error reading {f}: {e}\n")
