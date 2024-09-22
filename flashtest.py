#!/bin/python

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def memes():
	url = "https://www.reddit.com/r/api/meme/random.json"
	response = json.loads(requests.request("GET",url).text)
	meme_large = response["preview"][-2]
	return meme_large,subreddit

@app.route("/")
def index():
	meme_pic,subreddit = memes()
	return render_template("index.html",meme_pic=meme_pic,subreddit=subreddit)

app.run(host = "0.0.0.0", port=80)

