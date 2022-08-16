import json
import requests
from re import T
from flask import Flask, jsonify
from flask import request
from textblob import TextBlob
app= Flask(__name__)

def review(data):
    feedback=data
    blob=TextBlob(feedback)
    list=[]
    list.append(blob.sentiment)
    return list


def formatoutput(score):
    if score[0][0] > 0.0:
        output = {
            "total review":1,
            "positive review":1,
            "negative review":0,
            "neutral review":0,
            "result":"positive"
            }
    if score[0][0] < 0.0:
        output={
            "total review":1,
            "positive review":0,
            "negative review":1,
            "neutral review":0,
            "result":"negative"
        }
    else:
        output={
            "total review":1,
            "positive review":1,
            "negative review":0,
            "neutral review":1,
            "result":"neutral"
        }

    return output   




@app.route('/random',methods=['POST'])
def get():
    data = request.get_json()
    score=review(data)
    result=formatoutput(score)
    return result

    
@app.route('/api',methods=['GET','POST'])
def tests():
    if request.method == "POST":
        print("got requestmethod post")
    if request.is_json:
        print("json")
        data =request.get_json()
        return jsonify(data)



if __name__ == "__main__":
    app.run(debug = True)    