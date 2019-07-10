
'''@app.route('/')
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
    return render_template("reviews.html")'''
from flaskwebsite import app
if __name__ == '__main__':
    app.run(debug=True)
#run
