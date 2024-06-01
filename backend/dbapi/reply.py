from datetime import datetime
import json
from sqlalchemy import (
    select,
    update,
    and_
)
from ..dbapi.models import Reply
from ..dbapi.database import getdb

# CRUD of replies
class BasicReplyCRUD:
    @classmethod
    def createReplyByJson(cls, receivedJson):
        s = getdb()
        jsonDict = json.loads(receivedJson)
        date_format = "%Y-%m-%d %H:%M:%S"
        prevReplies = cls.getReplyAllByShareId(jsonDict['ShareId'])
        reply = Reply(
            ShareId=jsonDict['ShareId'],
            UserId=jsonDict['UserId'],
            PostTime=datetime.strptime(jsonDict['PostTime'], date_format),
            ReplyTo=jsonDict['ReplyTo'],
            Content=jsonDict['Content'],
            Floor=len(prevReplies)+1,
        )

        s.add(reply)
        s.commit()
        s.close()

    # from a pydantic object creates a reply
    @classmethod
    def createReplyByObject(cls, postedReply):
        s = getdb()
        prevReplies = cls.getReplyAllByShareId(postedReply.ShareId)
        dbReply = Reply(
            ShareId=postedReply.ShareId,
            UserId=postedReply.UserId,
            PostTime=postedReply.PostTime,
            ReplyTo=postedReply.ReplyTo,
            Content=postedReply.Content,
            Floor=len(prevReplies)+1,
        )
        s.add(dbReply)
        s.commit()
        s.close()

    # 查询一个帖子下的所有回复
    @classmethod
    def getReplyAllByShareId(cls, shareId):
        s = getdb()
        stmt = select(Reply).where(Reply.ShareId == shareId).order_by(Reply.Floor.asc())
        result = s.execute(stmt).scalars().all()
        s.close()
        return result

    # 查询一个帖子中的特定楼层
    @classmethod
    def getReplySpecific(cls, shareId, floor):
        s = getdb()
        stmt = select(Reply).where(and_(Reply.Floor == floor, Reply.ShareId == shareId))
        result = s.execute(stmt).scalars().all()
        s.close()
        return result

    # locate a specified reply by share id and its floor
    @classmethod
    def deleteReplyByLocation(cls, shareId, floor):
        s = getdb()
        stmt = select(Reply).where(and_(Reply.Floor == floor, Reply.ShareId == shareId))
        result = s.execute(stmt).scalars().all()
        s.delete(result[0])
        s.commit()
        s.close()

    # receive a pydantic object and create a reply
    @classmethod
    def deleteReplyByObject(cls, obj):
        s = getdb()
        stmt = select(Reply).where(and_(Reply.ShareId == obj.ShareId, Reply.Floor == obj.Floor))
        result = s.execute(stmt).scalars().all()
        for i in result:
            s.delete(i)
        s.commit()
        s.close()

    @classmethod
    def updateReply(cls, shareId, floor, newContent):
        s = getdb()
        stmt = update(Reply).where(and_(Reply.Floor == floor, Reply.ShareId == shareId)).values(Content=newContent)
        s.execute(stmt)
        s.commit()
        s.close()


if __name__ == '__main__':
    r1 = '{"ShareId":1, "UserId":1, "PostTime":"2024-05-30 01:00:00", "ReplyTo":1, "Content":"First reply"}'
    BasicReplyCRUD.createReplyByJson(r1)
    #BasicReplyCRUD.updateReply(1, 2, "updated reply")
    #replies = BasicReplyCRUD.getReplyAll(1)
    #for r in replies:
    #    BasicReplyCRUD.deleteReplyByObject(r)

    replies = BasicReplyCRUD.getReplyAllByShareId(1)
    for r in replies:
        print(r.ReplyId, r.ShareId, r.UserId, r.PostTime, r.Content, r.Floor)

