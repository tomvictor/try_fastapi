from fastapi import FastAPI
import asyncio
app = FastAPI()



async def func1():
    print("func1 start")
    await asyncio.sleep(7)
    print("func1 end")

async def func2():
    print("func2 start")
    await asyncio.sleep(7)
    print("func2 end")




@app.get("/")
async def root():
    """Home API

    Returns:

    """
    await asyncio.gather(func1(), func2())
    resp = {"id": 1, "name": "test"}
    return resp
