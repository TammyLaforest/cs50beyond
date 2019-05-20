import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/')
@app.route('/index')
def index():
    books = db.execute("SELECT * FROM books").fetchall()
    authors = db.execute("SELECT * FROM authors").fetchall()
    return render_template('index.html', books=books, authors=authors)




@app.route('/all')
def all():

    return render_template('data.html',)

@app.route('/authors')
def authors():
    return render_template('index.html',)

@app.route('/books')
def books():
    return render_template('index.html',)

# @app.route("/<string:name2>")
# def hello(name1, name2="Josh"):
# 	name1=name1.capitalize()
# 	name2 = name2.capitalize()
# 	return f"Hello, {name1} and {name2}!"


if __name__ == '__main__':
    app.run()
