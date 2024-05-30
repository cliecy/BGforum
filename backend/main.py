from fastapi import FastAPI
from networkapi.routers import router

app = FastAPI()

app.include_router(router, prefix="/shares", tags=["shares"])

if __name__=='__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)