from flask import Flask, g
from flask_login import LoginManager
import models

DEBUG = True
PORT = 8181
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'sdhnlgndfjkgnsdSDFSDjfkgn324534@#!@$%fdlsgfsdSDFGS'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view('login')

@login_manager.user_loader
def load_user(user_id):
    try:
        return models.User.get(models.User.id == user_id)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    if not hasattr(g, 'db'):
        g.db = models.DB
        g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response


if __name__ == '__MAIN':
    models.initialize()
    models.User.create_user(
        name = 'Andres',
        email = 'Andres@gmail.com',
        password = 'thepassword123'
    )
    app.run(debug=DEBUG, host=HOST, port=PORT)