from flask_restful import reqparse
from util.db import Database

default_username = 'lobbyServer'
default_password = 'lobbyServer'

global_parser = reqparse.RequestParser()
lobbyServer = Database('lobbyServer')

columns = []
for item in lobbyServer.table_schema.values():
    for v in item:
        if v not in columns:
            columns.append(v)

global_parser.add_argument('table', type=str)
for column in columns:
    global_parser.add_argument(column, type=str)
        