from app.crud.base import CRUDBase
from app.models.hero import Hero


class CRUDHero(CRUDBase):
    pass


hero = CRUDHero(Hero)
