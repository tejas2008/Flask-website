from flask import render_template, url_for, flash, redirect, request, abort
from flaskwebsite import app, db
<<<<<<< HEAD
from flaskwebsite.forms import ReviewForm
=======
>>>>>>> 632c4eab63ff304961942d4f2b0680a0b0dc41ac
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
    form=ReviewForm()
    return render_template("reviews.html",form=form)

