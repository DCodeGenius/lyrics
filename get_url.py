#url = "https://genius.com/Drake-gods-plan-lyrics"
def url_name():
    url = "https://genius.com/"
    artist = input("Enter the artist's name: ")
    song = input("Enter the song's name: ")
    artist_song =  artist + " " + song
    artist_song = '-'.join(artist_song.split())
    url += artist_song + "-lyrics"
    return url