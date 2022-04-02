from fastapi import FastAPI
import uvicorn

from app.api.v1.api import api_router

from app.core.config import settings

app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4200)
