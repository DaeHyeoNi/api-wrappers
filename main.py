from fastapi import FastAPI

from routers import root
from routers.naver import news
import uvicorn

app = FastAPI()
app.include_router(root.router)
app.include_router(news.router, prefix="/naver", tags=["naver"])


def start():
    uvicorn.run("main:app", host="127.0.0.1", port=3300)
