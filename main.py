from fastapi import FastAPI

from routers import root
from routers.naver import news

app = FastAPI()
app.include_router(root.router)
app.include_router(news.router, prefix="/naver", tags=["naver"])
