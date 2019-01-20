from pymongo import MongoClient
from bson.json_util import dumps 
import json
import unicodedata
from multiprocessing import Process, Lock, Value
import time

def worker_function(n, lock):
    worker_command = -1
    time.sleep(5)
    with lock:
        worker_command = n.value
    if(worker_command == 1):
        print 'alarm is _on_ I should listen'
    elif(worker_command == 2):
        print 'alarm is _off_ I should do nothing'
        



def command_function(doNum):
    
    client = MongoClient('mongodb://quinn2:quinn2@ds058508.mlab.com:58508/uofthacks')
    db=client.uofthacks
  
    #post_data = posts.findOne()
    command = ''
    value = ''
    document = db.posts.find_one()
    #sprint(document) # iterate the cursor
    print document
    #print type(document)
    for garbage in document.keys():
        if garbage == "name":
            #print key
            command = unicodedata.normalize('NFKD', document[garbage]).encode('ascii','ignore')
        elif garbage == "value":
            #print key
            value = unicodedata.normalize('NFKD', document[garbage]).encode('ascii','ignore')
        else:
            print "not name or value"

    with lock:
        if command == 'Alarm_set':
            if value == 'on':
                doNum.value = 1
            elif value == 'off':
                doNum.value = 2
            else: 
                print 'error: invalid Alarm_set value'
    



#this is the command function
if __name__ == '__main__':
    #queue doNum = Queue()
    doNum = Value('i', -1)
    lock = Lock()
    p = Process(target=worker_function, args=(doNum, lock))
    command_function(doNum)
    p.start()
    p.join()
    print(doNum)
