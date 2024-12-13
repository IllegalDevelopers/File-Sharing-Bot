from aiohttp import web
from .route import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app





# Illegal Developer Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Illegal_Developer
# Developer @Ishana_Dev_Bot
