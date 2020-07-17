import logging
import aiohttp
import aiohttp_jinja2
from aiohttp import web
from faker import Faker
import aioredis
from pprint import pprint

log = logging.getLogger(__name__)


def get_random_name():
    fake = Faker()
    return fake.name()


async def index(request):

    ws_current = web.WebSocketResponse()  # Starts websocket after coroutune call the websocket methods can be used
    ws_ready = ws_current.can_prepare(request)  # receive client request. Process the request format into websocket 
    
    if not ws_ready.ok:
        return aiohttp_jinja2.render_template('index.html', request, {})
    
    await ws_current.prepare(request)
    name = get_random_name()  # for every connected user and for each session intitialize random name

    log.info('%s joined.', name)
    # ** insert user at redis

    await request.app['redis'].sadd('visitors', name)
    values = await request.app['redis'].smembers('visitors', encoding='utf-8')
    print("redis user members: ", values)

    await ws_current.send_json({'action': 'connect', 'name': name})
    
    for ws in request.app['websockets'].values():
        await ws.send_json({'action': 'join', 'name': name})
        
    request.app['websockets'][name] = ws_current
    
    print(request.app['websockets'].items())
   
    while True:
        msg = await ws_current.receive()

        if msg.type == aiohttp.WSMsgType.text:
            for ws in request.app['websockets'].values():
                if ws is not ws_current:
                    await ws.send_json(
                        {'action': 'sent', 'name': name, 'text': msg.data})
                    
                    await request.app['redis'].sadd('messages', name + ":" + str(msg.data)) # insert message at reedis

                        
        else:
            break

    del request.app['websockets'][name]
    log.info('%s disconnected.', name)
    for ws in request.app['websockets'].values():
        await ws.send_json({'action': 'disconnect', 'name': name})

    return ws_current




