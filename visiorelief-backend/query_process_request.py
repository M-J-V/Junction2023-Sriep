from flask import request
from flask_restful import Resource

from query_chatgpt_singleton import QueryChatGPTSingleton

processed_requests = []

class QueryProcessRequest(Resource):
    def get(self):
        return {"all_requests": processed_requests}

    def put(self):
        input = request.form['data']

        processed_input = QueryChatGPTSingleton().query(input)

        return processed_input
