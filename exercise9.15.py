from random import choice

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

my_ticket = ['a', 3, 7, 'e']

def generate_ticket(pool):
    """Generate a winning ticket of 4 unique items."""
    ticket = []
    while len(ticket) < 4:
        pick = choice(pool)
        if pick not in ticket:
            ticket.append(pick)
    return ticket

attempts = 0
while True:
    attempts += 1
    new_ticket = generate_ticket(lottery_pool)
    if new_ticket == my_ticket:
        break

print(f"Your ticket: {my_ticket}")
print(f"Winning ticket found after {attempts} attempts!")