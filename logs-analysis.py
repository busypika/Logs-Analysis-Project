#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def sql_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def get_popular_articles():
    # Input query and get results
    results = sql_query('''
        SELECT articles.title, count(*) AS num
        FROM articles,
            (SELECT split_part(path, '/', 3) AS new_path FROM log) AS subq
        WHERE new_path = articles.slug
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3
        ''')
    # Print Results
    print("The most popular 3 articles are: ")
    print("")
    for i in range(0, 3):
        print('"%s" - %i views' % (results[i][0], results[i][1]))
    print("")


def get_popular_authors():
    # Input query and get results
    results = sql_query('''
        SELECT authors.name, num
        FROM authors,
            (SELECT articles.author, count(*) AS num
            FROM articles,
                (SELECT split_part(path, '/', 3) AS new_path FROM log) AS subq
            WHERE new_path = articles.slug
            GROUP BY articles.author
            ORDER BY num DESC) AS top_num
        WHERE authors.id =  top_num.author
        ''')
    # Print results
    print("The most popular article authors are: ")
    print("")
    for i in range(len(results)):
        print('"%s" - %i views' % (results[i][0], results[i][1]))
    print("")


def get_most_error():
    # Input query and get results
    results = sql_query('''
        SELECT total_d,
            (error.error_req*1.0/total.total_req)*100  AS percentage
        FROM
            (SELECT DATE(time) as total_d, count(*) AS total_req
            FROM log
            GROUP BY total_d) AS total
        JOIN
            (SELECT DATE(time) as error_d, count(*) AS error_req
            FROM log
            WHERE status LIKE '4%'
            GROUP BY error_d) AS error
        ON total_d = error_d
        WHERE (error.error_req*1.0/total.total_req)*100 > 1
        ''')
    # Print Results
    print("Days did more than 1%% of requests lead to errors are: ")
    print("")
    for i in range(len(results)):
        # %% for escape the % sign
        print("%s:  %3.2f %%  errors" % (str(results[i][0]), results[i][1]))
    print("")

if __name__ == '__main__':
    print("Analyzing...")
    print("")
    get_popular_articles()
    get_popular_authors()
    get_most_error()
