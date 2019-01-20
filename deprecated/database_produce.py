from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://quinn:quinn1@ds058508.mlab.com:58508/uofthacks')
db=client.uofthacks
posts = db.posts
post_data = {
  "user": {
    "userId": "ABwppHEZtWkz2oXVpIIzZXosjimP9aaIvsHNB2WmTLU3s6PxDKkBYBhsN46Q0TOCY_EZPhxo9ipU9j4gM_k",
    "locale": "en-US",
    "lastSeen": "2019-01-19T15:24:17Z"
  },
  "conversation": {
    "conversationId": "ABwppHHsiGH5npIrOXr4_iO0MS8A3jcdzJYwYHAJGU1nt3ehNKSgzXDL_z8OPgzHF2t_EElcHnlJthu2uf8",
    "type": "NEW"
  },
  "inputs": [
    {
      "intent": "enable",
      "rawInputs": [
        {
          "inputType": "KEYBOARD",
          "query": "talk to home safe turn on"
        }
      ],
      "arguments": [
        {
          "name": "trigger_query",
          "rawText": "turn on",
          "textValue": "turn on"
        },
        {
          "name": "enable",
          "rawText": "turn on",
          "textValue": "enable"
        }
      ]
    }
  ],
  "surface": {
    "capabilities": [
      {
        "name": "actions.capability.SCREEN_OUTPUT"
      },
      {
        "name": "actions.capability.AUDIO_OUTPUT"
      },
      {
        "name": "actions.capability.WEB_BROWSER"
      },
      {
        "name": "actions.capability.MEDIA_RESPONSE_AUDIO"
      }
    ]
  },
  "isInSandbox": "true",
  "availableSurfaces": [
    {
      "capabilities": [
        {
          "name": "actions.capability.SCREEN_OUTPUT"
        },
        {
          "name": "actions.capability.AUDIO_OUTPUT"
        },
        {
          "name": "actions.capability.WEB_BROWSER"
        }
      ]
    }
  ],
  "requestType": "SIMULATOR"
}
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))
#pprint(serverStatusResult)


