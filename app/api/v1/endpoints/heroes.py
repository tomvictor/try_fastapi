from fastapi import APIRouter, Depends
from sqlmodel import Session

from api.deps import get_db
from models.hero import HeroRead, HeroCreate, Hero
import crud

router = APIRouter()


@router.get("/")
def read_root():
    return {"title": "hello", "description": "world"}


@router.post("/heroes/", response_model=HeroRead)
def create_hero(*, session: Session = Depends(get_db), hero: HeroCreate):
    resp = crud.hero.create(session, hero)
    return resp
