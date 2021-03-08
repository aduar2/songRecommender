from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    genre = request.args['genre']
    artist = request.args['artist']
    era = request.args['era']
    sign = request.args['sign']
    
    Sign = str(sign)
    Era = str(era)
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
    songs = {
        "2010s rock": {
            "song1": {
                "song": "Spiderhead",
                "artist": "Cage the Elephant",
                "Sign": "scorpio",
                "Type": "water",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song2": {
                "song": "R U Mine?",
                "artist": "Arctic Monkeys",
                "Sign": "capricorn",
                "Type": "earth",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song3": {
                "song": "Dead and Gone",
                "artist": "The Black Keys",
                "Sign": "taurus, aries",
                "Type": "earth, fire",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song4": {
                "song": "1937 State Park",
                "artist": "Car Seat Headrest",
                "Sign": "virgo",
                "Type": "earth",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            }
        },
		
		
        "current pop": {
            "song1": {
                "song": "Test Drive",
                "artist": "Ariana Grande",
                "Sign": "cancer",
                "Type": "water",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song2": {
                "song": "Watermelon Sugar",
                "artist": "Harry Styles",
                "Sign": "aquarius",
                "Type": "air",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song3": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song4": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            }
        },
        
        "90s rock": {
            "song1": {
                "song": "",
                "artist": "Nirvana",
                "Sign": "pisces",
                "Type": "water",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song2": {
                "song": "",
                "artist": "Hole",
                "Sign": "cancer",
                "Type": "water",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song3": {
                "song": "",
                "artist": "Pavement?",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song4": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            }
        },
        
        "current rock": {
            "song1": {
                "song": "",
                "artist": "Beach Bunny",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song2": {
                "song": "",
                "artist": "Greta Van Fleet",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song3": {
                "song": "The Adults are Talking",
                "artist": "The Strokes",
                "Sign": "taurus",
                "Type": "earth",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song4": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            }
        },
        "00s rap": {
            "song1": {
                "song": "",
                "artist": "Kid Cudi",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song2": {
                "song": "",
                "artist": "Kanye West",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song3": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song4": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            }
        },
        "00s indie": {
            "song1": {
                "song": "Two Weeks",
                "artist": "Grizzly Bear",
                "Sign": "libra",
                "Type": "air",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song2": {
                "song": "1901",
                "artist": "Pheonix",
                "Sign": "scorpio",
                "Type": "water",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song3": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song4": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            }
        },
        "70s indie": {
            "song1": {
                "song": "San Francisco",
                "artist": "Foxygen",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song2": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song3": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song4": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            }
        },
        "90s indie": {
            "song1": {
                "song": "",
                "artist": "Pavement",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song2": {
                "song": "She Don't Use Jelly",
                "artist": "The Flaming Lips",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song3": {
                "song": "Fade Into You",
                "artist": "Mazzy Star",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song4": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            }
        },
        "2000s rock": {
            "song1": {
                "song": "Is This Is",
                "artist": "The Strokes",
                "Sign": "taurus",
                "Type": "earth",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song2": {
                "song": "Fell in Love With a Girl",
                "artist": "The White Stripes",
                "Sign": "cancer, sagittarius",
                "Type": "water, fire",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song3": {
                "song": "Heads Will Roll",
                "artist": "Yeah Yeah Yeahs",
                "Sign": "sagittarius",
                "Type": "fire",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song4": {
                "song": "Take Me Out",
                "artist": "Franz Ferdinand",
                "Sign": "sagittarius, pisces",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            }
        },
        "80s rock": {
            "song1": {
                "song": "Kiss Off",
                "artist": "Violent Femmes",
                "Sign": "gemini",
                "Type": "air",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song2": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song3": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song4": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            }
        },
        "0s ": {
            "song1": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song2": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song3": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song4": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            }
        }
    }
    #create and set taste, which is name of dictionary values

    taste = Era + " " + Genre
    
    
    reply = ["0", "1", "2", "3"]
	
    count = 0
    
    for x in songs[taste]:
        songRec = songs[taste][x]["song"]
        artistRec = songs[taste][x]["artist"]
        basicReply = "You might like " + songRec + " by " + artistRec
        
        if artistRec.lower() == Artist:
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
                    
        reply[count] = y
        count = count + 1
        
    theRecs = reply[0] + "   " + reply[1] + "   " + reply[2]+ "   " + reply[3]
    return render_template('response.html', response1 = reply[0], response2 = reply[1], response3 = reply[2], response4 = reply[3])

if __name__=="__main__":
    app.run(debug=False, port=54321)
