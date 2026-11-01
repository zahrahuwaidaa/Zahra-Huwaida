# Test 1: equality & inequality with strings
fruit = 'apple'
print(fruit == 'apple')   # True
print(fruit != 'banana')  # True

# Test 2: lower()
print('Apple'.lower() == 'apple')  # True

# Test 3: numerical tests
age = 20
print(age == 20)   # True
print(age != 20)   # False
print(age > 18)    # True
print(age < 18)    # False
print(age >= 20)   # True
print(age <= 20)   # True

# Test 4: and / or
print(age > 18 and age < 30)  # True
print(age > 18 or age > 30)   # True

# Test 5: item in list
fruits = ['apple', 'banana', 'cherry']
print('apple' in fruits)     # True

# Test 6: item not in list
print('grape' not in fruits) # True