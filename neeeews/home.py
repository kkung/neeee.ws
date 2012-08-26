from flask import Blueprint, render_template, g
from .models import News

home = Blueprint('home', __name__)


@home.route('/')
def index():
    news = g.session.query(News).all()
    return render_template('index.html', news=news)
