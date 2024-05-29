from datetime import datetime

from sqlalchemy import create_engine, Integer, DATETIME, ForeignKey, String
from sqlalchemy.orm import (
    sessionmaker,
    DeclarativeBase, Mapped, mapped_column
)


class Base(DeclarativeBase):
    pass


class Share(Base):
    __tablename__ = 'shares'

    ShareId: Mapped[int] = mapped_column(Integer, primary_key=True)
    UserId: Mapped[int] = mapped_column(Integer)
    Content: Mapped[str] = mapped_column(String(10000))
    Title: Mapped[str] = mapped_column(String(50))
    PostTime: Mapped[datetime] = mapped_column(DATETIME)
    IsLocked: Mapped[bool] = mapped_column(Integer, default=False)


class Reply(Base):
    __tablename__ = 'reply'
    ReplyId: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ShareId: Mapped[int] = mapped_column(Integer, ForeignKey('shares.ShareId'), index=True)
    UserId: Mapped[int] = mapped_column(Integer)
    PostTime: Mapped[datetime] = mapped_column(DATETIME)
    ReplyTo: Mapped[int] = mapped_column(Integer, nullable=True)
    Content: Mapped[str] = mapped_column(String(10000))
    Floor: Mapped[int] = mapped_column(Integer)


engine = create_engine('sqlite:///../bbs.db', echo=True)
session = sessionmaker(engine)
Base.metadata.create_all(bind=engine)
