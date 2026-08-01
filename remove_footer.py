import os
import glob
import re

files = glob.glob('src/pages/*.vue')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove <!-- Footer --> if it exists and the whole footer block
    new_content = re.sub(r'(\s*<!-- Footer -->)?\s*<footer[\s\S]*?</footer>', '', content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
