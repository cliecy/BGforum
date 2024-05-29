from datetime import datetime
import json
from sqlalchemy import (
    String,
    Integer,
    DATETIME,
    select,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from backend.api import Base, session
from backend.api.reply import Reply


class Share(Base):
    __tablename__ = 'shares'

    ShareId: Mapped[int] = mapped_column(Integer, primary_key=True)
    UserId: Mapped[int] = mapped_column(Integer)
    Content: Mapped[str] = mapped_column(String(10000))
    Title: Mapped[str] = mapped_column(String(50))
    PostTime: Mapped[datetime] = mapped_column(DATETIME)
    IsLocked: Mapped[bool] = mapped_column(Integer, default=False)


class ShareCURD:
    @classmethod
    def createShare(cls, receivedJson, newSession):
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

    @classmethod
    def getShareByShareId(cls, shareId, newSession):
        with newSession() as s:
            stmt = select(Share).where(Share.ShareId == shareId)
            result = s.scalars(stmt).all()
            stmt = select(Reply).where(Reply.ShareId == shareId).order_by(Reply.PostTime.desc())
            replies = s.scalars(stmt).all()
            return result, replies

    @classmethod
    def getAllShares(cls, newSession):
        with newSession() as s:
            stmt = select(Share).order_by(Share.ShareId)
            result = s.execute(stmt).scalars().all()
            return result

    @classmethod
    def deleteShareByShareId(cls, shareId, newSession):
        with newSession() as s:
            stmt = select(Share).where(Share.ShareId == shareId)
            result = s.execute(stmt).scalars().all()
            for share in result:
                s.delete(share)

            stmt = select(Reply).where(Reply.ShareId == shareId)
            result = s.execute(stmt).scalars().all()
            for reply in result:
                s.delete(reply)

            s.commit()


if __name__ == '__main__':
    mainshare = ('{"ShareId":null,'
                 '"UserId":2, '
                 '"Content":"World",'
                 '"Title":"Hello", '
                 '"PostTime":"2024-05-29 00:00:00",'
                 '"Floor":2, '
                 '"IsLocked":false}')
    #ShareCURD.createShare(mainshare, session)
    #ShareCURD.deleteShareByShareId(2, session)
    #shares = ShareCURD.getAllShares(session)
    main=ShareCURD.getShareByShareId(3, session)
    shares
    for s in shares:
        print(s.ShareId, s.UserId, s.Content, s.Title, s.PostTime)




