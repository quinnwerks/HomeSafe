from pymongo import MongoClient

client = MongoClient('mongodb://quinn2:quinn2@ds058508.mlab.com:58508/uofthacks')
db=client.uofthacks
posts = db.posts

#post_data = posts.findOne()
for document in posts.find():
    print(document) # iterate the cursor
posts.remove()
