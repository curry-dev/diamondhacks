from pymongo import MongoClient

mongoclient = MongoClient('mongodb+srv://devankshi:devapwd@outfitmatch.s4hpn.mongodb.net/?retryWrites=true&w=majority&appName=outfitmatch')

# db = mongoclient['sample_mflix']
# collection = db['users']
# documents = list(collection.find())
# for document in documents:
#     print(document)





# mongodb start
from pymongo import MongoClient

# MONGODB_URI = os.environ['MONGODB_URI']
mongoclient = MongoClient('mongodb+srv://devankshi:devapwd@cluster0.xtgxdsm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
print(mongoclient.list_database_names()) 
# db = mongoclient['sample_mflix']
# collection = db['users']
# print('count:', collection.count_documents({}))
# mongodb end