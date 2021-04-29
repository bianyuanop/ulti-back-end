from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class BattleHistory(Resource):

    def get(self):
        return {"status": "OK"}, 200

api.add_resource(BattleHistory, '/')


if __name__ == '__main__':
    app.run(debug=True)