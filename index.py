from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
	return render_template('home.html')


@app.route("/result")
def render_result():
	genre = request.args['genre']
	artist = request.args['artist']
	era = request.args['era']
	sign = request.args['sign']
	
	if sign == "leo" or "aries" or "sagittarius"
		element = "fire"
	else if sign == "pisces" or "cancer" or "scorpio"
		element = "water"
	else if sign == "capricorn" or "taurus" or "virgo"
		element = "earth"
	else if sign == "aquarius" or "gemini" or "libra"
		element = "air"
	else
		element = "none"
		
	genre = genre.casefold
	artist = artist.casefold
	era = era.casefold
	sign = sign.casefold

    #set variables from input. use sring methods to rid of whitespace and capitals :)
    
	songs = {
		"2010s rock": {
		"song1": {
			"song": "Sweetie Little Jean",
			"artist": "Cage the Elephant",
			"Sign": "scorpio",
			"Type": "water"
		 },
		 "song2": {
			 "song": "R U Mine?",
		 	"artist": "Arctic Monkeys",
			 "Sign": "capricorn",
			 "Type": "earth"
		 },
		 "song3": {
			 "song": "Dead and Gone",
		 	"artist": "The Black Keys",
			 "Sign": "taurus, aries",
			 "Type": "earth, fire"
		 },
		 "song4": {
		 	"song": "",
		 	"artist": "",
			"Sign": "",
		 	"Type": ""
		 }
	},
	
	
	"current pop": {
		"song1": {
			"song": "Test Drive",
			"artist": "Ariana Grande",
			"Sign": "cancer",
			"Type": "water"
		 },
		 "song2": {
		 	"song": "Watermelon Sugar",
		 	"artist": "Harry Styles",
		 	"Sign": "aquarius",
		 	"Type": "air"
		 },
		 "song3": {
			 "song": "",
		 	"artist": "",
			 "Sign": "",
			 "Type": ""
		 },
		 "song4": {
		 	"song": "",
		 	"artist": "",
			"Sign": "",
		 	"Type": ""
		 }
		},
		 
	
	"90s rock": {
		"song1": {
			"song": "",
			"artist": "Nirvana",
			"Sign": "pisces",
			"Type": "water"
		},
		 "song2": {
		 	"song": "",
		 	"artist": "Hole",
		 	"Sign": "cancer",
		 	"Type": "water"
		 },
		 "song3": {
			 "song": "",
		 	"artist": "Pavement?",
			 "Sign": "",
			 "Type": ""
		},
		 "song4": {
		 	"song": "",
		 	"artist": "",
			"Sign": "",
		 	"Type": ""
		 
		 }
		},
			
	
	"current rock": {
		"song1": {
			"song": "",
			"artist": "Beach Bunny",
			"Sign": "",
			"Type": ""
		 },
		 "song2": {
		 	"song": "",
		 	"artist": "Greta Van Fleet",
		 	"Sign": "",
		 	"Type": ""
		 },
		 "song3": {
		 	"song": "The Adults are Talking",
		 	"artist": "The Strokes",
		 	"Sign": "taurus",
		 	"Type": "earth"
		 },
		 
		 "song4": {
		 	"song": "",
		 	"artist": "",
			"Sign": "",
		 	"Type": ""
		 
		 }
		
		},
	
	
	"00s rap": {
		"song1": {
			"song": "",
			"artist": "Kid Cudi",
			"Sign": "",
			"Type": ""
		 },
		 "song2": {
		 	"song": "",
		 	"artist": "Kanye West",
		 	"Sign": "",
		 	"Type": ""
		 },
		 "song3": {
			 "song": "",
		 	"artist": "",
			 "Sign": "",
			 "Type": ""
		 },
		 "song4": {
		 	"song": "",
		 	"artist": "",
			"Sign": "",
		 	"Type": ""
		 
		 }
		
		},

		
	"00s indie": {
		"song1": {
			"song": "Two Weeks",
			"artist": "Grizzly Bear",
			"Sign": "libra",
			"Type": "air"
		 },
		 "song2": {
		 	"song": "1901",
		 	"artist": "Pheonix",
		 	"Sign": "scorpio",
		 	"Type": "water"
		 },
		 "song3": {
			 "song": "",
		 	"artist": "",
			 "Sign": "",
			 "Type": ""
		 },
		 "song4": {
		 	"song": "",
		 	"artist": "",
			"Sign": "",
		 	"Type": ""
		 }
		},
	
	
	"70s indie": {
		"song1": {
			"song": "San Francisco",
			"artist": "Foxygen",
			"Sign": "",
			"Type": ""
		 },
		 "song2": {
		 	"song": "",
		 	"artist": "",
		 	"Sign": "",
		 	"Type": ""
		 },
		 "song3": {
			 "song": "",
		 	"artist": "",
			 "Sign": "",
			 "Type": ""
		 },
		 "song4": {
		 	"song": "",
		 	"artist": "",
			"Sign": "",
		 	"Type": ""
		 
		 }
		
		},
	

	"90s indie": {
		"song1": {
			"song": "",
			"artist": "Pavement",
			"Sign": "",
			"Type": ""
		 },
		 "song2": {
		 	"song": "She Don't Use Jelly",
		 	"artist": "The Flaming Lips",
		 	"Sign": "",
		 	"Type": ""
		 },
		 "song3": {
			 "song": "Fade Into You",
		 	"artist": "Mazzy Star",
			 "Sign": "",
			 "Type": ""
		 },
		 "song4": {
		 	"song": "",
		 	"artist": "",
			"Sign": "",
		 	"Type": ""
		 
		 }
		
		},

		
	"2000s rock": {
		"song1": {
			"song": "Is This Is",
			"artist": "The Strokes",
			"Sign": "taurus",
			"Type": "earth"
			},
		 "song2": {
		 	"song": "Fell in Love With a Girl",
		 	"artist": "The White Stripes",
		 	"Sign": "cancer, sagittarius",
		 	"Type": "water, fire"
		 	},
		 "song3": {
			 "song": "Heads Will Roll",
		 	"artist": "Yeah Yeah Yeahs",
			 "Sign": "sagittarius",
			 "Type": "fire"
			 },
		 "song4": {
		 	"song": "Take Me Out",
		 	"artist": "Franz Ferdinand",
			"Sign": "sagittarius, pisces",
		 	"Type": ""
		 	}
		 },
		 	 
		 
	"80s rock": {
		"song1": {
			"song": "Kiss Off",
			"artist": "Violent Femmes",
			"Sign": "gemini",
			"Type": "air"
			},
		 "song2": {
		 	"song": "",
		 	"artist": "",
		 	"Sign": "",
		 	"Type": ""
		 	},
		 "song3": {
			 "song": "",
		 	"artist": "",
			 "Sign": "",
			 "Type": ""
			 },
		 "song4": {
		 	"song": "",
		 	"artist": "",
			"Sign": "",
		 	"Type": ""
		 	}
		 },
		 
		 
	"0s ": {
		"song1": {
			"song": "",
			"artist": "",
			"Sign": "",
			"Type": ""
			},
		 "song2": {
		 	"song": "",
		 	"artist": "",
		 	"Sign": "",
		 	"Type": ""
		 	},
		 "song3": {
			 "song": "",
		 	"artist": "",
			 "Sign": "",
			 "Type": ""
		 	},
		 "song4": {
		 	"song": "",
		 	"artist": "",
			"Sign": "",
		 	"Type": ""
		 
		 	}
		 }
		
		
	}
	

	#create and set element variables
	if sign.find("leo") == 0 or sign.find("aries") == 0 or sign.find("sagittarius") == 0:
		element = "fire"
	elif sign.find("pisces") == 0 or sign.find("cancer") == 0 or sign.find("scorpio") == 0:
		element = "water"
	elif sign.find("taurus") == 0 or sign.find("capricorn") == 0 or sign.find("virgo") == 0:
		element = "earth"
	elif sign.find("aquarius") == 0 or sign.find("gemini") == 0 or sign.find("libra") == 0:
		element = "air"
	else:
		element = "none"
    

    
    #create and set taste, which is name of dictionary values
	taste = era + " " + genre
    

	for x in songs[taste]:
		songRec = songs[taste][x]["song"]
		artistRec = songs[taste][x]["artist"]
		basicReply = "You might like " + songRec + " by " + artistRec
		
	if element == "none":
		result = basicReply
	else:
		artistElem = songs[taste][x]["Type"]
		artistSign = songs[taste][x]["Sign"]
		if artistElem.find(element) >= 0:
			if artistSign.find(sign) >= 0:
				#send something to the result page. this is same sign
				if artistSign == "aquarius" or artistSign == "aries":
					reply = "You might like this song, which is by an artist who is also an  " + sign + " : "+ songRec + " by " + artistRec
				else:
					reply = "You might like this song, which is by an artist who is also a " + sign + " : "+ songRec + " by " + artistRec
				
			else:
				if element == "earth" or element == "air":
					reply = "This song is by an artist who also has an " + element + " sign: "+ songRec + " by " + artistRec
				else:
					reply = "This song is by an artist who also has a " + element + " sign: "+ songRec + " by " + artistRec
		else:
			reply = basicReply
    		#ALSO sent to results page. this is absolutle yno zodiac connection
    		
	return render_template('result.html', result = reply)
    
if __name__=="__main__":
	app.run(debug=True, port=54321)
