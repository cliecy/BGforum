from datetime import datetime
import json
from sqlalchemy import (
    select,
    update
)
from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound

from backend.dbapi.models import Share
from backend.dbapi.database import getdb
from backend.networkapi import schemas




class BasicShareCRUD:
    @classmethod
    def createShareByJson(cls, receivedJson: str):
        s = getdb()
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
        s.add(share)
        s.commit()

    @classmethod
    def createShareByObject(cls, postedShare: schemas.ShareCreate):
        s = getdb()
        dbShare = Share(
            UserId=postedShare.UserId,
            Content=postedShare.Content,
            Title=postedShare.Title,
            PostTime=postedShare.PostTime,
            IsLocked=postedShare.IsLocked,
        )
        s.add(dbShare)
        s.commit()

    @classmethod
    def getShareByShareId(cls, shareId: int):
        s = getdb()
        stmt = select(Share).where(Share.ShareId == shareId)
        try:
            result = s.scalars(stmt).all()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Share not found")
        return result

    @classmethod
    def getAllShares(cls):
        s = getdb()
        stmt = select(Share).order_by(Share.ShareId)
        try:
            result = s.execute(stmt).scalars().all()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Database Empty")
        return result

    @classmethod
    def deleteShareByShareId(cls, shareId):
        s = getdb()
        stmt = select(Share).where(Share.ShareId == shareId)
        result = s.execute(stmt).scalars().all()
        for share in result:
            s.delete(share)
        s.commit()

    @classmethod
    def updateShareByShareId(cls, shareId, newContent):
        s = getdb()
        try:
            stmt = select(Share).where(Share.ShareId == shareId)
            result = s.execute(stmt).scalars().first()
            if result.IsLocked:
                raise HTTPException(status_code=404, detail="Share has been locked")
            stmt = update(Share).where(Share.ShareId == shareId).values(content=newContent)
            s.execute(stmt)
            s.commit()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Share not found")

    @classmethod
    def userLogin(cls, userinfo: schemas.UserLogin):
        try:
            username = userinfo.username
        except HTTPException as e:
            raise
if __name__ == '__main__':
    mainshare = ('{"ShareId":null,'
                 '"UserId":2, '
                 '"Content":"World",'
                 '"Title":"Hello", '
                 '"PostTime":"2024-05-29 00:00:00",'
                 '"Floor":2, '
                 '"IsLocked":false}')
    BasicShareCRUD.createShareByJson(mainshare)
    shares = BasicShareCRUD.getAllShares()
    for sh in shares:
        print(sh.ShareId, sh.UserId, sh.Content, sh.Title, sh.PostTime)



