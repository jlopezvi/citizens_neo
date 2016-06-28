from flask import Flask, jsonify, json, redirect, url_for
from crossdomain import crossdomain
from flask import request, send_from_directory
from flask.ext.assets import Environment, Bundle
import ast
import json, requests
from twython import Twython
from communityManager import saveCommunity, deleteCommunity, addCommunityToContact, getCommunities
from userManagement import deleteUser, getAllUsers, saveUser, addContactToUser, getContacts
from concernManager import addConcernToUser, deleteOneConcern, getAllConcerns
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__, static_folder='static')
assets = Environment(app)
assets.init_app(app)

APP_KEY = 'HhTmHEyWuutW83qtXTPzOM4zt'
APP_SECRET = 'VgDdNCHtIS0OYi9kh9BNZDu0Rvot7Y6kGf8GCXNUxPXf0BwVEz'
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(app.static_folder + '/js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(app.static_folder + '/css', path)


@app.route('/templates/<path:path>')
def send_templates(path):
    return send_from_directory(app.static_folder + '/templates', path)


@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory(app.static_folder + '/images', path)


@app.route('/app/<path:path>')
def send_app(path):
    return send_from_directory(app.static_folder + '/app', path)


@app.route('/sign-in-twitter', methods=['POST'])
def sign_in_twitter():
    global OAUTH_TOKEN, OAUTH_TOKEN_SECRET
    twitter = Twython(app_key=APP_KEY, app_secret=APP_SECRET)
    auth = twitter.get_authentication_tokens(callback_url='http://127.0.0.1:5000/oauth')

    OAUTH_TOKEN = auth['oauth_token']
    OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

    response = jsonify(auth)
    return response


@app.route('/oauth', methods=['GET'])
def oauth():
    oauth_verifier = request.args.get('oauth_verifier')
    global OAUTH_TOKEN, OAUTH_TOKEN_SECRET

    twitter = Twython(APP_KEY, APP_SECRET,
                      OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    final_step = twitter.get_authorized_tokens(oauth_verifier)

    OAUTH_TOKEN = final_step['oauth_token']
    OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

    response = jsonify(final_step)

    # redirect(url_for('root'))
    return response


@app.route('/tweet')
def tweet():

    t = Twython(
        app_key=APP_KEY,
        app_secret=APP_SECRET,
        oauth_token=OAUTH_TOKEN,
        oauth_token_secret=OAUTH_TOKEN_SECRET
    )

    status_update = t.update_status(status=request.args['status'])
    response = jsonify(status_update)

    return response


@app.route('/addUser', methods=['POST', 'OPTIONS'])
# @crossdomain(origin='*', headers=['Content-Type'])
def get_user():
    return saveUser(request.get_json())


@app.route('/addCommunity', methods=['POST', 'OPTIONS'])
def add_comunity():
    return saveCommunity(request.get_json())


@app.route('/addCommunityToUser/<string:name>/<string:email>', methods=['POST', 'OPTIONS'])
def add_community_to_user(name, email) :
    add_community_to_contact(name, email)
    return "Community %s was added to user with email %s" % (name, email)


@app.route('/delete/community/<string:name>', methods=['DELETE', 'OPTIONS'])
def removeCommunity(name):
    deleteCommunity(name)
    return "Community %s was successfully removed" % name


@app.route('/deleteUser/<string:email>', methods=['DELETE', 'OPTIONS'])
def removeUser(email):
    deleteUser(email)
    return "User with email %s was successfully removed" % email


@app.route('/getAllContactsForUser/<string:email>', methods=['GET', 'OPTIONS'])
def getAllContacts(email):
    return json.dumps(getContacts(email))


@app.route('/getCommunitiesOfUser/<string:email>', methods=['GET', 'OPTIONS'])
def getAllCommunitiesForUser(email):
    return json.dumps(getCommunities(email))


@app.route('/getUsers', methods=['GET', 'OPTIONS'])
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
    return "addConcern was invoked"


@app.route('/deleteConcern/<string:id_concern>', methods=['DELETE', 'OPTIONS'])
def deleteConcern(id_concern) :
    print(id_concern)
    deleteOneConcern(id_concern)
    return "deleteConcern was invoked"


@app.route('/getConcerns/<string:current>', methods=['GET', 'OPTIONS'])
def getConcerns(current):
    print (current)
    return json.dumps(getAllConcerns(current))

if __name__ == '__main__':
    app.debug = True
    app.run()
