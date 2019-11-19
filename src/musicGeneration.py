import spotipy
import json
import sys 
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
from collections import counter 


def genSpotify(headlines):
    market = [ "GB" ]

    CLIENT_ID = "7119d58befe845908623210d01aaa472"
    CLIENT_SECRET = "c6cb0c99349d47efbd92e1fd0fe18786"

    credentials = oauth2.SpotifyClientCredentials(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET)

    token = credentials.get_access_token()
    spotify = spotipy.Spotify(auth=token)


    #filter redundant words from headlines
    filterWords = ['the', 'is', 'and', 'what', 'a', 'at', 'when', 'to', 'of', 'in']
    filterHeadlines = headlines.Split()
    filteredHeadlines = [word for word in filterHeadlines if word.lower() not in filterWords]
    filtered = ' '.join(filteredHeadlines)

    #find 10 most common words
    listWords = filtered.split()
    Counter = Counter(listWords)
    searchWords = Counter.most_common(10)



    #search for each keyword and return top result
    foundTracks = []
    for x in searchWords:
        results = spotify.search(x, type="track", limit = 1)
        foundTracks.append(results)
        
    return foundTracks
        

    #testing functionality of search
    # results = spotify.search('jpegmafia', type="track", limit = 1)
    # for i, t in enumerate(results['tracks']['items']):
    #     print (' ', i, t['name'])