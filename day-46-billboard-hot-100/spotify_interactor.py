import spotipy
import sys 
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from pprint import pprint 
from billboard_getter import get_billboard_top100


if __name__ == '__main__':
    print("We provide service of travelling back with how music at a specific data")
    date = input("What it the day you want to trace back to?(seperated by -, e.g. 2000-09-02)\n")
    input(f"OK, so you want to travel back to: {date} \n(press any button to continue)\n")
    playlist_name = f"Billboard-top100-{date}"
    year = date.split("-")[0]
    singer2song = get_billboard_top100(date)

    scope = "playlist-modify-private,playlist-read-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    # get user_id
    user_id = sp.current_user()['id']
    print("user_id:", user_id)
    # get player_id
    playlists = sp.user_playlists(user_id)
    playlist_id = ""
    for item in playlists["items"]:
        if item["name"] == playlist_name:
            playlist_id = item["id"]
    if playlist_id != "":
        print(playlist_name + " already exists")
    else:
        # create playlist if not exist 
        playlist_id = sp.user_playlist_create(user_id, 
                                              f"Billboard-top100-{date}", 
                                              public=False)["id"]
        print(playlist_name + " just created")
    # write to playlist 
    track_urls = []
    for artist, track in list(singer2song.items()):
        result = sp.search(q=f"artist:{artist} track: {track} year: {year}", type="track", limit=1)
        try:
            external_url = result['tracks']['items'][0]["external_urls"]["spotify"]
            print(external_url)
            print(track, artist, external_url)
            track_urls.append(external_url)
        except Exception as e:
            print(e)
            print(track, artist, " not found")
    sp.user_playlist_add_tracks(user_id, playlist_id, track_urls)
