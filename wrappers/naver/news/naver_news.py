import os

import requests
from fastapi import HTTPException


class NaverNewsAPIKeyNotSetException(Exception):
    pass


class NaverNews:
    endpoint = "https://openapi.naver.com/v1/search/news.json"

    def __init__(self):
        self._api_key = os.environ.get("NAVER_API_KEY")
        self._api_secret = os.environ.get("NAVER_API_SECRET")

    def _validation_api_key(self):
        if self._api_key is None and self._api_secret is None:
            raise NaverNewsAPIKeyNotSetException(
                "NAVER_API_KEY and NAVER_API_SECRET must be set in environment"
            )

    def fetch(self, keyword: str):
        try:
            self._validation_api_key()
        except NaverNewsAPIKeyNotSetException as e:
            raise HTTPException(status_code=500, detail=str(e))

        res = requests.get(
            NaverNews.endpoint,
            params={"query": keyword,},
            headers={
                "X-Naver-Client-Id": self._api_key,
                "X-Naver-Client-Secret": self._api_secret,
            },
        )
        try:
            res.raise_for_status()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        return res.json()
