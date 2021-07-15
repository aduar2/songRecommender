from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def getHome():
	return render_template('home.html')

@app.route("/response")
def getResponse():
        
    genre = request.args['genre']
    artist = request.args['artist']
    decade = request.args['decade']
    sign = request.args['sign']
    platform = request.args['platform']
    
    Sign = str(sign)
    Decade = str(decade)
    Genre = str(genre)
    Artist = str(artist)
    
    Artist = Artist.casefold()
    Sign = Sign.casefold()
    
    if Sign == "leo" or Sign == "aries" or Sign == "sagittarius":
        element = "fire"
    elif Sign == "pisces" or Sign == "cancer" or Sign == "scorpio":
        element = "water"
    elif Sign == "capricorn" or Sign == "taurus" or Sign == "virgo":
        element = "earth"
    elif Sign == "aquarius" or Sign == "gemini" or Sign == "libra":
        element = "air"
    else:
        element = "none"
	
    #set variables from input. use sring methods to rid of whitespace and capitals :)
    

    taste = Decade + " " + Genre
    
    count = 0
    
    reply = ["0", "1", "2", "3"]
    urls = ["0", "1", "2", "3"]
    
    with open('songs.json') as song_data:
        songs = json.load(song_data)
    
    return render_template('response.html', response1 = song, response2 = songs[0], response3 = songs[0][taste])
	

if __name__=="__main__":
    app.run(debug=False, port=54321)
