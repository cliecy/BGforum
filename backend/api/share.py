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


def createShare(receivedJson, newSession):
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


def getShareByShareId(shareId, newSession):
    with newSession() as s:
        stmt = select(Share).where(Share.ShareId == shareId)
        result = s.scalars(stmt).all()
        return result


def getAllShares(newSession):
    with newSession() as s:
        stmt = select(Share).order_by(Share.ShareId)
        result = s.execute(stmt).scalars().all()
        for i in result:
            print(i)
        return result


def deleteShareByShareId(shareId, newSession):
    with newSession() as s:
        stmt = select(Share).where(Share.ShareId == shareId)
        result = s.execute(stmt).scalars().all()
        for share in result:
            s.delete(share)
        s.commit()


if __name__ == '__main__':
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
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    mainshare = ('{"ShareId":null,'
                 '"UserId":2, '
                 '"Content":"World",'
                 '"Title":"Hello", '
                 '"PostTime":"2024-05-29 00:00:00",'
                 '"Floor":2, '
                 '"IsLocked":false}')
    createShare(mainshare, session)
    deleteShareByShareId(2, session)
    shares = getAllShares(session)
    for s in shares:
        print(s.ShareId, s.UserId, s.Content, s.Title, s.PostTime)




