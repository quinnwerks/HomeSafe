'use strict';

// Import the Dialogflow module from the Actions on Google client library.
const {dialogflow} = require('actions-on-google');

// Import the firebase-functions package for deployment.
const functions = require('firebase-functions');
const co = require('co');
const mongodb = require('mongodb');

const uri = 'mongodb://micho:micho1@ds058508.mlab.com:58508/uofthacks';

// Instantiate the Dialogflow client.
const app = dialogflow({debug: true});
const https = require("https");
// Handle the Dialogflow intent named 'favorite color'.
// The intent collects a parameter named 'color'.
app.intent('enable', (conv, {enable}) => {

  co(function*() {
    const client = yield mongodb.MongoClient.connect(uri);
     var myobj = { name: "Alarm_set" };
     var newvalues = { $set: {value: "on" } };
   // console.log("req");
client.db('uofthacks').collection('posts').updateOne(myobj, newvalues, function(err, res) {
    if (err) throw err;
   
   
   // db.close();
  });
   
  });
 conv.close('The system is now enabled.');
    // Respond with the user's lucky number and end the conversation.
   
});

app.intent('disable', (conv, {enable}) => {

  co(function*() {
    const client = yield mongodb.MongoClient.connect(uri);
     var myobj = { name: "Alarm_set" };
     var newvalues = { $set: {value: "off" } };
  //  console.log("req");
client.db('uofthacks').collection('posts').updateOne(myobj, newvalues, function(err, res) {
    if (err) throw err;
    
   // db.close();
  });
   
  });
conv.close('The system is now disabled.');
    // Respond with the user's lucky number and end the conversation.
   
});

// Set the DialogflowApp object to handle the HTTPS POST request.
exports.dialogflowFirebaseFulfillment = functions.https.onRequest(app);