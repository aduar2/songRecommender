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
    taste = str(taste)
    
    urls = []
        
    replies = []
    
    with open('songs.json') as song_data:
        songs = json.load(song_data)
        
    for song in songs:
        songRec1 = song[taste]["song1"]["song"]
        artistRec1 = song[taste]["song1"]["artist"]
        
        songRec2 = song[taste]["song2"]["song"]
        artistRec2 = song[taste]["song2"]["artist"]
        
        songRec3 = song[taste]["song3"]["song"]
        artistRec3 = song[taste]["song3"]["artist"]
        
        songRec4 = song[taste]["song4"]["song"]
        artistRec4 = song[taste]["song4"]["artist"]
        
        
        basicReply1 = "You might like " + songRec1 + " by " + artistRec1
        basicReply2 = "You might like " + songRec2 + " by " + artistRec2
        basicReply3 = "You might like " + songRec3 + " by " + artistRec3
        basicReply4 = "You might like " + songRec4 + " by " + artistRec4
	
    
    
    #replies
        if artistRec1.casefold() == Artist:
            y = "Here is a song by an artist you already like: " + songRec1 + " by " + artistRec1
        else:
            if element == "none":
                y = basicReply1
            else:
                artistElem1 = song[taste]["song1"]["Type"]
                artistSign1 = song[taste]["song1"]["Sign"]
		
                if artistElem1.find(element) >= 0:
                    if artistSign1.find(Sign) >= 0:
                        #send something to the result page. this is same sign
                        if artistSign1 == "aquarius" or artistSign1 == "aries":
                            y = "You might like this song, which is by an artist who is also an " + sign + ": "+ songRec1 + " by " + artistRec1
                        else:
                            y = "You might like this song, which is by an artist who is also a " + sign + ": "+ songRec1 + " by " + artistRec1
                    else:
                        if element == "earth" or element == "air":
                            y = "This song is by an artist who also has an " + element + " sign: "+ songRec1 + " by " + artistRec1
                        else:
                            y = "This song is by an artist who also has a " + element + " sign: "+ songRec1 + " by " + artistRec1
                else:
                    y = basicReply1
                    
        replies.append(str(y)) #[0]
                    
                    
        if artistRec2.casefold() == Artist:
            y = "Here is a song by an artist you already like: " + songRec2 + " by " + artistRec2
        else:
            if element == "none":
                y = basicReply
            else:
                artistElem2 = song[taste]["song2"]["Type"]
                artistSign2 = song[taste]["song2"]["Sign"]
		
                if artistElem2.find(element) >= 0:
                    if artistSign2.find(Sign) >= 0:
                        #send something to the result page. this is same sign
                        if artistSign2 == "aquarius" or artistSign2 == "aries":
                            y = "You might like this song, which is by an artist who is also an " + sign + ": "+ songRec2 + " by " + artistRec2
                        else:
                            y = "You might like this song, which is by an artist who is also a " + sign + ": "+ songRec2 + " by " + artistRec2
                    else:
                        if element == "earth" or element == "air":
                            y = "This song is by an artist who also has an " + element + " sign: "+ songRec2 + " by " + artistRec2
                        else:
                            y = "This song is by an artist who also has a " + element + " sign: "+ songRec2 + " by " + artistRec2
                else:
                    y = basicReply2
                    
                    replies.append(str(y)) #[1]
                   
                
        if artistRec3.casefold() == Artist:
            y = "Here is a song by an artist you already like: " + songRec3 + " by " + artistRec3
        else:
            if element == "none":
                y = basicReply3
            else:
                artistElem3 = song[taste]["song3"]["Type"]
                artistSign3 = song[taste]["song3"]["Sign"]
		
                if artistElem3.find(element) >= 0:
                    if artistSign3.find(Sign) >= 0:
                        #send something to the result page. this is same sign
                        if artistSign3 == "aquarius" or artistSign3 == "aries":
                            y = "You might like this song, which is by an artist who is also an " + sign + ": "+ songRec3 + " by " + artistRec3
                        else:
                            y = "You might like this song, which is by an artist who is also a " + sign + ": "+ songRec3 + " by " + artistRec3
                    else:
                        if element == "earth" or element == "air":
                            y = "This song is by an artist who also has an " + element + " sign: "+ songRec3 + " by " + artistRec3
                        else:
                            y = "This song is by an artist who also has a " + element + " sign: "+ songRec3 + " by " + artistRec3
                else:
                    y = basicReply3
                    
        replies.append(str(y))#[2]
                 
                
        if artistRec4.casefold() == Artist:
            y = "Here is a song by an artist you already like: " + songRec4 + " by " + artistRec4
        else:
            if element == "none":
                y = basicReply4
            else:
                artistElem4 = song[taste]["song4"]["Type"]
                artistSign4 = song[taste]["song4"]["Sign"]
		
                if artistElem4.find(element) >= 0:
                    if artistSign4.find(Sign) >= 0:
                        #send something to the result page. this is same sign
                        if artistSign4 == "aquarius" or artistSign4 == "aries":
                            y = "You might like this song, which is by an artist who is also an " + sign + ": "+ songRec4 + " by " + artistRec4
                        else:
                            y = "You might like this song, which is by an artist who is also a " + sign + ": "+ songRec4 + " by " + artistRec4
                    else:
                        if element == "earth" or element == "air":
                            y = "This song is by an artist who also has an " + element + " sign: "+ songRec4 + " by " + artistRec4
                        else:
                            y = "This song is by an artist who also has a " + element + " sign: "+ songRec4 + " by " + artistRec4
                else:
                    y = basicReply4
                    
        replies.append(str(y)) #[3]
                   
           
        urls.append(str(song[taste]["song1"][platform]))#[0]
        urls.append(str(song[taste]["song2"][platform]))#[1]
        urls.append(str(song[taste]["song3"][platform]))#[2]
        urls.append(str(song[taste]["song4"][platform]))#[3]
            
            
    return render_template('response.html', response1 = replies[0], response2 = replies[1], response3 = replies[2], response4 = songRec4, songLink1 = urls[0], songLink2 = urls[1], songLink3 = urls[2], songLink4 = urls[3])

if __name__=="__main__":
    app.run(debug=False, port=54321)
