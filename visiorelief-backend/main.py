from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from openai import OpenAI
from dotenv import load_dotenv

from query_process_request_audio import QueryProcessRequestAudio
from query_process_request_text import QueryProcessRequestText
from query_chatgpt_singleton import QueryChatGPTSingleton

# Load environment variables from .env file
load_dotenv()

# Setup the ChatGPT connection
client = OpenAI()
QueryChatGPTSingleton().setup(client)

# Setup the API
app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

api.add_resource(QueryProcessRequestAudio, '/query')
api.add_resource(QueryProcessRequestText, '/query-text')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=1337)
