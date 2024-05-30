from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker
)

from backend.dbapi.models import Base
engine = create_engine('sqlite:///../bbs.db', echo=True)
session = sessionmaker(engine)


def getdb():
    return session()

