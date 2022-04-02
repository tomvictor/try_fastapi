from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    return {"title": "hello", "description": "world"}
