from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class ShareCreate(BaseModel):
    UserId: int
    Content: str
    Title: str
    PostTime: datetime
    IsLocked: bool = False


class ShareResponse(BaseModel):
    ShareId: int
    UserId: int
    Content: str
    Title: str
    PostTime: datetime
    IsLocked: bool

    class Config:
        from_attributes = True


class ReplyCreate(BaseModel):
    ShareId: int
    UserId: int
    PostTime: datetime
    ReplyTo: Optional[int] = None
    Content: str


class ReplyResponse(BaseModel):
    ReplyId: int
    ShareId: int
    UserId: int
    PostTime: datetime
    ReplyTo: Optional[int] = None
    Content: str
    Floor: int

    class Config:
        from_attributes = True


class ShareAndRepliesResponse(BaseModel):
    share: List[ShareResponse]
    replies: List[ReplyResponse]

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    #UserId: int
    LastLogintime: datetime
    UserName: str
    gender: str
    motto: str
    numofShares: int
    password: str


class UserResponse(BaseModel):
    UserId: int
    #UserClass: int
    LastLogintime: datetime
    UserName: str
    gender: str
    motto: str
    numofShares: int
    # password: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    UserName: str
    password: str

    class Config:
        from_attributes = True
