from aiohttp import web
import json
import select_query

async def handle(request):
    response_obj = { 'status' : 'success' }
    return web.Response(text=json.dumps(response_obj))

app = web.Application()

app.router.add_get('/', handle)
app.router.add_get('/query/select/', select_query.select_query)
app.router.add_get('/query/tables/', select_query.show_tables_query)

web.run_app(app)