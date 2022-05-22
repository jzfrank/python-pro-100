Music is memory. Music makes life colorful. 

This little project provides you with the opportunity to time travel with the healing power of music! 

Take you back to a specific date by tracing back the most popular music at that date! 


How to use: 
At the very beginning, install require packages (spotipy, requests, bs4)

1. Downloa this repo
2. Go to spotify developer dashboard  
3. Create a new app 
4. Change the app setting's redirect url to "http://example.com"
5. Open the new app, export its client_id, secret_key in the environment variables
```bash
export SPOTIPY_CLIENT_ID=...
export SPOTIPY_CLIENT_SECRET=...
export SPOTIPY_REDIRECT_URI=http://example.com
```
6. Now good to go!
```bash
python spotify_interactor.py
```
