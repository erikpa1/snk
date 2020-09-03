from flaskr.server import *

from flask import render_template


@app.route('/')
@app.route('/index.html')
def CreateMainPage():
    print("Here")
    render_template("page_main.html")
    pass


app.run(debug = True)