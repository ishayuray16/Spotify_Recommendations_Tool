# Spotify Song Recommendations
import spotipy # for web requests to api
from spotipy import SpotifyOAuth # Authentication 
import json # parsing spotify results
# Environment Variables
clientid = "Client ID"
clientsec = "Client Secret"
redirect = "Redirect URI"
# Console Operations
print("Spotify Song Recommendations Tool ")
exprec = input("Do you wish to get explicit recommendations? [y/n] : ")
scope="user-read-recently-played user-top-read user-read-currently-playing"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=clientid, client_secret=clientsec, redirect_uri=redirect))
print("(1) For song recommendations\n(2) For recommendations from a specific genre\n(3) For your stats\n")
choice = int(input())
if(choice==1):
    pass
if(choice==2):
    genre = input("Enter name of the genre : ")
    recommendations = sp.recommendations(seed_genres=[genre], limit=5)
    i = 0
    while i<5:
        print(recommendations['tracks'][i]["name"])
        i+=1
if(choice==3):
   curtrack = sp.current_user_playing_track()
   store = [] # Stores artist names
   print("Currently Playing : ")
   i = 0
   while True:
       try:
           store.append(curtrack["item"]["artists"][i]["name"] + " ")
           i+=1
       except IndexError:
           break
   print(curtrack["item"]["name"] + " - " + "".join(store) )