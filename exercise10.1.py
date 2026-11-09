from pathlib import Path

path = Path('exercise10_1.txt')
contents = path.read_text()

print("Reading entire file:")
print(contents)

print("\nReading line by line:")
lines = contents.splitlines()
for line in lines:
    print(line)