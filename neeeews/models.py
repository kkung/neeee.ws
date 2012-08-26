from sqlalchemy import *
from sqlalchemy import orm
from sqlalchemy.sql import functions
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
