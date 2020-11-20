from difflib import SequenceMatcher
import random
from data import data
from flask import Flask, request, json ,render_template ,Response

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def chatbot (inputStr):
    maxPercent = 0.0
    Type = ""
    for i in data:
        for model in i["models"]:
            similarity = similar(inputStr, model)
            if maxPercent <= similarity:
                maxPercent = similarity
                Type = i["type"]
    if maxPercent <= 0.4:
        return maxPercent , "متاسفانه دیتایی پیدا نشد."
    return maxPercent, random.choice((next((sub for sub in data if sub['type'] == Type), None))["responses"])

def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )

app = Flask(__name__)
@app.route("/api", methods=['POST'])
def hello():
    data = request.form['input']
    maxp ,data = chatbot(data)
    print(maxp)
    return render_template("hello.html",name=data)
@app.route("/" , methods = ['POST', 'GET'])
def main():    
    return render_template("hello.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)

