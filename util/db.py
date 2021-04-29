import pymysql


def connect(user, password, targetDB, host='localhost'):
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=targetDB,
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection

def close(connection):
    try:
        connection.close()
    except Exception as e:
        print("Connection close err ", e)