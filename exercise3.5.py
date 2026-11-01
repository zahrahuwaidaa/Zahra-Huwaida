guests = ['Albert Einstein', 'Marie Curie', 'Isaac Newton']
print(f"{guests[1]} can't make it to dinner.")

guests[1] = 'Nikola Tesla'

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")