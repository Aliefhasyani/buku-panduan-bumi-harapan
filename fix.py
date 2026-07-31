import glob

for f in glob.glob('src/pages/*.vue'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # The literal is probably backtick-n since it was replaced using PowerShell
    content = content.replace("`n          <strong", "\n          <strong")
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Done')
