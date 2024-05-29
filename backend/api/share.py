from datetime import datetime
import json
from sqlalchemy import (
    select,
    update
)


from backend.api import Share, session


class ShareCURD:
    @classmethod
    def createShare(cls, receivedJson: str, newSession):
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
    def getShareByShareId(cls, shareId: int, newSession):
        with newSession() as s:
            stmt = select(Share).where(Share.ShareId == shareId)
            result = s.scalars(stmt).all()
            return result

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
            s.commit()

    @classmethod
    def updateShareByShareId(cls, shareId, newContent, newSession):
        with newSession() as s:
            stmt = update(Share).where(Share.ShareId == shareId).values(content=newContent)
            s.execute(stmt)
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
    shares = ShareCURD.getAllShares(session)
    for s in shares:
        print(s.ShareId, s.UserId, s.Content, s.Title, s.PostTime)




