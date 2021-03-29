from flask import Flask, render_template
from flask import request

app = Flask(__name__)

# Basic Routes
@app.route('/')
def index():
    return 'Hello World, First App Flask '

# Query Parameters
@app.route('/search_with_query_param')
def search(name ='Mundo', lastname = 'Default'):
    name = request.args.get('name')
    lastname = request.args.get('lastname')
    return 'Hola {} {}'.format(name, lastname)

#Path Params
@app.route('/search_with_path_param/<name>')
def search_path_param(name):
    return 'By Path Param {}'.format(name)

@app.route('/add/<float:num_one>/<float:num_two>')
@app.route('/add/<float:num_one>/<int:num_two>')
@app.route('/add/<int:num_one>/<int:num_two>')
@app.route('/add/<int:num_one>/<float:num_two>')
def add(num_one, num_two):
    context = {
        'num1': num_one,
        'num2': num_two,
    }
    #return render_template("add.html", num1= num_one, num2=num_two)
    return render_template("add.html", **context)

app.run(debug=True, port = 8099, host = '0.0.0.0')
