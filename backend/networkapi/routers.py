from fastapi import APIRouter
from backend.dbapi.operations import (
    Operations,
)
from backend.networkapi import schema

router = APIRouter()


@router.get('/', response_model=list[schema.ShareResponse])
def getShares():
    result = Operations.getAllShares()
    return result


@router.get('/{shareId}', response_model=schema.ShareAndRepliesResponse)
def getReplies(shareId: int):
    share = Operations.getShareByShareId(shareId)
    replies = Operations.getReplyAllByShareId(shareId)
    return {"share": share, "replies": replies}

