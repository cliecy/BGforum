from fastapi import FastAPI
from datetime import datetime
import json
from sqlalchemy import (
    create_engine,
    String,
    Integer,
    DATETIME,
    select, ForeignKey
)
from sqlalchemy.orm import (
    sessionmaker,
    DeclarativeBase,
    Mapped,
    mapped_column
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
    ShareId: Mapped[int] = mapped_column(Integer, ForeignKey('shares.ShareId'))
    UserId: Mapped[int] = mapped_column(Integer)
    PostTime: Mapped[datetime] = mapped_column(DATETIME)
    ReplyTo: Mapped[int] = mapped_column(Integer, nullable=True)
    Content: Mapped[str] = mapped_column(String(10000))
    Floor: Mapped[int] = mapped_column(Integer)


# 创建engine
engine = create_engine('sqlite:///bbs.db', echo=True)
newSession = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


def createShare(receivedJson):
    jsonDict = json.loads(receivedJson)
    date_format = "%Y-%m-%d %H:%M:%S"
    share = Share(
        ShareId=jsonDict['ShareId'],
        UserId=jsonDict['UserId'],
        Content=jsonDict['Content'],
        Title=jsonDict['Title'],
        PostTime=datetime.strptime(jsonDict['PostTime'], date_format),
        IsLocked=jsonDict['IsLocked'],
    )
    with newSession() as s:
        s.add(share)
        s.commit()


def getShareByShareId(shareId):
    with newSession() as s:
        stmt = select(Share).where(Share.ShareId == shareId).order_by(Share.Floor)
        result = s.scalars(stmt).all()
        return result


def getAllShares():
    with newSession() as s:
        stmt = select(Share).order_by(Share.ShareId)
        result = s.execute(stmt).scalars().all()
        for i in result:
            print(i)
        return result


def deleteShareByShareId(shareId):
    with newSession() as s:
        stmt = select(Share).where(Share.ShareId == shareId)
        result = s.execute(stmt)
        for share in result:
            s.delete(share)
        s.commit()


if __name__ == '__main__':
    mainshare = ('{"ShareId":null,'
                 '"UserId":2, '
                 '"Content":"World",'
                 '"Title":"Hello", '
                 '"PostTime":"2024-05-29 00:00:00",'
                 '"Floor":2, '
                 '"IsLocked":false}')
    createShare(mainshare)
    deleteShareByShareId(1)
    shares = getAllShares()
    for s in shares:
        print(s.ShareId, s.UserId, s.Content, s.Title, s.PostTime)

app = FastAPI()


@app.get("/shares/{shareId}")
async def getShare(shareId: int):
    shares = getShareByShareId(shareId)
    if shares:
        share = shares[0]
        return {
            "ShareId": share.ShareId,
            "UserId": share.UserId,
            "Content": share.Content,
            "Title": share.Title,
            "PostTime": share.PostTime,
            "IsLocked": share.IsLocked
        }
    return {"error": "Share not found"}