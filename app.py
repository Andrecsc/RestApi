from flask import Flask, render_template, jsonify
import json
import requests
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "hello"


@app.route('/getstores')
def get_stores():  # put application's code here
    req = requests.get("http://127.0.0.1:5000/store")
    data = json.loads(req.content)
    return render_template('get_store_s.html', data=data)


@app.route('/getstore')
def get_store():  # put application's code here
    store_name: str = "My Wonderful store"

    req = requests.get("http://127.0.0.1:5000/store/{0}".format(store_name))
    data = json.loads(req.content)
    return render_template('get_store_s.html', data=data)


@app.route('/poststore')
def post_store():  # put application's code here
    store_name: str = "store 2"
    item_name: str = "item 2"
    item_price: float = 12.99

    payload = {'name': store_name, 'item': [{'name': item_name, 'price': item_price}]}
    jsonify(payload)

    req = requests.post("http://127.0.0.1:5000/store", json=payload)

    return render_template("poststore.html", message = str(req.text))


@app.route('/postitem', methods=['POST'])
def post_item():  # put application's code here
    store_name: str = "store 2"
    item_name: str = "item 2"
    item_price: float = 12.99

    payload = {'name': store_name, 'item': [{'name': item_name, 'price': item_price}]}
    jsonify(payload)

    req = requests.post("http://127.0.0.1:5000/{0}/item".format(store_name), json=payload)

    return render_template("postitem.html", message = str(req.text))


if __name__ == '__main__':
    app.run()

