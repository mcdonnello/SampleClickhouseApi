class QueryBuilder(object):
    "Construct SQL queries from url params"
    def __init__(self):
        pass
    def build_select(self, columns, table_name, limit):
        return "SELECT {0} FROM {1} LIMIT {2}".format(columns, table_name, limit)




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