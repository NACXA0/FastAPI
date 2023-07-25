import logging
import socketio
from aiohttp import web
from urllib import parse
from bidict import bidict
from __init__ import app

@app.get('/a')
def a():
    return {'a': 'a'}


@app.get('/chat_room', summary='聊天室界面')
async def chat_room(request):
    with open('.templates/chat_room.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


async def login(request):
    data = await request.json()
    user_name = data['user_name']
    if user_sid.get(user_name, None):
        return web.json_response({'code': 'fail'}, status=-1)
    else:
        return web.json_response({'code': 'success'}, status=200)


async def connect(sid, environ):
    query_params = environ['QUERY_STRING'].split('&')
    params = dict()
    for query_param in query_params:
        a, b = query_param.split('=')
        params[a] = parse.unquote(b)
    user_name = params['name']
    user_sid[user_name] = sid
    await sio.emit('reply', f'{user_name}连线成功！', namespace='/chat')


async def message(sid, data):
    # print("server received message!", data)
    await sio.emit('reply', f"{user_sid.inv[sid]}: {data}", namespace='/chat')


async def disconnect(sid):
    user_name = user_sid.inv[sid]
    del user_sid[user_name]
    await sio.emit('reply', f'{user_name}退出连线！', namespace='/chat')


if __name__ == '__main__':
    app = web.Application()
    # logging.basicConfig(level=logging.DEBUG)
    app.router.add_get('/chat_room', chat_room)
    app.router.add_routes([web.post('/login', login)])
    app.router.add_static('/static', 'static')

    sio = socketio.AsyncServer()
    sio.on('disconnect', disconnect, namespace='/chat')
    sio.on('chat message', message, namespace='/chat')
    sio.on('connect', connect, namespace='/chat')
    sio.attach(app)

    user_sid = bidict()
    web.run_app(app, host='localhost')

    # 聊天室页面：http://localhost:8080/chat_room
    # 如果修改ip地址需要修改chat_room.html中的第20行以及第61的localhost