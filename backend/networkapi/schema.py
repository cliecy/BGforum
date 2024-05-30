from datetime import datetime

from pydantic import BaseModel


class ShareBase(BaseModel):
    ShareId: int
    UserId: int
    Content: str
    Title: str
    PostTime: datetime
    IsLocked: bool



