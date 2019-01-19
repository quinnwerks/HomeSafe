from pymongo import MongoClient
from bson.json_util import dumps 
import json
import unicodedata
client = MongoClient('mongodb://quinn2:quinn2@ds058508.mlab.com:58508/uofthacks')
db=client.uofthacks
posts = db.posts

#post_data = posts.findOne()
command = ''
value = ''
command = -1
document = posts.findOne({name:"Alarm_set"})

#sprint(document) # iterate the cursor
print document
#print type(document)
for garbage in document.keys():
    print key
    if garbage == "name":
        #print key
        command = unicodedata.normalize('NFKD', document[garbage]).encode('ascii','ignore')
    elif key == "value":
        #print key
        value = unicodedata.normalize('NFKD', document[garbage]).encode('ascii','ignore')
    else:
        print "not name or value"

if len(keyList) != len(valueList):
    print 'error: kv length mismatch'


if keyList[0] == 'Alarm_set':
    if valueList[0] == 'On':
        command = 1
    elif valueList[0] == 'Off':
        command = 2
    else: 
        print 'error: invalid Alarm_set value'

print command



print keyList
print valueList
#print type(keyList[0])
#print(doc_json['name'])

def dummy_function():
    print 'do machine learning lmao'



