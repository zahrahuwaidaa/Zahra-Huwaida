sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'ham', 'pastrami', 'veggie']
finished_sandwiches = []

print("Sorry, we've run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")