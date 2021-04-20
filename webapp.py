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
    
    for x in songs[0][taste]:
        songRec = [x][0]["song"]
        artistRec = [x][0]["artist"]
        basicReply = "You might like " + songRec + " by " + artistRec
        
        if artistRec.casefold() == Artist:
            y = "Here is a song by an artist you already like: " + songRec + " by " + artistRec
        else:
            if element == "none":
                y = basicReply
            else:
                artistElem = songs[taste][x]["Type"]
                artistSign = songs[taste][x]["Sign"]
                if artistElem.find(element) >= 0:
                    if artistSign.find(Sign) >= 0:
                        #send something to the result page. this is same sign
                        if artistSign == "aquarius" or artistSign == "aries":
                            y = "You might like this song, which is by an artist who is also an " + sign + ": "+ songRec + " by " + artistRec
                        else:
                            y = "You might like this song, which is by an artist who is also a " + sign + ": "+ songRec + " by " + artistRec
                    else:
                        if element == "earth" or element == "air":
                            y = "This song is by an artist who also has an " + element + " sign: "+ songRec + " by " + artistRec
                        else:
                            y = "This song is by an artist who also has a " + element + " sign: "+ songRec + " by " + artistRec
                else:
                    y = basicReply
                    
        if platform == "Spotify":
            urls[count] = songs[taste][x]["Spotify"]
        elif platform == "Apple":
            urls[count] = songs[taste][x]["Apple"]
        else:
            urls[count] = songs[taste][x]["Youtube"]
                    
        reply[count] = y
        count = count + 1
        
    return render_template('response.html', response1 = reply[0], response2 = reply[1], response3 = reply[2], response4 = reply[3], songLink1 = urls[0], songLink2 = urls[1], songLink3 = urls[2], songLink4 = urls[3])
	

if __name__=="__main__":
    app.run(debug=False, port=54321)
