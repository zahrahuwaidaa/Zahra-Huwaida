mountains = ['Everest', 'Kilimanjaro', 'Fuji', 'Denali', 'Elbrus']
print(mountains)

mountains.append('Matterhorn')
print(mountains)

mountains.insert(0, 'Annapurna')
print(mountains)

del mountains[0]
print(mountains)

popped = mountains.pop()
print(f"Poppped: {popped}")
print(mountains)

mountains.remove('Fuji')
print(mountains)

mountains.sort()
print(mountains)

print(sorted(mountains, reverse=True))
print(sorted(mountains))

mountains.reverse()
print(mountains)

print(len(mountains))