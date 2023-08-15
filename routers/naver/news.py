from fastapi import APIRouter, Request

from wrappers.naver.news.naver_news import NaverNews

router = APIRouter()


@router.get("/news")
async def news(request: Request):
    naver_news = NaverNews()

    try:
        keyword = request.query_params["keyword"]
    except KeyError:
        return {"error": "keyword is required."}

    return naver_news.fetch(keyword)
