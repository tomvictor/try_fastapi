from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.api.deps import get_db
from app.models.hero import HeroRead, HeroCreate, Hero, HeroUpdate
from app import crud

router = APIRouter()


@router.get("/")
def read_root():
    return {"title": "hello", "description": "world"}


@router.post("/heroes/", response_model=HeroRead)
def create_hero(*, db: Session = Depends(get_db), hero: HeroCreate):
    resp = crud.hero.create(db, hero)
    return resp


@router.get("/heroes/{hero_id}", response_model=HeroRead)
def read_hero(*, db: Session = Depends(get_db), hero_id: int):
    db_hero = crud.hero.get(db, hero_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return db_hero


@router.patch("/heroes/{hero_id}", response_model=HeroRead)
def update_hero(*, db: Session = Depends(get_db), hero_id: int, hero: HeroUpdate):
    db_hero = crud.hero.get(db, hero_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    return crud.hero.update(db, db_hero, hero)


@router.delete("/heroes/{hero_id}")
def delete_hero(*, db: Session = Depends(get_db), hero_id: int):
    db_hero = crud.hero.get(db, hero_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    crud.hero.delete(db, db_hero)
    return {"ok": True}
