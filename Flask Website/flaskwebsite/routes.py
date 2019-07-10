from flask import Flask render_template, url_for, flash, redirect, request, abort
from flaskwebsite import app, db
from flaskwebsite.forms import PostForm
from flaskwebsite import app, db, bcrypt
from flaskwebsite.forms import ReviewForm
from flaskwebsite.models import Post
app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template("index.html")
@app.route('/books')
def bookpage():
    return render_template("books.html")
@app.route('/movies1')
def moviepage1():
    return render_template("movies1.html")
@app.route('/movies2')
def moviepage2():
    return render_template("movies2.html")
@app.route('/faq')
def faqpage():
    return render_template("faq.html")


@app.route('/reviews')
def reviewpage():
    return render_template("reviews.html")

if __name__ == '__main__':
    app.run(debug=True)