from cmath import rect

from logging import exception

import pymongo

from flask import Flask,request

client = pymongo.MongoClient("mongodb+srv://aurelrasya:jan9anlup4@atlascluster.6dbbaag.mongodb.net/?retryWrites=true&w=majority")

db = client.sunrise

collection = db.aurel

def sans (kecepatan,latitude,longitude) -> tuple:

    try:

        data = {

            "kecepatan": kecepatan,

            "latitude": latitude,

            "logitude": longitude,

            

        }

        rec_idl = collection.insert_one(data)

        print("Data direcord",rec_idl)

        return True,None

    except Exception as e:

      return False,str(e)
