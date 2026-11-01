buffet = ('nasi goreng', 'mie goreng', 'sate', 'gado-gado', 'rendang')
for food in buffet:
    print(food)

# buffet[0] = 'pizza'  # TypeError: 'tuple' object does not support item assignment

print("\nMenu has changed:")
buffet = ('kwetiaw', 'capcay', 'ayam goreng', 'dimsum', 'nasi padang')
for food in buffet:
    print(food)