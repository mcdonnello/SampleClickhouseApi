class QueryBuilder(object):
    "Construct SQL queries from url params"
    def __init__(self):
        pass
    @staticmethod
    def build_select(columns, table_name, where, limit, group, order, direction):
        base_query = "SELECT {0} FROM {1} ".format(columns, table_name)
        
        organise_query_group = organise_query_order = limit_string = where_clause = ""
        if(where != ""): where_clause = "WHERE {0} ".format(where)
        if(limit != ""): limit_string = "LIMIT {0} ".format(limit)
        if (group != ""): organise_query_group = "GROUP BY {0} ".format(group)
        if (order != ""): organise_query_order = "ORDER BY {1} {2} ".format(order, direction)
        return base_query + where_clause + limit_string + organise_query_group + organise_query_order + "FORMAT JSON"

    @staticmethod
    def build_show_tables(db, where_and, limit):
        "SHOW TABLES FROM <db> [WHERE ...] [AND name LIKE <pattern>] [LIMIT <N>] [INTO OUTFILE <filename>] [FORMAT <format>]"
        if(db == ""): db = "tutorial"
        if(where_and != ""): where_and = "WHERE {0}".format(where_and)
        if(limit != ""): limit = "LIMIT {0}".format(limit)
        return "SHOW TABLES FROM  {0} {1} {2}".format(db, where_and, limit)

    ''' 
    Sample queries to use.

    SELECT
        *
            FROM tutorial.visits_v1
            LIMIT 10

    SELECT
        StartURL,
        AVG(Duration)
            FROM tutorial.visits_v1
            LIMIT 10

    SELECT
        StartURL,
        AVG(Duration)
            FROM tutorial.visits_v1
            WHERE StartDate BETWEEN '2014-03-23' AND '2014-03-30'
            LIMIT 10

    SELECT
        StartURL,
        AVG(Duration)
            FROM tutorial.visits_v1
            WHERE StartDate BETWEEN '2014-03-23' AND '2014-03-30'
            GROUP BY StartURL
            ORDER BY AVG(Duration) DESC
            LIMIT 10

    SELECT
    StartURL AS URL,
    AVG(Duration) AS AvgDuration
        FROM tutorial.visits_v1
        WHERE StartDate BETWEEN '2014-03-23' AND '2014-03-30'
        GROUP BY URL
        ORDER BY AvgDuration DESC
        LIMIT 10
'''