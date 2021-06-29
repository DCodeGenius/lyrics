#url = "https://genius.com/Drake-gods-plan-lyrics"
def url_name(artist, song):
    url = "https://genius.com/"
    artist = artist
    song = song
    artist_song =  artist + " " + song
    artist_song = '-'.join(artist_song.split())
    url += artist_song + "-lyrics"
    return url
