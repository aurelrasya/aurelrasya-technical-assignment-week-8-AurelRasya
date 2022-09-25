from sqlite3 import Timestamp

from flask import Flask,request

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

def assignment(kecepatan,latitude,longitude) -> tuple:

    try:

        data = {

            "kecepatan": kecepatan,

            "latitude": latitude,

            "logitude": longitude,

            "Timestamp": datetime.datetime.now()

        }

        results = collection.insert_one(data)

        print(results.inserted_ids)

        return True,None

    except Exception as e:

      return False,str(e)
