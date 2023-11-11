from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

from openai import OpenAI
from dotenv import load_dotenv

from chatgpt_flask_test import QueryProcessRequest
from QueryChatGPTSingleton import QueryChatGPTSingleton

# Load environment variables from .env file
load_dotenv()

client = OpenAI()
QueryChatGPTSingleton().setup(client)

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

api.add_resource(QueryProcessRequest, '/query')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
