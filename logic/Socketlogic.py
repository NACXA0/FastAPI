import os
import socketio
from urllib import parse
from bidict import bidict
from pydantic import BaseModel, Field                       #
from fastapi.responses import JSONResponse, HTMLResponse    #
from fastapi import APIRouter                               #
from fastapi.staticfiles import StaticFiles                 #

user_sid = bidict()
pwd_path = os.path.dirname(os.path.abspath(__file__))

class Login(BaseModel):
    user_name:str = Field(..., description='1')

router = APIRouter()

@router.get('/chat_room', summary='聊天室界面')
async def chat_room():
    with open(chat_room) as f:
        return HTMLResponse(f.read())

@router.post('/login', summary='登录')
async def login(item: Login):
    user_name = item.user_name
    JSONResponse.media_type = 'application/json; charset=utf-8'
    if user_sid.get(user_name, None):
        return JSONResponse({'code':'fail'}, status_code=400)
    else:
        return JSONResponse({'code':'success'}, status_code=200)

def init_socketio(app):
    #事件函数
    async def connect(sid, environ):
        query_params = environ['QUERTY_STRING'].split('&')
        params = dict()
        for query_params in query_params:
            a, b = query_params.split('=')
            params[a] = parse.unquote(b)
        user_name = params['name']
        user_sid[user_name] = sid

        await sio.emit('reply', f'{user_name}连线成功！', namespace='/chat')
    async def message(sid, data):
        await sio.emit('reply', f"{user_sid.inv[sid]}: {data}", namespace='/chat')

    async def disconnect(sid):
        user_name = user_sid.inv[sid]
        del user_sid[user_name]
        await sio.emit('reply', f'{user_name}退出连线！', namespace='/chat')

    # 静态文件
    app.mount("/static", StaticFiles(directory=f"{pwd_path}/static"), name="static")

    # 初始化socketio
    sio = socketio.AsyncServer(async_mode='asgi')
    # 绑定事件函数
    sio.on('disconnect', disconnect, namespace='/chat')
    sio.on('chat message', message, namespace='/chat')
    sio.on('connect', connect, namespace='/chat')
    # app绑定socketio
    app.mount('/', socketio.ASGIApp(socketio_server=sio))  # 使用默认的socket

