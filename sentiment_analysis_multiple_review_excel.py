import json
from typing import OrderedDict
import requests
from re import T
from flask import Flask,jsonify,request
from flask import request
from textblob import TextBlob
import pandas as pd
import flask_excel as excel

app= Flask(__name__)

def review(data):
    feedback=data
    blob=TextBlob(feedback)
    list=[]
    list.append(blob.sentiment)
    return list
   
    


def formatoutput(total,pos,neg,neu):
    output = OrderedDict({
            "total review":total,
            "positive review":pos,
            "negative review":neg,
            "neutral review":neu,
            })
    return output



     


@app.route('/sentiment', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file_key']
        data_xls = pd.read_excel(f)
        list=data_xls.values.tolist()
        total_review=0
        pos_count=0
        neg_count=0
        neu_count=0
        for sublist in list:
            for text in sublist:
                score=review(text)
                total_review += 1
                if score[0][0] > 0:
                    pos_count += 1
                elif score[0][0] < 0:
                    neg_count += 1
                else:
                    neu_count += 1   

        result=formatoutput(total_review,pos_count,neg_count,neu_count)
    return OrderedDict(result)
    

    



if __name__ == "__main__":
    app.run(debug="TRUE")
        