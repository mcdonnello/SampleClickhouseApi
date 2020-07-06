class QueryBuilder(object):
    "Construct SQL queries from url params"
    def __init__(self):
        pass
    def build_select(self, columns, table_name, limit, group, order, direction):
        query = "SELECT {0} FROM {1} ".format(columns, table_name)
        
        organise_query_group = organise_query_order = limit_string = ""
        if(limit != ""): limit_string = "LIMIT {0} ".format(limit)
        if (group != ""): organise_query_group = "GROUP BY {0} ".format(group)
        if (order != ""): organise_query_order = "ORDER BY {1} {2} ".format(order, direction)
        return query + limit_string + organise_query_group + organise_query_order + "FORMAT JSON"




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