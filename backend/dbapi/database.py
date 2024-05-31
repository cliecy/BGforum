from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker
)

engine = create_engine('sqlite:////Users/guanjiezou/bgforum/backend/bbs.db', echo=True)
session = sessionmaker(engine)


def getdb():
    return session()

