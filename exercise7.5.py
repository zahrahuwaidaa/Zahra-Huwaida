prompt = "\nHow old are you? (enter 'quit' to finish): "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("The ticket is free.")
    elif age <= 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")