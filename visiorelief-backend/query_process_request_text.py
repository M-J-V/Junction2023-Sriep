from io import BytesIO
from flask import request, send_file
from flask_restful import Resource
from gtts import gTTS
import json

from query_chatgpt_singleton import QueryChatGPTSingleton

class QueryProcessRequestText(Resource):
    def post(self):
        data = request.get_json()
        scene = data.get('scene')
        sounds = data.get('sounds')
        length = data.get('length')
        print(data)
        print(scene)
        print(sounds)
        print(length)

        processed_input = QueryChatGPTSingleton().query(scene, sounds, length)

        return processed_input