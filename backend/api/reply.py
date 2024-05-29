from datetime import datetime
import json
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



