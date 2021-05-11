# -*- coding: utf-8 -*-
"""
Created on Sat May 09 19:40:38 2021

@author: Yusuf Jordan El Anwar 1184026
"""

from flask import Flask
from textblob import TextBlob
from flask import render_template
from flask import request
import re

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST': 
        URL = request.form['URL']
        hapus = URL.replace(('-'),' ')
        ganti = r"https?://(www\.)?"
        text = re.sub(ganti, ' ', hapus)
        sentiment = TextBlob(text).sentiment.polarity
        print (sentiment)
        
        if sentiment > 0:
            analysis = "Positif"
        elif sentiment == 0:
            analysis = "Netral"
        else:
            analysis = "Negatif"
            
        return render_template('hasil.html', URL=URL, sentiment=sentiment, analysis=analysis)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)