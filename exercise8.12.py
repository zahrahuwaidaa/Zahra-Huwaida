def make_sandwich(*items):
    """Summarize the sandwich being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('ham')
make_sandwich('turkey', 'cheese')
make_sandwich('beef', 'lettuce', 'tomato', 'mayo')