import logging
import jinja2
import aiohttp_jinja2

from aiohttp import web
from views import index


import aioredis


async def close_redis(app):
    

    
    await app['redis'].wait_closed()
    print("redis closed")


async def init_app():
    app = web.Application()  # Appplication dictionary
    app["websockets"] = {}  # storing websockets at Application
    app["redis"] = await aioredis.create_redis_pool('redis://localhost')

    app.on_shutdown.append(shutdown)  # Listen the Shutdown event and shutdown the server
    app.on_shutdown.append(flush_redis) # delete all in memory data    
    app.on_shutdown.append(close_redis) # close redis

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates/'))  # at templates there are html pages

    app.router.add_get('/', index)  # main page of the chat
    
    return app


async def shutdown(app):
    for ws in app['websockets'].values():  # cßlose all sockets iteratively
        await ws.close(code=1000, message='Server shutdown')
    
    app['websockets'].clear()
    
def main():
    logging.basicConfig(level=logging.DEBUG)
    app = init_app()  # initiaize app settings
    web.run_app(app)  # run web app

    

if __name__ == '__main__':
    main()