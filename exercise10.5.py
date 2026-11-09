from pathlib import Path

path = Path('guest_book.txt')
names = []

while True:
    name = input("Enter your name (or 'quit' to finish): ")
    if name == 'quit':
        break
    names.append(name)
    print(f"Welcome, {name}!")

contents = "\n".join(names)
path.write_text(contents)
print(f"\n{len(names)} name(s) saved to guest_book.txt.")