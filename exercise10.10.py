from pathlib import Path

filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        count = contents.lower().count('the')
        print(f"{filename} contains the word 'the' approximately {count} times.")