from datetime import datetime
import json

from fastapi.openapi.models import Schema
from sqlalchemy import (
    String,
    Integer,
    DATETIME,
    select,
    ForeignKey
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)

from backend.api import Base, session


class Reply(Base):
    __tablename__ = 'reply'
    ReplyId: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ShareId: Mapped[int] = mapped_column(Integer, ForeignKey('shares.ShareId'))
    UserId: Mapped[int] = mapped_column(Integer)
    PostTime: Mapped[datetime] = mapped_column(DATETIME)
    ReplyTo: Mapped[int] = mapped_column(Integer, nullable=True)
    Content: Mapped[str] = mapped_column(String(10000))
    Floor: Mapped[int] = mapped_column(Integer)


class ReplyCRUD:
    @classmethod
    def createReply(cls, receivedJson, newSession):
        jsonDict = json.loads(receivedJson)
        date_format = "%Y-%m-%d %H:%M:%S"
        reply=Reply(
            ShareId=jsonDict['ShareId'],
            UserId=jsonDict['UserId'],
            PostTime=datetime.strptime(jsonDict['PostTime'], date_format),
            ReplyTo=jsonDict['ReplyTo'],
            Content=jsonDict['Content'],
            Floor=jsonDict['Floor'],
        )


