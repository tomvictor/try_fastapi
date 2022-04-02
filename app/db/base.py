# Import all the models, so that Base has them before being
# imported by Alembic
# from app.db.base_class import Base  # noqa
from sqlmodel import SQLModel
from app.models.hero import Hero  # noqa
