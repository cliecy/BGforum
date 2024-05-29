from datetime import datetime
import json
from sqlalchemy import (
    select,
    update,
    and_
)

from backend.api import Reply, session


class ReplyCRUD:
    @classmethod
    def createReply(cls, receivedJson, newSession):
        jsonDict = json.loads(receivedJson)
        date_format = "%Y-%m-%d %H:%M:%S"
        reply = Reply(
            ShareId=jsonDict['ShareId'],
            UserId=jsonDict['UserId'],
            PostTime=datetime.strptime(jsonDict['PostTime'], date_format),
            ReplyTo=jsonDict['ReplyTo'],
            Content=jsonDict['Content'],
            Floor=jsonDict['Floor'],
        )

        with newSession() as s:
            s.add(reply)
            s.commit()

    # 查询一个帖子下的所有回复
    @classmethod
    def getReplyAll(cls, shareId, newSession):
        with newSession() as s:
            stmt = select(Reply).where(Reply.ShareId == shareId).order_by(Reply.Floor.asc())
            result = s.execute(stmt).scalars().all()
            return result

    # 查询一个帖子中的特定楼层
    @classmethod
    def getReplySpecific(cls, shareId, floor, newSession):
        with newSession() as s:
            stmt = select(Reply).where(and_(Reply.Floor == floor, Reply.ShareId == shareId))
            result = s.execute(stmt).scalars().all()
            return result

    @classmethod
    def deleteReply(cls, shareId, floor, newSession):
        with newSession() as s:
            stmt = select(Reply).where(and_(Reply.Floor == floor, Reply.ShareId == shareId))
            result = s.execute(stmt).scalars().all()
            s.delete(result[0])
            s.commit()

    @classmethod
    def updateReply(cls, shareId, floor, newContent, newSession):
        with newSession() as s:
            stmt = update(Reply).where(and_(Reply.Floor == floor, Reply.ShareId == shareId)).values(content=newContent)
            s.execute(stmt)
            s.commit()


if __name__ == '__main__':
    r1 = '{"ShareId":1, "UserId":1, "PostTime":"2024-05-30 01:00:00", "ReplyTo":1, "Content":"First reply", "Floor":2}'
    ReplyCRUD.createReply(r1, session)
    replies = ReplyCRUD.getReplyAll(2, session)
    for r in replies:
        print(r.ReplyId, r.ShareId, r.UserId, r.PostTime, r.Content, r.Floor)

