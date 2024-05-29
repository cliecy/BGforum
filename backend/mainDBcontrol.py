from sqlalchemy import (
    create_engine
)
from sqlalchemy.orm import (
    sessionmaker,
    DeclarativeBase
)


class Base(DeclarativeBase):
    pass


# 创建engine
engine = create_engine('sqlite:///bbs.db', echo=True)
newSession = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

