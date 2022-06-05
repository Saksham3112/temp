# THE FILE NAME MUST BE APP.PY

from flask import Flask,render_template,request


app = Flask("__main__")

# DECORATOR 
@app.route("/")
def parentdir():
    return "<a href='/home'>Hello Front End</a>"

outdoor_sports=["Cricket","baseball","football","tennis","rugby"]

@app.route("/home")
def home():
    ## return "<marquee>It's Home</marquee>"
    #same as using rendering 
    #return '''<html>
    #<head> </head>
    #<body>
    #    <h1>Welcome to home</h1>
    #</body>
    #</html>'''
    #print(render_template("home.html"))  GETS WRITTEN AT SERVER CONSOLE
    name=request.args.get("name")
    return render_template("home.html",name=name.title(),arr=outdoor_sports)

if __name__=="__main__":
    # app.run() // Requires to run the python file after each save
    app.run(use_reloader=True,debug=True)