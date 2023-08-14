from fastapi import APIRouter, FastAPI, Request

router = APIRouter()


@router.get("/")
async def index(request: Request):
    return {"message": "Hello World!"}


app = FastAPI()
app.include_router(router)
