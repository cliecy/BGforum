from .reply import BasicReplyCRUD
from .share import BasicShareCRUD


class Operations(BasicReplyCRUD, BasicShareCRUD):
    @classmethod
    def deleteWholeShare(cls, shareId):
        cls.deleteReplyByObject(shareId)
