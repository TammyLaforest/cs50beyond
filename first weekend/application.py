from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/julia")
def julia():
	return "Hello, Julia. Julia doesn't like otters"

# @app.route("/<string:name>")
# def hello(name):
# 	name = name.capitalize()
# 	return f"Hello, {name}!"

@app.route("/<string:name1>/<string:name2>")
@app.route("/<string:name2>")
def hello(name1, name2="Josh"):
	name1=name1.capitalize()
	name2 = name2.capitalize()
	return f"Hello, {name1} and {name2}!"