from flask import Flask
from flask_restful import Resource, Api
from random import choice
import uuid

app = Flask(__name__)
api = Api(app)

def data():
    values = {"ID": str(uuid.uuid4()),
        "placa_id": str(uuid.uuid4()),
        "value_x":choice(range(1000)),
        "value_y":choice(range(1000)),
        "value_z":choice(range(1000)),
        "value_w":choice(range(1000)),
        "value_a":choice(range(1000)),
        "value_b":choice(range(1000)),
        "value_c":choice(range(1000)),
        "value_d":choice(range(1000)),
        "value_h":choice(range(1000))
        }
    return values  


class Report(Resource):
    def get(self):
        values = [data()  for p in range(100)]    
        
        return {'result': values}

api.add_resource(Report, '/report')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)
