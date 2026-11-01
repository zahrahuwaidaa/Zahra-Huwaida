def make_album(artist, title):
    """Build a dictionary describing a music album."""
    return {'artist': artist, 'title': title}

while True:
    print("\nEnter album details (or 'q' to quit):")
    artist = input("Artist: ")
    if artist == 'q':
        break
    title = input("Album title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)