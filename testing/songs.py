songs = [{'rank': 1, 'song': 'Like a Rolling Stone', 'artist': 'Bob Dylan', 'year': 1965},
         {'rank': 2, 'song': 'Satisfaction', 'artist': 'The Rolling Stones', 'year': 1965},
         {'rank': 5, 'song': 'Respect', 'artist': 'Aretha Franklin', 'year': 1967}]

def find_by_artist(songs, artist_name):
    return [song['song'] for song in songs if song['artist'] == artist_name]

def display_song_names(songs):
    return [song['song'] for song in songs]

def alphebatize(songs):
    return sorted(display_song_names(songs))

def tracks_from_year(song_list, year):
    return [song['song'] for song in song_list if song['year'] == year]
