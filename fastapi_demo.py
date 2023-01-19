
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

import sqlite_demo
from sqlite_demo import *

# start_cmd: uvicorn fastapi_demo:app --reload

app = FastAPI()

from pydantic import BaseModel


class Item(BaseModel):
    email: str
    name: str
    time: int


@app.get("/", response_class=HTMLResponse)
async def root():
    form_html = open("form.html", 'r').read()
    return form_html



@app.post("/sub/")
async def sub_function(item: Item):
    # 检查是否存在重复email，是的话校验token，并更新信息
    # 否则，存数据库
    sqlite_demo.insert(item.email, item.name, item.time)
    return {"info": "接收到如下信息","email": item.email, "name": item.name, "time": item.time}


@app.get("/unsub/")
async def unsub_function(email: str, token: str):
    # 检查email与token是否一致
    # 更新有效标识
    return {"info": "接收到如下信息","email": email, "token": token}


@app.get("/sum/all")
async def sum_all():
    # 查询表中注册有的email数量
    num = sqlite_demo.count_all()
    return {"num": num}

@app.get("/sum/now")
async def sum_now():
    # 查询表中注册有的服务中的email数量
    num = sqlite_demo.count_now()
    return {"num": num}



@app.on_event("shutdown")
async def shutdown_event():
    print("关闭应用程序啦")
    sqlite_demo.clear()
