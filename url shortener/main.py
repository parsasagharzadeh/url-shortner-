import random
import string
import json
from flask import Flask, render_template , redirect  , request


app = Flask(__name__)
shortened_url = {}

def shortedUrlName(url):
  words = []
  lastWord=""
  outWord=""
  for word in url:
     words.append([lastWord,word])
     lastWord=word 
  for pearsIndex in range(len(words)):
     if words[pearsIndex][1]=="/" and words[pearsIndex][0]!="/" and words[pearsIndex+1][1]!="/" :
       break
      
     outWord= outWord+words[pearsIndex][1]
  outWord=outWord[8:]
     
    
  return outWord
  
@app.route("/",methods=["GET","POST"])
def index():
  if request.method== "POST":
   long_url = request.form['long_url']
   short_url=shortedUrlName(long_url)
   
   shortened_url[short_url]=long_url 
   with open("url.json","w")as f:
     json.dump(shortened_url,f)
   return f"shortened url : {request.url_root}{short_url}"  
  return render_template("index.html")

@app.route("/<short_url>")
def redirect_url(short_url):
  long_url=shortened_url.get(short_url)
  if long_url:
    print(long_url)
    return redirect(long_url)
  else:
    return "url not finded",404
if __name__ == "__main__":
  app.run(debug=True)