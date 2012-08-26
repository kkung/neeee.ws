from sqlalchemy import orm
from sqlalchemy.ext import declarative

Session = orm.sessionmaker(autocommit=True)
Base = declarative.declarative_base()
