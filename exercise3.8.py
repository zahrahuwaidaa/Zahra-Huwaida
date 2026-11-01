places = ['Tokyo', 'Paris', 'New York', 'Reykjavik', 'Cairo']
print("Original:", places)

print("\nSorted:", sorted(places))
print("Original still:", places)

print("\nReverse sorted:", sorted(places, reverse=True))
print("Original still:", places)

places.reverse()
print("\nAfter reverse():", places)
places.reverse()
print("After reverse() again:", places)

places.sort()
print("\nAfter sort():", places)
places.sort(reverse=True)
print("After sort(reverse=True):", places)