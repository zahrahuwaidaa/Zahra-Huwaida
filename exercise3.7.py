guests = ['Stephen Hawking', 'Albert Einstein', 'Nikola Tesla',
          'Marie Curie', 'Isaac Newton', 'Galileo Galilei']
print(" Sorry, I just found out that the new dinner table won't arrive in time for the dinner, and I have space for only two guests.")

while len(guests) > 2:
    removed = guests.pop()
    print(f"Sorry {removed}, I can't invite you to dinner.")

for guest in guests:
    print(f"{guest}, you're still invited to dinner.")

del guests[0]
del guests[0]
print(guests)