# Imports
import openai

import json
import datetime
import time

import requests

from flask import Flask
from flask import render_template
from flask import request
from flask import session

app = Flask(__name__)

# Routing
@app.route('/', methods=['GET', 'POST'])
def index():

    
    response = ["", ""]

    if request.method == "POST":    # Query sent
        
        # Keys
        openai.api_key = ""
    
        today = datetime.datetime.now();
        today = time.mktime(today.timetuple())
        lastYear = datetime.datetime.now()-datetime.timedelta(weeks=52);
        lastYear = time.mktime(lastYear.timetuple())
    
        # Get all time historical data: https://api.coingecko.com/ping
        #coinDataQuery = "https://api.coingecko.com/api/v3/coins/" + request.form['query'] + "/market_chart/range?vs_currency=cad&from=" + str(lastYear) +"&to=" + str(today)

        #coinData = requests.get(coinDataQuery)

        #print(coinData.json())

        botResponse = openai.Completion.create(model="text-davinci-003", prompt=request.form['query'], temperature=0, max_tokens=1000)

        response[1] = request.form['query']
        response[0] = botResponse

        # Troubleshooting
        print("Bot Raw Response: ", botResponse)
        print("Bot Text Response: ", response[0])
        print("Last Line: ", response[1])

        # Extract OpenAI response
        response[0] = botResponse["choices"][0]["text"]

        return render_template('index.html', response=response)
    
    else:   # No query
        botResponse = ""

        return render_template('index.html', response=response)
