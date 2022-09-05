import mysql.connector

__cnx = None

'''__cnx is a global variable declaration, and it refers that
if a connection is already present there's no need of an additional 
connection to be built or else build the connection for the particular instance'''


def get_sql_connection():
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='root',
                                        host='127.0.0.1',
                                        database='grocery_store'
                                        )

    return __cnx
