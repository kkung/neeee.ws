from sqlalchemy import *
from sqlalchemy import orm
from sqlalchemy.sql import functions
from wtforms import Form, TextField, validators
from . import database
from datetime import datetime


class News(database.Base):
    """"""

    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)

    title = Column(Unicode(512), nullable=False)

    link = Column(Unicode(512))

    created_at = Column(
        DateTime(timezone=True),
        default=functions.now(),
        index=True)

    votes = Column(Integer, default=0)

    @property
    def hour_age(self):
        return (datetime.utcnow() - self.created_at).total_seconds() / 60 / 60

    @property
    def score(self, gravity=1.8):
        return (self.votes - 1) / pow((self.hour_age + 2), gravity)

    @property
    def domain(self):
        from urlparse import urlparse
        return urlparse(self.link).hostname


class NewsForm(Form):
    title = TextField('Title', [validators.Required()])
    link = TextField('URL', [
        validators.Length(max=512),
        validators.Optional()])
