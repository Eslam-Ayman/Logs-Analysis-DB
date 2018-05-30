# !/usr/bin/env python3
# docstrings (the triple quotation mark method)
"""
The first line in this file should be your shebang, which specifies
which Python interpreter should be used to run your code .
The shebang tells the OS which interpreter to use when your script
is run directly. For example, if you run `` .
"""

# importing DB-API module
import psycopg2

# this function for printing result as a table style


def header_style(question, headr1, header2):
    print("\n\n"+question+"\n\n"
          "------------------------------------+--------------------\n"
          "\t       "+headr1+"\t    |    "+header2+" \n"
          "------------------------------------+--------------------")

# this is connection function to connect with postgres DB


def conn():
    conn_db_obj = psycopg2.connect(database="news")
    cursor = conn_db_obj.cursor()
    return conn_db_obj, cursor

# the first question function implementation


def question_1():
    # connect with DB
    conn_db_obj, cursor = conn()
    # execute query
    cursor.execute("""
                   select count(*) as GetAccessTimes ,
                   articles.title as ArtName
                   from articles inner join log on log.path
                   = '/article/' || articles.slug
                   where log.status = '200 OK'
                   group by ArtName
                   order by GetAccessTimes desc limit 3
                   """)
    # fetching all results from database
    results = cursor.fetchall()
    # close connection of database
    conn_db_obj.close()
    # printing the results in table
    header_style('1. What are the most popular three articles of all time?',
                 'Articles Name', 'Access Times')
    for GetAccessTimes, ArtName in results:
        print("%s    |       %d" % (ArtName, GetAccessTimes))

# the second question function implementation


def question_2():
    # connect with DB
    conn_db_obj, cursor = conn()
    # execute query
    cursor.execute("""
                   select authors.name as authName ,
                   count(*) as GetAccessTimes
                   from authors inner join articles
                   on articles.author = authors.id
                   inner join log on log.path
                   like concat('%',articles.slug,'%')
                   where log.status = '200 OK'
                   group by authName
                   order by GetAccessTimes desc
                   """)
    # fetching all results from database
    results = cursor.fetchall()
    # close connection of database
    conn_db_obj.close()
    # printing the results in table
    header_style('2. Who are the most popular article authors of all time?',
                 'Author Name', 'Access Times')
    for authName, GetAccessTimes in results:
        print("%s \t\t    |       %d" % (authName, GetAccessTimes))

# the third question function implementation


def question_3():
    # connect with DB
    conn_db_obj, cursor = conn()
    # execute query
    cursor.execute("""
                   select * from (
                   select date(log.time) as day ,
                   100.0 *
                   sum(case log.status when '200 OK' then 0 else 1 end)
                   /count(date(log.time)) as percentage from log
                   group by day ) as virtualTable
                   where percentage > 1
                   """)
    # fetching all results from database
    results = cursor.fetchall()
    # close connection of database
    conn_db_obj.close()
    # printing the results in table
    header_style("3. On which days did "
                 "more than 1% of requests lead to errors?",
                 'Date of Day', 'Percentage')
    for day, percentage in results:
        print("%s\t\t\t    |       %.1f %%" % (day, percentage))


# calling of all of the tree function to get the result

""" To make sure the main subroutine is
only run when this program is executed directly,
and not when it is imported as a module"""
if __name__ == '__main__':
    question_1()
    question_2()
    question_3()
