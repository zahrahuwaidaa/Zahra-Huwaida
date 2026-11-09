from pathlib import Path

filenames = ['exercise10_8_1.cats.txt', 'exercise10_8_2.dogs.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        print(f"\nContents of {filename}:")
        print(contents.rstrip())