# Flask

All about Flask Framework

Flask is a micro web framework written in Python. It is classified as a 
microframework because it does not require particular tools or libraries


## Install Flask

In order to install flask we are going to use ```pip```

```shell
pip install flask
```

With the above command we should have flask installed and ready to use.


### Start up Flask Application

In order to start Flask server we just need to write the next lines of code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)
```

### Playing with templates

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% block head %} {% endblock %}
</head>
<body>
    {% block body %} {% endblock %}
</body>
</html>
```


```html
{% extends 'base.html' %}

{% block head %}
<title> Home </title>
{% endblock %}

{% block body %}
<h2> Home Page</h2>
{% endblock %}
```

#### Passing data to templates

In order to send data to our template we can do it in then next way

```python
from flask import Flask, render_template

app = Flask(__name__)
all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1. Lalalala'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of post 2. Lalalalasss'
    },
]

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)
```

As you can see we pass the posts variable to our template. So in 
our template we are going to have that variable

In order to use the information that we receive we need to use jinja2 syntax


```html
{% extends 'base.html' %}

{% block head %}
<title> Posts </title>
{% endblock %}

{% block body %}
<h2> All Posts </h2>
    {% for post in posts %}
        <h2>{{post.title}}</h2>
        <h3>{{post.content}}</h3>
    {% endfor %}
{% endblock %}
```

## Database

As we said before Flask is a very lighweight microframework
so it does not have a database, nevertheless we can use a third party
in order to deal with databases.

### SQL Alchemy

In order to install flask sql alchemy we can use the nexr command

```shell
pip install flask-sqlalchemy
```