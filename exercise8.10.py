def show_messages(messages):
    """Print each message."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

messages = ['Hello!', 'How are you?', 'Goodbye!']
sent_messages = []

send_messages(messages, sent_messages)

print(f"\nOriginal list: {messages}")
print(f"Sent messages: {sent_messages}")