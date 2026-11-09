from pathlib import Path

path = Path('exercise10_1.txt')
contents = path.read_text()

print("Reading entire file:")
print(contents)

print("\nReading line by line:")
for line in contents.splitlines():
    print(line)