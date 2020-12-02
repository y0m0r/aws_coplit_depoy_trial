from flask import Flask, request
from flask_restful import Resource, Api
import os
app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
   def get(self):
      return { "message" : "Hello Flask API World!" , "version": 3}


class Greeting2 (Resource):
   def get(self):
      print(dict(os.environ.items()))
      return dict(os.environ.items())
      # return { "message" : "Hello Flask API World!!" , "version": 3}


api.add_resource(Greeting, '/') # Route_1
api.add_resource(Greeting2, '/api') # Route_1


if __name__ == '__main__':
   app.run('0.0.0.0','3000')
