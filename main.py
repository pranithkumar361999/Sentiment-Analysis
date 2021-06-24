from flask import Flask,render_template,redirect,request,send_file
from flask_sqlalchemy import SQLAlchemy
import os
import string
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app=Flask(__name__)


@app.route('/analyze')
def analyze():
    text=open('reviews.txt',encoding='utf-8').read()
    analyser=SentimentIntensityAnalyzer()
    score=analyser.polarity_scores(text)
    if score['compound']>=0.5:
        img='/static/positive.jpg'
        comment='Good'
    elif score['compound']<=-0.5:
        img='/static/negative.jpg'
        comment='Bad'
    else:
        img='/static/neutral.png'
        comment='Neutral'
    

    return render_template('analyze.html',img=img,comment=comment)

@app.route('/reviews')
def reviews():
    text=open('reviews.txt',encoding='utf-8').read()
    splitted_text=text.split()
    return render_template('overall.html',text=splitted_text)
    



@app.route("/",methods=['GET','POST'])
def index():
    if request.method=="POST":
        text=request.form['review']
        print(text)
        f1=open("reviews.txt","a+")
        f1.write(text)
        f1.write("\n")
        f1.close()

    else:
        return render_template('index.html')


    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)