from py2neo import neo4j
import ast
import json
import logging
from utils import NotFoundError,getGraph

def saveUser(user):
    email = user.get('email')
    try:
        getUserByEmail(email)
        app.logger.debug("user with email %s already exists" % email)
        return "User with email %s already exists" % email
    except NotFoundError as e:
       newUser(user)
       return "User %s was successfully added" % email

def newUser(userJson):
    app.logger.debug("new user is being created..")
    email = userJson.get('email')
    newUser, = getGraph().create({"name" : userJson.get('name'), "surname" : userJson.get('surname'), "email" : email, "country" : userJson.get('country'), "city" : userJson.get('city')})
    __addToUsersIndex(email, newUser)
    app.logger.debug("%s has just been added" % email)


def deleteUser(email) :
    userFound = __getUserByEmail(email)
    userFound.delete()

def getAllUsers():
    allnodes = __getUsersIndex().query("email:*")
    users = []
    for node in allnodes:
         users.append(node.get_properties())
    return users

def __getUsersIndex():
    return getGraph().get_or_create_index(neo4j.Node, "Users")

def __getUserByEmail(email) :
    userFound = __getUsersIndex().get("email", email)
    if userFound :
         return userFound[0]
    raise NotFoundError("User with email %s not found " % email)

def addContactToUser(currentUser, newContact) :
    currentUser = __getUserByEmail(currentUser)
    newContact = __getUserByEmail(newContact)
    getGraph().create((currentUser, "IS_FRIEND_OF", newContact))

def getContacts(email) :
    currentUser = __getUserByEmail(email)
    rels = list(getGraph().match(start_node=currentUser, rel_type="IS_FRIEND_OF"))
    contacts = []
    for rel in rels:
        contacts.append(rel.end_node.get_properties())
        #print getGraph().node(rel.end_node)
    return contacts


def __addToUsersIndex(email, newUser) :
     getGraph().get_or_create_index(neo4j.Node, "Users").add("email", email, newUser)
 

