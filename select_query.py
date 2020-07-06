from aiohttp import web
import json
from query_builder import QueryBuilder
async def select_query(request):
    try:
        columns = request.query['columns']
        table_name = request.query['table']
        limit = request.query['limit']
        query_builder = QueryBuilder()
        query_string = query_builder.build_select(columns, table_name, limit)
        response_obj = { 'status' : 'query successful', 'query' : query_string }
        # return a success json response with status code 200 i.e. 'OK'
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = { 'status' : 'failed', 'reason': str(e) }
        # return failed with a status code of 500 i.e. 'Server Error'
        return web.Response(text=json.dumps(response_obj), status=500)