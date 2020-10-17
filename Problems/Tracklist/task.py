def tracklist(**artists):
    for artist, album in artists.items():
        print(artist)
        for album_name, track in album.items():
            print("ALBUM:", album_name, "TRACK:", track)
