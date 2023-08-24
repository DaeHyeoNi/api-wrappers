from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/",
    responses={
        200: {
            "description": "Success",
            "content": {"application/json": {"example": {"message": "Hello World!"}}},
        }
    },
)
async def index():
    return {"message": "Hello World!"}
