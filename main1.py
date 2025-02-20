from fastapi import FastAPI

app = FastAPI()


@app.get('/greet/{username}')
async def greet(username:str):
    return {"message" : f"Hello {username}"}


@app.get('/')
async def read_root():
    return {"message" : "hello world"}

#uvicorn main:app --reload
#clrl + Z
#pkill -9 Python
class chirag:
    def hello(username:str)->str:
        print("hello",{username}) 