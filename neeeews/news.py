from flask import Blueprint, render_template, g, request, redirect, url_for
from .models import News, NewsForm

news = Blueprint('news', __name__)


@news.route('/')
def index():
    news = sorted(g.session.query(News).all(), key=lambda item: item.score)
    return render_template('index.html', news=news)


@news.route('/submit', methods=['GET', 'POST'])
def submit():
    form = NewsForm(request.form)
    if request.method == 'POST' and form.validate():
        news = News(
            title=form.title.data,
            link=form.link.data)
        with g.session.begin():
            g.session.add(news)

        return redirect(url_for('news.index'))

    return render_template('submit.html', form=form)


@news.route('/<int:id>/vote/<any(up, down):vote_dir>', methods=['POST'])
def vote(id, vote_dir):
    news = g.session.query(News).get(id)
    if news is None:
        abort(404)

    if vote_dir == "up":
        g.session.query(News).update({News.votes: News.votes + 1})
    else:
        g.session.query(News).update({News.votes: News.votes - 1})
    return redirect(url_for('news.index'))
