from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://quinn:quinn1@ds058508.mlab.com:58508/uofthacks')
db=client.uofthacks
posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott',
    'daddy':'like'
}
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))
#pprint(serverStatusResult)


