sandwich_orders = ['tuna', 'ham', 'turkey', 'veggie']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")