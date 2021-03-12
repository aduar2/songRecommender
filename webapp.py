from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
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
    songs = {
        "current pop": {
            "song1": {
                "song": "Test Drive",
                "artist": "Ariana Grande",
                "Sign": "cancer",
                "Type": "water",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/test-drive/1553944254?i=1553944494",
                "YouTube": ""
            },
            "song2": {
                "song": "Watermelon Sugar",
                "artist": "Harry Styles",
                "Sign": "aquarius",
                "Type": "air",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/watermelon-sugar/1485802965?i=1485802967",
                "YouTube": ""
            },
            "song3": {
                "song": "Violent",
                "artist": "carolesdaughter",
                "Sign": "sagittarius",
                "Type": "fire",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/violent/1541025550?i=1541025569",
                "YouTube": ""
            },
            "song4": {
                "song": " ",
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
                "song": "Painkiller",
                "artist": "Beach Bunny",
                "Sign": "Libra",
                "Type": "air",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/painkiller/1476463573?i=1476463575",
                "YouTube": ""
            },
            "song2": {
                "song": "Bittersweet",
                "artist": "Greer",
                "Sign": "capricorn",
                "Type": "earth",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/bittersweet/1485075167?i=1485075168",
                "YouTube": ""
            },
            "song3": {
                "song": "The Adults are Talking",
                "artist": "The Strokes",
                "Sign": "taurus",
                "Type": "earth",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/the-adults-are-talking/1498121188?i=1498121711",
                "YouTube": ""
            },
            "song4": {
                "song": "I Wish I Was Stephen Malkmus",
                "artist": "Beabadoobee",
                "Sign": "gemini",
                "Type": "air",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/i-wish-i-was-stephen-malkmus/1482163543?i=1482163549",
                "YouTube": ""
            }
        },
        "current indie": {
            "song1": {
                "song": "Townie",
                "artist": "Mitski",
                "Sign": "libra",
                "Type": "air",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/townie/1070245429?i=1070245509",
                "YouTube": ""
            },
            "song2": {
                "song": "What Do You Want from Me Tonight?",
                "artist": "Sidney Gish",
                "Sign": "pisces",
                "Type": "water",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/what-do-you-want-from-me-tonight/1193369386?i=1193369399",
                "YouTube": ""
            },
            "song3": {
                "song": "",
                "artist": "",
                "Sign": "",
                "Type": "earth",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song4": {
                "song": "Fool",
                "artist": "Frankie Cosmos",
                "Sign": "aries",
                "Type": "fire",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/fool/1079006535?i=1079006538",
                "YouTube": ""
            }
        },
        "2010s pop": {
            "song1": {
                "song": "Lights",
                "artist": "Ellie Goulding",
                "Sign": "capricorn",
                "Type": "earth",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/lights-single-version/1440788349?i=1440788691",
                "YouTube": ""
            },
            "song2": {
                "song": "Blank Space",
                "artist": "Taylor Swift",
                "Sign": "sagittarius",
                "Type": "fire",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/blank-space/1440935467?i=1440935808",
                "YouTube": ""
            },
            "song3": {
                "song": "Everybody Talks",
                "artist": "Neon Trees",
                "Sign": "sagittarius",
                "Type": "fire",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/everybody-talks/1443506853?i=1443506997",
                "YouTube": ""
            },
            "song4": {
                "song": "Diamonds",
                "artist": "Rihanna",
                "Sign": "pisces",
                "Type": "water",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/diamonds/1443232426?i=1443232440",
                "YouTube": ""
            }
        },

        "2010s rock": {
            "song1": {
                "song": "Spiderhead",
                "artist": "Cage the Elephant",
                "Sign": "scorpio",
                "Type": "water",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/spiderhead/683346293?i=683346493",
                "YouTube": ""
            },
            "song2": {
                "song": "R U Mine?",
                "artist": "Arctic Monkeys",
                "Sign": "capricorn",
                "Type": "earth",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/r-u-mine/663097964?i=663097966",
                "YouTube": ""
            },
            "song3": {
                "song": "Dead and Gone",
                "artist": "The Black Keys",
                "Sign": "taurus, aries",
                "Type": "earth, fire",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/dead-and-gone/1052966287?i=1052966685",
                "YouTube": ""
            },
            "song4": {
                "song": "1937 State Park",
                "artist": "Car Seat Headrest",
                "Sign": "virgo",
                "Type": "earth",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/1937-state-park/1117093779?i=1117094123",
                "YouTube": ""
            }
        },
        "2010s indie": {
            "song1": {
                "song": "",
                "artist": "Grimes",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song2": {
                "song": "",
                "artist": "Mac DeMarco",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "",
                "YouTube": ""
            },
            "song3": {
                "song": "",
                "artist": "Tame Impala",
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
        "00s pop": {
            "song1": {
                "song": "Poker Face",
                "artist": "Lady Gaga",
                "Sign": "aries",
                "Type": "fire",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/poker-face/1476727669?i=1476727864",
                "YouTube": ""
            },
            "song2": {
                "song": "Promiscuous (feat. Timbaland)",
                "artist": "Nelly Furtado",
                "Sign": "sagittarius",
                "Type": "fire",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/promiscuous-feat-timbaland/1442463545?i=1442463848",
                "YouTube": ""
            },
            "song3": {
                "song": "Paper Planes",
                "artist": "M.I.A.",
                "Sign": "cancer",
                "Type": "water",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/paper-planes/296393419?i=296393515",
                "YouTube": ""
            },
            "song4": {
                "song": "Umbrella (feat. JAY Z)",
                "artist": "Rihanna",
                "Sign": "pisces",
                "Type": "water",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/umbrella-feat-jay-z/1441154435?i=1441154437",
                "YouTube": ""
            }
        },
        "00s indie": {
            "song1": {
                "song": "Two Weeks",
                "artist": "Grizzly Bear",
                "Sign": "libra",
                "Type": "air",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/two-weeks/314837656?i=314837675",
                "YouTube": " "
            },
            "song2": {
                "song": "1901",
                "artist": "Pheonix",
                "Sign": "scorpio",
                "Type": "water",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/1901/1450828963?i=1450829103",
                "YouTube": " "
            },
            "song3": {
                "song": "Rawnald Gregory Erickson the Second",
                "artist": "STRFKR",
                "Sign": "",
                "Type": "",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/rawnald-gregory-erickson-the-second/290359552?i=290359609",
                "YouTube": " "
            },
            "song4": {
                "song": "Young Folks",
                "artist": "Peter Bjorn and John",
                "Sign": "libra, taurus",
                "Type": "air, earth",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/young-folks/215554129?i=215554232",
                "YouTube": " "
            }
        },
        "00s rock": {
            "song1": {
                "song": "Is This It",
                "artist": "The Strokes",
                "Sign": "taurus",
                "Type": "earth",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/is-this-it/266376953?i=266376961",
                "YouTube": " "
            },
            "song2": {
                "song": "Fell in Love With a Girl",
                "artist": "The White Stripes",
                "Sign": "cancer, sagittarius",
                "Type": "water, fire",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/fell-in-love-with-a-girl/1533513361?i=1533513365",
                "YouTube": " "
            },
            "song3": {
                "song": "Heads Will Roll",
                "artist": "Yeah Yeah Yeahs",
                "Sign": "sagittarius",
                "Type": "fire",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/heads-will-roll/1440771833?i=1440771850",
                "YouTube": " "
            },
            "song4": {
                "song": "Take Me Out",
                "artist": "Franz Ferdinand",
                "Sign": "sagittarius, pisces",
                "Type": "fire, water",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/take-me-out/315843479?i=315844084",
                "YouTube": " "
            }
        },
        "90s pop": {
            "song1": {
                "song": "Just a Girl",
                "artist": "No Doubt",
                "Sign": "libra",
                "Type": "air",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/just-a-girl/1440845400?i=1440845532",
                "YouTube": ""
            },
            "song2": {
                "song": "Say My Name",
                "artist": "Destiny's Child",
                "Sign": "leo, aquarius, virgo",
                "Type": "fire, air, earth",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/say-my-name/266809606?i=266809802",
                "YouTube": ""
            },
            "song3": {
                "song": "Thank You",
                "artist": "Dido",
                "Sign": "capricorn",
                "Type": "earth",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/thank-you/254578536?i=254579170",
                "YouTube": ""
            },
            "song4": {
                "song": "Human Nature",
                "artist": "SWV",
                "Sign": "gemini, cancer, taurus",
                "Type": "air, water, earth",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/right-here-human-nature-radio-mix/266799911?i=266800348",
                "YouTube": ""
            }
        },
        "90s rock": {
            "song1": {
                "song": "On a Plain",
                "artist": "Nirvana",
                "Sign": "pisces",
                "Type": "water",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/on-a-plain/1440783617?i=1440783786",
                "YouTube": ""
            },
            "song2": {
                "song": "Plump",
                "artist": "Hole",
                "Sign": "cancer",
                "Type": "water",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/plump/1445732603?i=1445732610",
                "YouTube": ""
            },
            "song3": {
                "song": "Loretta's Scars",
                "artist": "Pavement?",
                "Sign": "gemini",
                "Type": "air",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/lorettas-scars/1544358287?i=1544358708",
                "YouTube": ""
            },
            "song4": {
                "song": "Blow Up the Outside World",
                "artist": "Soundgarden",
                "Sign": "cancer",
                "Type": "water",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/blow-up-the-outside-world/1440866412?i=1440866777",
                "YouTube": ""
            }
        },
   
        "90s indie": {
            "song1": {
                "song": "Harness Your Hopes",
                "artist": "Pavement",
                "Sign": "gemini",
                "Type": "air",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/harness-your-hopes-b-side/295095700?i=295095778",
                "YouTube": ""
            },
            "song2": {
                "song": "She Don't Use Jelly",
                "artist": "The Flaming Lips",
                "Sign": "capricorn",
                "Type": "earth",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/she-dont-use-jelly/1231989623?i=1231989631",
                "YouTube": " "
            },
            "song3": {
                "song": "Fade Into You",
                "artist": "Mazzy Star",
                "Sign": "cancer",
                "Type": "water",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/fade-into-you/1440848808?i=1440848810",
                "YouTube": " "
            },
            "song4": {
                "song": "",
                "artist": "Neutral Milk Hotel",
                "Sign": "Scorpio",
                "Type": "water",
                "Spotify": "",
                "Apple": " ",
                "YouTube": ""
            }
        },
        "80s pop": {
            "song1": {
                "song": "Material Girl",
                "artist": "Madonna",
                "Sign": "leo",
                "Type": "fire",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/material-girl/80815235?i=80815209",
                "YouTube": ""
            },
            "song2": {
                "song": "If You Leave",
                "artist": "Orchestral Manoeuvres In the Dark",
                "Sign": "cancer, pisces",
                "Type": "water",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/if-you-leave/726172489?i=726172620",
                "YouTube": ""
            },
            "song3": {
                "song": "Karma Chameleon",
                "artist": "Culture Club",
                "Sign": "gemini",
                "Type": "air",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/karma-chameleon/724214023?i=724214046",
                "YouTube": ""
            },
            "song4": {
                "song": "Call Me",
                "artist": "Blondie",
                "Sign": "cancer",
                "Type": "water",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/call-me/716231242?i=716231650",
                "YouTube": ""
            }
        },
        "80s indie": {
            "song1": {
                "song": "The Killing Moon",
                "artist": "Echo & the Bunnymen",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/the-killing-moon/31740160?i=31740178",
                "YouTube": ""
            },
            "song2": {
                "song": "Jealous",
                "artist": "Eyedress",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/jealous/1485913818?i=1485913824",
                "YouTube": ""
            },
            "song3": {
                "song": "Age of Consent",
                "artist": "Joy Division",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/age-of-consent/1040981945?i=1040982045",
                "YouTube": ""
            },
            "song4": {
                "song": "1 4 2",
                "artist": "Inner Wave",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/1-4-2/1441533537?i=1441533773",
                "YouTube": ""
            }
        },
        "80s rock": {
            "song1": {
                "song": "Kiss Off",
                "artist": "Violent Femmes",
                "Sign": "gemini",
                "Type": "air",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/kiss-off/1455129708?i=1455129986",
                "YouTube": " "
            },
            "song2": {
                "song": "Bad Reputation;",
                "artist": "Joan Jett",
                "Sign": "virgo",
                "Type": "earth",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/bad-reputation/1434145250?i=1434145252",
                "YouTube": " "
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
                "Sign": "scorpio, aquarius",
                "Type": "water, air",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/san-francisco/579417867?i=579417919",
                "YouTube": " "
            },
            "song2": {
                "song": "Psycho Killer",
                "artist": "Talking Heads",
                "Sign": "Taurus",
                "Type": "earth",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/psycho-killer/124925532?i=124924802",
                "YouTube": " "
            },
            "song3": {
                "song": "Sarah",
                "artist": "Alex G",
                "Sign": "aquarius",
                "Type": "air",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/sarah/1483272616?i=1483272819",
                "YouTube": " "
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
	    "70s rock": {
            "song1": {
                "song": "Picture Book",
                "artist": "The Kinks",
                "Sign": "",
                "Type": "",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/picture-book-2018-stereo-remaster/1422691058?i=1422691732",
                "YouTube": ""
            },
            "song2": {
                "song": "Cherry Bomb",
                "artist": "Runaways",
                "Sign": "",
                "Type": "",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/cherry-bomb/1440747926?i=1440747928",
                "YouTube": " "
            },
            "song3": {
                "song": "Break On Through",
                "artist": "The Doors",
                "Sign": "sagittarius",
                "Type": "fire",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/break-on-through-to-the-other-side-mono-remastered/1192962129?i=1192962341",
                "YouTube": " "
            },
            "song4": {
                "song": "70s ",
                "artist": "Queen",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": " ",
                "YouTube": ""
            }
        },
        "70s pop": {
            "song1": {
                "song": "These Boots Are Made for Walkin'",
                "artist": "Nancy Sinatra",
                "Sign": "gemini",
                "Type": "air",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/these-boots-are-made-for-walkin/148036422?i=148036556",
                "YouTube": " "
            },
            "song2": {
                "song": "Sunshine, Lollipops and Rainbows",
                "artist": "Lesley Gore",
                "Sign": "aquarius",
                "Type": "air",
                "Spotify": " ",
                "Apple": "https://music.apple.com/us/album/sunshine-lollipops-and-rainbows/1444110306?i=1444110937",
                "YouTube": " "
            },
            "song3": {
                "song": "Bennie and the Jets",
                "artist": "Elton John",
                "Sign": "Aries",
                "Type": "fire",
                "Spotify": "",
                "Apple": "https://music.apple.com/us/album/bennie-and-the-jets/1440863013?i=1440863120",
                "YouTube": ""
            },
            "song4": {
                "song": "70s",
                "artist": "",
                "Sign": "",
                "Type": "",
                "Spotify": "",
                "Apple": " ",
                "YouTube": ""
            }
        }
    }

    taste = Decade + " " + Genre
    
    count = 0
    
    reply = ["0", "1", "2", "3"]
    urls = ["0", "1", "2", "3"]
    
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
