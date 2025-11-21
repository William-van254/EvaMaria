from aiohttp import web
import os

routes = web.RouteTableDef()
@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({"ok": True})

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

# The port Koyeb expects the server to run on
port = int(os.environ.get("PORT", 8000))
web.run_app(web_server(), port=port)
