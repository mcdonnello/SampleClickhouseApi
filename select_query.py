from aiohttp import web
from aiohttp import ClientSession
import json
from query_builder import QueryBuilder
async def select_query(request):
    try:
        columns = request.query['columns']
        table_name = request.query['table']
        where = request.query['where']
        limit = request.query['limit']
        grouping = request.query['group']
        ordering = request.query['order']
        direction = request.query['direction']

        query_string = QueryBuilder.build_select(columns, table_name, where, limit, grouping, ordering, direction)

        clickhouse_http_query = "http://mcdonnelloprojects.xyz:8123//?query={0}".format(query_string)
        async with ClientSession() as session:
            async with session.get(clickhouse_http_query) as resp:
                response_data = await resp.text()
        await session.close()

        # return a success json response with status code 200 i.e. 'OK'
        return web.Response(text=response_data, status=200)
    except Exception as e:
        response_obj = { 'status' : 'failed', 'reason': str(e) }
        # return failed with a status code of 500 i.e. 'Server Error'
        return web.Response(text=json.dumps(response_obj), status=500)

async def show_tables_query(request):
    try:
        db = request.query['db']
        where_and = request.query['where_and']
        limit = request.query['limit']
        query_string = QueryBuilder.build_show_tables(db, where_and, limit)

        clickhouse_http_query = "http://mcdonnelloprojects.xyz:8123//?query={0}".format(query_string)
        async with ClientSession() as session:
            async with session.get(clickhouse_http_query) as resp:
                response_data = await resp.text()
        await session.close()

        # return a success json response with status code 200 i.e. 'OK'
        return web.Response(text=response_data, status=200)
    except Exception as e:
        response_obj = { 'status' : 'failed', 'reason': str(e) }
        # return failed with a status code of 500 i.e. 'Server Error'
        return web.Response(text=json.dumps(response_obj), status=500)