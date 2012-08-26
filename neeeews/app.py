# coding=utf-8
from flask import Flask, render_template, g
import werkzeug
import sqlalchemy
from . import database


blueprints = {'neeeews.news:news': {}}


def create_app(config_file=None):
    app = Flask(__name__)
    app.config.from_object('default_settings')
    if config_file is not None:
        app.config.from_pyfile(config_file)

    bps = dict(blueprints)
    bps.update(app.config.get('BLUEPRINTS', {}))
    for im, kwargs in bps.iteritems():
        bp = werkzeug.utils.import_string(im)
        app.register_blueprint(bp, **(kwargs or {}))

    @app.before_request
    def attach_database():
        engine = app.config['ENGINE']
        g.database_engine = sqlalchemy.create_engine(engine)
        g.session = database.Session(bind=g.database_engine)

    return app
