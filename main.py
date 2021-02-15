from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    """Home API

    Returns:

    """
    resp = {"id": 1, "name": "test"}
    return resp
