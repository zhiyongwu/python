import pymongo

client = pymongo.MongoClient('localhost',27017)
db = client.mycoll
for data in db.col.find():
	print(data)