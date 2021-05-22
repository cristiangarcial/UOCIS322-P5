import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.tododb

@app.route('/')
def index():
    return render_template('index.html',
			  items=list(db.tododb.find()))

@app.route('/insert/', methods=['POST'])
def insert():
    item_doc = {
        'title': request.form['title'],
        'body': request.form['body']
    }
    db.tododb.insert_one(item_doc)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
