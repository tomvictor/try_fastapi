from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from sqlmodel import SQLModel, Session


ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def create(self, session: Session, hero: CreateSchemaType) -> ModelType:
        db_hero = self.model.from_orm(hero)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero
