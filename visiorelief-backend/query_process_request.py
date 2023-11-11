from flask import request
from flask_restful import Resource
import json

from query_chatgpt_singleton import QueryChatGPTSingleton

class QueryProcessRequest(Resource):
    def get(self):
        scene = request.form['scene']
        sounds = json.loads(request.form['scene'])
        # sounds = ["sound1", "sound2"]
        processed_input = QueryChatGPTSingleton().query(scene, sounds)

        return processed_input
