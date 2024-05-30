from backend.dbapi import (
    models,
)
from .reply import BasicReplyCRUD
from .share import BasicShareCRUD


class Operations(BasicReplyCRUD, BasicShareCRUD):
    @classmethod
    def getWholeShare(cls, shareId):
        top = cls.getShareByShareId(shareId)
        replies = cls.getReplyAllByShareId(shareId)
        return top, replies

    @classmethod
    def deleteWholeShare(cls, shareId):
        cls.deleteReplyByObject(shareId)

    @classmethod
    def createReply(cls, shareId):
        top = cls.getShareByShareId(shareId)