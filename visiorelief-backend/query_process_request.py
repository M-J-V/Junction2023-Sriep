from flask import request
from flask_restful import Resource

from query_chatgpt_singleton import QueryChatGPTSingleton

class QueryProcessRequest(Resource):
    def get(self):
        input = request.form['data']

        processed_input = QueryChatGPTSingleton().query(input)

        return processed_input
