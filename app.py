from flask import Flask, request, render_template, url_for, redirect
import json
import requests
from requests.exceptions import HTTPError

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/load_hotels')
def load_hotels():
    url = 'http://fake-hotel-api.herokuapp.com/api/hotels?count=5'
    json_data = requests.get(url).json()
    print(json_data)
    if "error" in json_data:
        return "Error Occurred,Couldn't fetch any data"
    return render_template('load_hotels1.html', datas=json_data)


@app.route('/reviews/<id>')
def reviews(id):
    if id:
        #in request.args:
       # hotel_id = request.args.get("id")
        data = requests.get('http://fake-hotel-api.herokuapp.com/api/reviews?hotel_id=' + id).json()
        print(data)
        return render_template('reviews.html', datas=data)
    else:
        return "Give hotel id first"


if __name__ == "__main__":
    app.run(debug=True)