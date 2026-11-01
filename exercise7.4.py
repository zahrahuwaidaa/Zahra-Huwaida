prompt = "\nEnter a pizza topping (or 'quit' to finish): "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")