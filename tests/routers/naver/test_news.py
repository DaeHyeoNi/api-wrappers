import pytest
from unittest.mock import patch, Mock
from fastapi import HTTPException
import requests

from wrappers.naver.news.naver_news import NaverNews


@pytest.fixture
def mock_env_variables():
    with patch("wrappers.naver.news.naver_news.os") as mock_os:
        mock_os.environ.get.return_value = "your_api_key"
        yield


@pytest.fixture
def mock_requests_get():
    with patch("wrappers.naver.news.naver_news.requests.get") as mock_get:
        yield mock_get


def test_fetch_news_success(mock_env_variables, mock_requests_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": "news_data"}
    mock_requests_get.return_value = mock_response

    naver_news = NaverNews()
    result = naver_news.fetch("keyword")
    assert result == {"data": "news_data"}


def test_fetch_news_failure(mock_env_variables, mock_requests_get):
    mock_response = Mock()
    mock_response.status_code = 400
    mock_requests_get.return_value = mock_response
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "Bad Request"
    )

    naver_news = NaverNews()
    with pytest.raises(HTTPException) as context:
        naver_news.fetch("keyword")
    assert context.value.status_code == 500


def test_fetch_news_no_api_key():
    with patch("wrappers.naver.news.naver_news.os") as mock_os:
        mock_os.environ.get.return_value = None

        naver_news = NaverNews()
        with pytest.raises(HTTPException) as context:
            naver_news.fetch("keyword")
        assert context.value.status_code == 500
        assert (
            str(context.value.detail)
            == "NAVER_API_KEY and NAVER_API_SECRET must be set in environment"
        )
