from pathlib import Path

path = Path('exercise10_1.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    modified = line.replace('Python', 'C')
    print(modified)