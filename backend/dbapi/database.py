from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker
)

engine = create_engine('sqlite:////Users/frankzhu/Desktop/Work/Employment/BBS/BGforum/backend/bbs.db', echo=True)
session = sessionmaker(engine)


def getdb():
    return session()

