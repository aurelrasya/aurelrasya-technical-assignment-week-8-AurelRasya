from sqlite3 import Timestamp

from flask import Flask,request

from db import save_to_db

import pymongo

import datetime

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://aurelrasya:jan9anlup4@atlascluster.6dbbaag.mongodb.net/?retryWrites=true&w=majority")

db = client.sunrise

collection = db.aurel

@app.route('/week8',methods=['GET','POST'])

def location_application():

    kecepatan= request.args.get('kecepatan')

    latitude = request.args.get('latitude')

    longitude = request.args.get('longitude')

    save_to_db(kecepatan=kecepatan,latitude=latitude,longitude=longitude)

    return{

        "output":{

            "kecepatan":kecepatan,

            "latitude":latitude,

            "longitude":longitude,

            "timestamp": datetime.datetime.now()

        }

    }

if __name__ == '__main__':

    app.run(debug=True)
