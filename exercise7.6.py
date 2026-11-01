# Versi 1: conditional test in while statement
print("--- Version 1: conditional test ---")
age = ''
while age != 'quit':
    age = input("How old are you? ('quit' to finish): ")
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("Free")
        elif age <= 12:
            print("$10")
        else:
            print("$15")

# Versi 2: active variable
print("\n--- Version 2: active variable ---")
active = True
while active:
    age = input("How old are you? ('quit' to finish): ")
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Free")
        elif age <= 12:
            print("$10")
        else:
            print("$15")

# Versi 3: break statement
print("\n--- Version 3: break ---")
while True:
    age = input("How old are you? ('quit' to finish): ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Free")
    elif age <= 12:
        print("$10")
    else:
        print("$15")