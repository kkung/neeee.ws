from sqlalchemy import *
from sqlalchemy import orm
from sqlalchemy.sql import functions
from wtforms import Form, TextField, validators
from . import database


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


class NewsForm(Form):
    title = TextField('Title', [validators.Required()])
    link = TextField('URL', [
        validators.Length(max=512),
        validators.Optional()])
