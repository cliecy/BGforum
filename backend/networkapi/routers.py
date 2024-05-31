from fastapi import APIRouter
from ..dbapi.operations import (
    Operations,
)
from ..networkapi import schemas

router = APIRouter()


@router.get('/', response_model=list[schemas.ShareResponse])
def getShares():
    result = Operations.getAllShares()
    return result


@router.get('/{shareId}', response_model=schemas.ShareAndRepliesResponse)
def getReplies(shareId: int):
    share = Operations.getShareByShareId(shareId)
    replies = Operations.getReplyAllByShareId(shareId)
    return {"share": share, "replies": replies}


@router.post('/', response_model=schemas.ShareCreate)
def createShares(share: schemas.ShareCreate):
    Operations.createShareByObject(share)


@router.post('/{shareId}', response_model=schemas.ReplyCreate)
def createReply(reply: schemas.ReplyCreate):
    Operations.createReplyByObject(reply)
