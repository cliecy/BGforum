from fastapi import FastAPI
from backend.dbapi.share import (
    getShareByShareId,
)


app = FastAPI()


@app.get("/shares/{shareId}")
async def getShare(shareId: int):
    shares = getShareByShareId(shareId)
    if shares:
        share = shares[0]
        return {
            "ShareId": share.ShareId,
            "UserId": share.UserId,
            "Content": share.Content,
            "Title": share.Title,
            "PostTime": share.PostTime,
            "IsLocked": share.IsLocked
        }
    return {"error": "Share not found"}