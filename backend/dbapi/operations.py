from .reply import BasicReplyCRUD
from .share import BasicShareCRUD
from .user import UserCURD


class Operations(BasicReplyCRUD, BasicShareCRUD, UserCURD):
    @classmethod
    def deleteWholeShare(cls, shareId):
        cls.deleteReplyByObject(shareId)
