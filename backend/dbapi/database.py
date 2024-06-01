from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker
)

engine = create_engine('sqlite:///backend/bbs.db', echo=True, pool_size=1000000)
session = sessionmaker(engine)


def getdb():
    return session()

