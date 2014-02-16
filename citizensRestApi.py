from flask import Flask,jsonify,json
from crossdomain import crossdomain
from flask import request
from py2neo import neo4j
import ast
import json
from communityManager import saveCommunity
from userManagement import deleteUser,getAllUsers,saveUser,addContactToUser,getContacts
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route('/addUser', methods=['POST', 'OPTIONS'])
#@crossdomain(origin='*', headers=['Content-Type'])
def getUser():
    saveUser(request.get_json())
  
@app.route('/addCommunity', methods=['POST', 'OPTIONS'])
def addComunity():
    saveCommunity(request.get_json())

@app.route('/deleteUser/<string:email>', methods=['DELETE', 'OPTIONS'])
def removeUser(email) :
    deleteUser(email)
    return "User with email %s was successfully removed" % email

@app.route('/getAllContactsForUser/<string:email>', methods=['GET', 'OPTIONS'])
def getAllContacts(email) :
    return json.dumps(getContacts(email))

@app.route('/getUsers', methods=['GET','OPTIONS'])
def getUsers():
    return json.dumps(getAllUsers())


@app.route('/addContact/<string:current>/<string:newContact>', methods=['POST', 'OPTIONS'])
def addContact(current, newContact) :
    addContactToUser(current, newContact)
    return "addContact was invoked"


def getGraph() :
    return neo4j.GraphDatabaseService("http://localhost:7474/db/data")

if __name__ == '__main__':
    app.debug = True
    app.run()
