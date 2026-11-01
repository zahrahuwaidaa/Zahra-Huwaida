guests = ['Albert Einstein', 'Marie Curie', 'Isaac Newton']
print(" I just found a bigger dinner table, so now more space is available!")

guests.insert(0, 'Stephen Hawking')
guests.insert(2, 'Nikola Tesla')
guests.append('Galileo Galilei')

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")