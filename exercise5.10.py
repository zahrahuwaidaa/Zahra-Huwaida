current_users = ['John', 'Mary', 'Steve', 'Lina', 'Admin']
new_users = ['JOHN', 'lina', 'Peter', 'Grace', 'ADMIN']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' already used. Please choose a different username.")
    else:
        print(f"Username '{new_user}' is available.")