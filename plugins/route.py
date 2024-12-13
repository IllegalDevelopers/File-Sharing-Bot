from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Madflix_Bots")




# Illegal Developer Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Illegal_Developer
# Developer @Ishana_Dev_Bot
