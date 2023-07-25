from typing import Union
import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
#from logic.GLMAPI import *
from logic.Socketlogic import *
from __init__ import templates
#from logic.Socket2 import *


app = FastAPI()#main里必须要有app，不能从别处继承
#templates = Jinja2Templates(directory="./templates")#这个是使用模板必须的，否则就只能写html'''<html代码>'''


#class Item(BaseModel):
#    name: str
#    price: float
#    is_offer: Union[bool, None] = None

#class text_class(BaseModel):#接收信息然后返回
#    word: "word这里是class里的文字"



def startup_event():
    """Socketio项目初始化"""
    app.include_router(router)
    init_socketio(app)


@app.get("/")
def read_root():
    return {"message": "Hellow World1324"}

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}

#@app.put("/items/{item_id}")
#def update_item(item_id: int, item: Item):
#    return {"item_name": item.name, "item_id": item_id}



@app.get("/Response", summary='对话界面')#接收信息然后返回
async def connect(sid, environ):
    query_params = environ['QUERY_STRING'].split('&')
    params = dict()
    for query_param in query_params:
        a, b = query_param.split('=')
        params[a] = parse.unquote(b)
    user_name = params['name']
    user_sid[user_name] = sid
    await sio.emit('reply', f'{user_name}连线成功！', namespace='/chat')

#def text_def(request: Request):
#    return templates.TemplateResponse("chat_simple.html",{"request": request})

async def message(sid, data):
    print("server received message!", data)
    await sio.emit('reply', f"{user_sid.inv[sid]}: {data}", namespace='/chat')

async def disconnect(sid):
    user_name = user_sid.inv[sid]
    del user_sid[user_name]
    await sio.emit('reply', f'{user_name}退出连线！', namespace='/chat')








@app.get("/Q")#量子计算模拟
def Q():
    return {"文字": "量子计算模拟"}


