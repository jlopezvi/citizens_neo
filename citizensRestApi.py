from flask import Flask,jsonify,json
from crossdomain import crossdomain
from flask import request
from py2neo import neo4j
import ast
import json
from communityManager import saveCommunity,deleteCommunity,addCommunityToContact,getCommunities
from userManagement import deleteUser,getAllUsers,saveUser,addContactToUser,getContacts
from concernManager import addConcernToUser,deleteConcern,getAllConcerns
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route('/addUser', methods=['POST', 'OPTIONS'])
#@crossdomain(origin='*', headers=['Content-Type'])
def getUser():
    return saveUser(request.get_json())
  
@app.route('/addCommunity', methods=['POST', 'OPTIONS'])
def addComunity():
    return saveCommunity(request.get_json())

@app.route('/addCommunityToUser/<string:name>/<string:email>', methods=['POST', 'OPTIONS'])
def addCommunityToUser(name, email) :
    addCommunityToContact(name, email)
    return "Community %s was added to user with email %s" % (name, email)

@app.route('/delete/community/<string:name>', methods=['DELETE', 'OPTIONS'])
def removeCommunity(name):
    deleteCommunity(name)
    return "Community %s was successfully removed" % name

@app.route('/deleteUser/<string:email>', methods=['DELETE', 'OPTIONS'])
def removeUser(email) :
    deleteUser(email)
    return "User with email %s was successfully removed" % email

@app.route('/getAllContactsForUser/<string:email>', methods=['GET', 'OPTIONS'])
def getAllContacts(email) :
    return json.dumps(getContacts(email))

@app.route('/getCommunitiesOfUser/<string:email>', methods=['GET','OPTIONS'])
def getAllCommunitiesForUser(email):
    return json.dumps(getCommunities(email))

@app.route('/getUsers', methods=['GET','OPTIONS'])
def getUsers():
    return json.dumps(getAllUsers())


@app.route('/addContact/<string:current>/<string:newContact>', methods=['POST', 'OPTIONS'])
def addContact(current, newContact) :
    addContactToUser(current, newContact)
    return "addContact was invoked"

@app.route('/addConcern/<string:current>', methods=['POST', 'OPTIONS'])
def addConcern(current) :
    concern = request.get_json()
    addConcernToUser(current, concern)

@app.route('/deleteConcern/<string:idConcern>', methods=['POST', 'OPTIONS'])
def deleteConcern(idConcern) :
    print idConcern
    deleteConcern(idConcern)

@app.route('/getAllConcerns/<string:current>', methods=['GET', 'OPTIONS'])
def getConcerns(current):
    print current
    json.dumps(getAllConcerns(current))

if __name__ == '__main__':
    app.debug = True
    app.run()
