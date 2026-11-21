from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def homepage():
    return """
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="UTF-8>
      <title>cats site</title>
    </head>
    <body>
      <h1>My meme cats site!!</h1>
      <h2>Where you can find information about some meme cats (now where is cats: Katzu, Luna, Rigby</h2>
       <img src="/static/cat1.jpg" width="300">
    </body>
    </html>
    """
