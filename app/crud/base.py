from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from sqlmodel import SQLModel, Session


ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def create(self, db: Session, hero: CreateSchemaType) -> ModelType:
        db_hero = self.model.from_orm(hero)
        db.add(db_hero)
        db.commit()
        db.refresh(db_hero)
        return db_hero

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def update(
        self,
        db: Session,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ):
        hero_data = obj_in.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(db_obj, key, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: ModelType):
        db.delete(db_obj)
        db.commit()
        return {"ok": True}
