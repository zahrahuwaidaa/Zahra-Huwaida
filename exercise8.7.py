def make_album(artist, title, num_songs=None):
    """Build a dictionary describing a music album."""
    album = {'artist': artist, 'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

print(make_album('tame impala', 'currents'))
print(make_album('daft punk', 'random access memories'))
print(make_album('radiohead', 'ok computer'))
print(make_album('the beatles', 'abbey road', 17))