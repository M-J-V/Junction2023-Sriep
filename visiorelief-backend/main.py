from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from openai import OpenAI
from dotenv import load_dotenv

from query_process_request import QueryProcessRequest
from query_chatgpt_singleton import QueryChatGPTSingleton

# Load environment variables from .env file
load_dotenv()

client = OpenAI()
QueryChatGPTSingleton().setup(client)

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

api.add_resource(QueryProcessRequest, '/query')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=1337)
