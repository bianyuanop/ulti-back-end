from flask import Flask
from flask_restful import Api
from util.control import DatabaseController

app = Flask(__name__)
api = Api(app)

api.add_resource(DatabaseController, '/admin/db-control')

if __name__ == '__main__':
    app.run(debug=True)