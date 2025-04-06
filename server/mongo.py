# from pymongo import MongoClient
# import os
# from dotenv import load_dotenv
# load_dotenv()
# MONGODB_URI = os.environ['MONGODB_URI']
# mongoclient = MongoClient(MONGODB_URI)
# # print(mongoclient.list_database_names()) 
# db = mongoclient['sample_mflix']
# collection = db['users']
# print('collection:', collection)
# print('count:', collection.count_documents({}))


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://devankshi:devapwd@cluster0.xtgxdsm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)