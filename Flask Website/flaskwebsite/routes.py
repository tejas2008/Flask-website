from flask import render_template, url_for, flash, redirect, request, abort
from flaskwebsite import app, db, bcrypt
from flaskwebsite.forms import ReviewForm
from flaskwebsite.models import Post
@app.route('/')
def homepage():
    return render_template("index.html")
@app.route('/books')
def bookpage():
    return render_template("books.html")
@app.route('/movies')
def moviepage():
    return render_template("movies.html")
@app.route('/faq')
def faqpage():
    return render_template("faq.html")
@app.route('/reviews')
def reviewpage():
    return render_template("reviews.html")