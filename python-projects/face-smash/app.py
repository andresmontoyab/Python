from flask import Flask, g, render_template, flash, url_for, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash
import models
import forms

DEBUG = True
PORT = 8181
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'sdhnlgndfjkgnsdSDFSDjfkgn324534@#!@$%fdlsgfsdSDFGS'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    try:
        return models.User.get(models.User.id == user_id)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    if not hasattr(g, 'db'):
        g.db = models.DATABASE
        g.db.connect()
        g.user = current_user

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash('Register finished ok')
        models.User.create_user(
            username = form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash('Email or password is not correct')
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('You are log in', 'success')
                return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout', methods=('GET', 'POST'))
@login_required
def logout():
    logout_user()
    flash('You are log out', 'success')
    return redirect(url_for('index'))

@app.route('/new_post', methods=('GET', 'POST'))
def post():
    form = forms.PostForm()
    if form.validate_on_submit():
        models.Posts.create(user=g.user._get_current_object(),
                           content=form.content.data.strip())
        flash("Post saved", 'success')
        return redirect(url_for('index'))
    return render_template('post.html', form= form)

@app.route(('/'))
def index():
    stream = models.Posts.select().limit(15)
    return render_template('stream.html', stream=stream)

@app.route('/stream')
@app.route('/stream/<username>')
def stream(username= None):
    template = 'stream.html'
    if username and username != current_user.username:
        user = models.User.select().where(models.User.username**username).get()
        stream = user.posts.limit(15)
        template = 'user_stream.html'
    else:
        stream = current_user.get_stream().limit(15)
        user = current_user
    if username:
        template = 'user_stream.html'
    return render_template(template, stream= stream, user= user)

@app.route('/follow/<username>')
@login_required
def follow(username):
    try:
        to_user = models.User.get(models.User.username**username)
    except models.DoesNotExist:
        pass
    else:
        try:
            models.Relationship.create(
                from_user= g.user._get_current_object(),
                to_user= to_user
            )
        except models.IntegrityError:
            pass
        else:
            flash('Now you are following to {}'.format(to_user.username), 'success')
    return redirect(url_for('stream', username=to_user.username))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    try:
        to_user = models.User.get(models.User.username**username)
    except models.DoesNotExist:
        pass
    else:
        try:
            relationship = models.Relationship.get(from_user= g.user._get_current_object(),to_user= to_user)
            if relationship:
                relationship.delete_instance()
        except models.IntegrityError:
            pass
        except models.DoesNotExist:
            flash('You are not following that user')
        else:
            flash('Now you are not following to {}'.format(to_user.username), 'success')
    return redirect(url_for('stream', username=to_user.username))

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)