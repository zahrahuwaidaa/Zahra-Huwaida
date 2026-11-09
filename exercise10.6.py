print("Enter two numbers and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first = input("\nFirst number: ")
    if first == 'q':
        break
    second = input("Second number: ")
    if second == 'q':
        break

    try:
        result = int(first) + int(second)
    except ValueError:
        print("Please enter only numbers!")
    else:
        print(f"{first} + {second} = {result}")