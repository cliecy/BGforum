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


@router.post('/shares', response_model=schemas.ShareCreate)
def createShares(share: schemas.ShareCreate, user: schemas.UserResponse):
    Operations.createShareByObject(share)
    Operations.updateSharenumberbyObject(user)

@router.post('/shares/{shareId}', response_model=schemas.ReplyCreate)
def createReply(reply: schemas.ReplyCreate):
    Operations.createReplyByObject(reply)


@router.post('/users', response_model=schemas.UserCreate)
def registerUser(user: schemas.UserCreate):
    try:
        Operations.createUserbyObject(user)
    except user.password != user.passwordconfirm:
        raise HTTPException(status_code=400, detail='The password is not same in two times you inputted.')


@router.post('/users/login')
def UserLogin(user: schemas.UserLogin):
    return Operations.userLogin(user)
    
@router.get('/users/{userId}', response_model=schemas.UserResponse)
def getUser(userId: int):
    Operations.getUserByUserId(userId)

@router.post('/users/{userId}', response_model=schemas.UserResponse)
def userupdate(user: schemas.UserResponse):
    Operations.updateUser(user)

@router.get('/users/{userName}')
def getUserId(UserName: str):
    return Operations.getUserIdbyName(UserName)