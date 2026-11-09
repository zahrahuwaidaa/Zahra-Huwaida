# Kunjungi https://pymotw.com dan pelajari modul random.
from random import randint, choice

print("Random integers:")
for _ in range(5):
    print(randint(1, 100))

print("\nRandom choices from a list:")
colors = ['red', 'green', 'blue', 'yellow']
for _ in range(3):
    print(choice(colors))