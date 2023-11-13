from songs import find_by_artist, display_song_names, alphebatize, tracks_from_year, songs


def test_find_by_artist():
    matching_songs = find_by_artist(songs, 'Aretha Franklin')
    matching_songs_2 = find_by_artist(songs, 'Bob Dylan')
    assert matching_songs == ['Respect']
    assert matching_songs_2 == ['Like a Rolling Stone']


def test_display_song_names():
    song_names = display_song_names(songs)
    assert song_names == ['Like a Rolling Stone', 'Satisfaction', 'Respect']


def test_alphebatize():
    test_1  = alphebatize(songs[:2])
    test_2  = alphebatize(songs[2:])

    assert test_1 == sorted(test_1)
    assert test_2 == sorted(test_2)


def test_tracks_from_year():
    test_1 = tracks_from_year(songs,1965)
    assert test_1 == ['Like a Rolling Stone', 'Satisfaction']



    
