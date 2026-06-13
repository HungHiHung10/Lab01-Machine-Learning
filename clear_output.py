import json
import glob
import os

for f in glob.glob('notebooks/*.ipynb'):
    print(f"Processing {f}...")
    try:
        with open(f, 'r', encoding='utf-8') as file:
            nb = json.load(file)
            
        for cell in nb.get('cells', []):
            if 'outputs' in cell:
                cell['outputs'] = []
            if 'execution_count' in cell:
                cell['execution_count'] = None
                
        with open(f, 'w', encoding='utf-8') as file:
            json.dump(nb, file, indent=1)
        print(f"Successfully cleared {f}")
    except Exception as e:
        print(f"Error processing {f}: {e}")
