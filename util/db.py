import pymysql

default_username = 'lobbyServer'
default_password = 'lobbyServer'

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


# use table_schema for security check
# key -> table_name 
# values -> columns
class Database:
    
    def __init__(self, db):
        self.table_schema = {}
        self.db = db
        connection = pymysql.connect(host='localhost',
            user=default_username,
            password=default_password,
            database=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        
        cursor = connection.cursor()
        cursor.execute('show tables;') 
        tables = cursor.fetchall()
        for table in tables:
            self._getColumnName(cursor, table['Tables_in_lobbyServer'])
        
        connection.close()
    
    def _getColumnName(self, cursor, table_name):
        sql = '''
        SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = '{database}' AND TABLE_NAME = '{table}';
        '''
        cursor.execute(sql.format(database=self.db, table=table_name))
        fields = cursor.fetchall()
        fields = [item['COLUMN_NAME'] for item in fields] 
        self.table_schema[table_name] = fields
        
if __name__ == '__main__':
    db = Database('lobbyServer')
