import datetime
from flasktutorial import app
from flask import render_template

articles = [{'id': 1, 'title': 'Something bad happened today!', 'text': 'Today was a bad day',
             'date': datetime.date(1999, 4, 12)}, {'id': 2, 'title': 'Something good happened today!', 'text': 'Today was a good day',
                                                   'date': datetime.date(2004, 6, 1)}]


@app.route('/')
def index():
    return render_template('index.html', articles=articles)


@app.route('/article/<int:article_id>')
def article(article_id):
    return render_template('article.html', article=articles[article_id - 1])
