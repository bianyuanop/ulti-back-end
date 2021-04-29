import pymysql
from flask_restful import Resource, reqparse
from util import global_parser, default_username, default_password, db
from . import lobbyServer
        
class DatabaseController(Resource):

    def get(self):
        return lobbyServer.table_schema, 200
    
    def delete(self):
        args = global_parser.parse_args()

        table = args.get('table')
        if table not in lobbyServer.table_schema.keys():
            return {}, 400

        conn = db.connect(default_username, default_password, 'lobbyServer')
        cursor = conn.cursor()
        cols = lobbyServer.table_schema[table] 
        sql = 'delete from {table} where'
        print(cols)
        for col in cols:
            sql += " %s={%s}" % (col, col)
            if col != cols[-1]:
                sql += " and"
        
        print(sql)

        

        
        
         

if __name__ == '__main__':
    db = Database()