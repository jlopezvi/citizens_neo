from flask import Flask, request, jsonify
from twython import Twython

app = Flask(__name__)

app_key = "HhTmHEyWuutW83qtXTPzOM4zt"
app_secret = "VgDdNCHtIS0OYi9kh9BNZDu0Rvot7Y6kGf8GCXNUxPXf0BwVEz"


@app.route("/")
def help_page():
    return "This is the home page"


@app.route("/login")
def login_url():

    t = Twython(
        app_key=app_key,
        app_secret=app_secret,
        callback_url=request.args['url']
    )

    auth_props = t.get_authentication_tokens()
    response = jsonify(auth_props)

    if (request.args['callback']):
        response.data = request.args['callback']+"("+response.data+")"

    return response


@app.route("/confirm")
def confirm_creds():

    t = Twython(
        app_key=app_key,
        app_secret=app_secret,
        oauth_token=request.args['oauth_token'],
        oauth_token_secret=request.args['oauth_token_secret']
    )

    auth_tokens = t.get_authorized_tokens()
    response = jsonify(auth_tokens)

    if (request.args['callback']):
        response.data = request.args['callback']+"("+response.data+")"

    return response


@app.route("/tweet")
def tweet():

    t = Twython(
        app_key=app_key,
        app_secret=app_secret,
        oauth_token=request.args['oauth'],
        oauth_token_secret=request.args['token']
    )

    status_update = t.updateStatus(status=request.args['status'])
    response = jsonify(status_update)

    if (request.args['callback']):
        response.data = request.args['callback']+"("+response.data+")"

    return response


@app.route("/search")
def search():

    t = Twython(
        app_key=app_key,
        app_secret=app_secret,
        oauth_token=request.args['oauth'],
        oauth_token_secret=request.args['token']
    )

    search = t.search(q=request.args['q'])
    response = jsonify(t)
    #
    # 	if (request.args['callback']):
    # 		response.data = request.args['callback']+"("+response.data+")"
    #
    return "This far"


if __name__ == "__main__":
    app.run()


