import pymongo

import uuid

import datetime

client = pymongo.MongoClient("mongodb+srv://aurelrasya:jan9anlup4@atlascluster.6dbbaag.mongodb.net/?retryWrites=true&w=majority")

db = client.sunrise

collection = db.aurel

def save_to_db(kecepatan,latitude,longitude) -> tuple:

    try:

        data = {

            "kecepatan": kecepatan,

            "latitude": latitude,

            "logitude": longitude,

             }

        results = collection.insert_many(kecepatan,latitude,longitude)

        print(results.inserted_ids)

        return True,None

    except Exception as e:

      return False,str(e)

save_to_db(20,20,20)
