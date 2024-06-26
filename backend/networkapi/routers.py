from fastapi import APIRouter
from ..dbapi.operations import (
    Operations,
)
from ..networkapi import schemas
from fastapi import HTTPException
router = APIRouter()


@router.get('/shares', response_model=list[schemas.ShareResponse])
def getShares():
    result = Operations.getAllShares()
    return result


@router.get('/shares/{shareId}', response_model=schemas.ShareAndRepliesResponse)
def getReplies(shareId: int):
    share = Operations.getShareByShareId(shareId)
    replies = Operations.getReplyAllByShareId(shareId)
    return {"share": share, "replies": replies}


@router.post('/shares')
def createShares(share: schemas.ShareCreate):
    print("HELLO WORLD")
    Operations.createShareByObject(share)
    # Operations.updateSharenumberbyObject(user)

@router.post('/shares/{shareId}')
def createReply(reply: schemas.ReplyCreate):
    Operations.createReplyByObject(reply)


@router.post('/users')
def registerUser(user: schemas.UserCreate):
    return Operations.createUserbyObject(user)

@router.post('/users/login')
def UserLogin(user: schemas.UserLogin):
    return Operations.userLogin(user)
    
@router.get('/user/{userId}', response_model=schemas.UserResponse)
def getUser(userId: int):
    return Operations.getUserByUserId(userId)

@router.post('/users/{userId}', response_model=schemas.UserResponse)
def userupdate(user: schemas.UserResponse):
    return Operations.updateUser(user)

@router.get('/users/{UserName}') 
def getUserId(UserName: str):
    return Operations.getUserIdbyName(UserName)