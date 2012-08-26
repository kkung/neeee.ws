from flask import Blueprint, render_template, g, request, redirect, url_for
from .models import News, NewsForm

news = Blueprint('news', __name__)


@news.route('/')
def index():
    news = g.session.query(News).all()
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
