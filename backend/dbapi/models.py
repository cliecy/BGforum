from datetime import datetime

from sqlalchemy import Integer, String, DATETIME, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from backend.dbapi.database import engine


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
    Replies = relationship("Reply", backref="Share")


class Reply(Base):
    __tablename__ = 'reply'
    ReplyId: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ShareId: Mapped[int] = mapped_column(Integer, ForeignKey('shares.ShareId'), index=True)
    UserId: Mapped[int] = mapped_column(Integer)
    PostTime: Mapped[datetime] = mapped_column(DATETIME)
    ReplyTo: Mapped[int] = mapped_column(Integer, nullable=True)
    Content: Mapped[str] = mapped_column(String(10000))
    Floor: Mapped[int] = mapped_column(Integer)


class User(Base):
    __tablename__ = "User"
    UserId: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=True, autoincrement=True)
    UserClass: Mapped[int] = mapped_column(Boolean, nullable=False, default=False)
    UserName: Mapped[str] = mapped_column(String(10000), nullable=False)
    motto: Mapped[str] = mapped_column(String(10000))
    LastLogintime: Mapped[datetime] = mapped_column(DATETIME, nullable=False)
    gender: Mapped[int] = mapped_column(Integer, nullable=False)
    password: Mapped[str] = mapped_column(String(10000), nullable=False)
    numofShares: Mapped[int] = mapped_column(Integer, nullable=False)


Base.metadata.create_all(bind=engine)
