from fastapi import APIRouter, Depends
from pydantic import BaseModel

from wrappers.naver.news.naver_news import NaverNews

from .example_news import example_data_fetch_naver_news

router = APIRouter()


class NaverNewsInput(BaseModel):
    keyword: str


class NaverNewsAPIKeyNotSetError(BaseModel):
    detail: str = "NAVER_API_KEY and NAVER_API_SECRET must be set in environment"


@router.get(
    "/news",
    responses={
        200: {
            "description": "Success",
            "content": {"application/json": {"example": example_data_fetch_naver_news}},
        },
        401: {
            "model": NaverNewsAPIKeyNotSetError,
            "description": "If NAVER_API_KEY and NAVER_API_SECRET not set in environment",
        },
        500: {"description": "If requests raise exception",},
    },
)
async def news(request: NaverNewsInput = Depends()):
    naver_news = NaverNews()

    return naver_news.fetch(keyword=request.keyword)
