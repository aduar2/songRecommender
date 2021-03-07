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
	
	reply = "eeeeee"
    		
	return render_template('result.html', return = reply)
    
if __name__=="__main__":
	app.run(debug=False, port=54321)
