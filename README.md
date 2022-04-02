# try_fastapi
 start coding FastAPI

Alembic cmds
------------

caveats:
manually import 'sqlmodel' to versions
```commandline

alembic current
alembic revision --autogenerate -m "create hero model"
alembic upgrade heads
```
