from fastapi import APIRouter
from backend.dbapi.operations import (
    Operations,
)


router = APIRouter()


@router.get('/shares')
def getShares():
    Operations.getAllShares()

@router.get('/shares/{shareId}')
def getReplies(shareId: int):
    Operations.getReplyAllByShareId(shareId)

