from fastapi import APIRouter, Depends
from sqlmodel import Session

from api.deps import get_db
from models.hero import HeroRead, HeroCreate, Hero

router = APIRouter()


@router.get("/")
def read_root():
    return {"title": "hello", "description": "world"}


@router.post("/heroes/", response_model=HeroRead)
def create_hero(*, session: Session = Depends(get_db), hero: HeroCreate):
    db_hero = Hero.from_orm(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero
