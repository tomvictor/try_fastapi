from crud.base import CRUDBase
from models.hero import Hero


class CRUDHero(CRUDBase):
    pass


hero = CRUDHero(Hero)
