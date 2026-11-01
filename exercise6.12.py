favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    'mike': ['java', 'kotlin'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is {languages[0].title()}.")
    else:
        print(f"\n{name.title()}'s favorite languages are:")