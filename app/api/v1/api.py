from fastapi import APIRouter

from .endpoints import heroes

api_router = APIRouter()
api_router.include_router(heroes.router, tags=["hero"])
