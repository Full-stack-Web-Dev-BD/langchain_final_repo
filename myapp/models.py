from django.db import models
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

connection_String = os.getenv("CONSTRING")

client = MongoClient(connection_String)
db = client['history']

class LogModel(models.Model):

    callerID = models.CharField(max_length=30)
    caller = models.CharField(max_length=100)
    time = models.DateTimeField()
    length = models.IntegerField()
    topic = models.CharField(max_length=30)
    transfer = models.BooleanField(default=False)
    url = models.URLField(max_length=200)
    callbackID = models.CharField(max_length=30)

    @classmethod
    def get_all(self, cid):
        collection = db['logs']
        results = collection.find({"callerID" : cid})
        return results


    def save(self, *args, **kwargs):
        collection = db['logs']
        data = {'callerID' : self.callerID, 'caller': self.caller, 'callbackID': self.callbackID, 'time': self.time, 'length' : self.length, "topic": self.topic, "transfer": self.transfer, "url":self.url}
        collection.insert_one(data)


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')