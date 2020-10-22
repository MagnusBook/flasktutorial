from flask import render_template
from flasktutorial import app, query_db


@app.route('/')
def index():
    articles = query_db('SELECT id, * FROM article;')
    return render_template('index.html', articles=articles)


@app.route('/article/<int:article_id>')
def article(article_id):
    article = query_db(
        'SELECT * FROM article WHERE id=%s;', (article_id), True)
    return render_template('article.html', article=article)
