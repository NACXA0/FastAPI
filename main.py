from typing import Union

from fastapi import FastAPI, Request
from pydantic import BaseModel
#from logic.GLMAPI import *
from logic.Socketlogic import router, init_socketio, socketio
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./templates")#这个是使用模板必须的，否则就只能写html'''<html代码>'''

'''
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class text_class(BaseModel):#接收信息然后返回
    word: "word这里是class里的文字"
'''
# 初始化socketio
sio = socketio.AsyncServer(async_mode='asgi')
# app绑定socketio
app.mount('/', socketio.ASGIApp(socketio_server=sio))  # 使用默认的socket path
def startup_event():
    """Socketio项目初始化"""
    app.include_router(router)
    init_socketio(app)


@app.get("/")
def read_root():
    return {"message": "Hellow World1324"}
'''
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
'''


@app.get("/Response")#接收信息然后返回
def text_def(request: Request):
    return templates.TemplateResponse("chat_simple.html",{"request": request})


@app.get("/Q")#量子计算模拟
def Q():
    return {"文字": "量子计算模拟"}



