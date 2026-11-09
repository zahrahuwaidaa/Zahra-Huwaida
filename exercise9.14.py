from random import choice

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
while len(winning_ticket) < 4:
    pick = choice(lottery_pool)
    if pick not in winning_ticket:
        winning_ticket.append(pick)

print("Any ticket matching these 4 numbers or letters wins a prize:")
print(winning_ticket)