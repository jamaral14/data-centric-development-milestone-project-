import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'handover_manager'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'Env value not loaded')


@app.route('/')
def hello():
    return 'Hello World'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
                        debug=True)