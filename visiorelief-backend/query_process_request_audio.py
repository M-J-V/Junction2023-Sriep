from io import BytesIO
from flask import request, send_file
from flask_restful import Resource
from gtts import gTTS
import json

from query_chatgpt_singleton import QueryChatGPTSingleton

# Process the post request with ChatGPT and return the response as an audio file
class QueryProcessRequestAudio(Resource):
    def post(self):
        data = request.get_json()
        scene = data.get('scene')
        sounds = data.get('sounds')
        length = data.get('length')
        print(data)
        print(scene)
        print(sounds)
        print(length)

        # Process the request with ChatGPT
        processed_input = QueryChatGPTSingleton().query(scene, sounds, length)
        
        # Convert the response to an audio file
        speech = gTTS(processed_input, lang='en', tld='us')

        # Send the audio file back
        fp = BytesIO()
        speech.write_to_fp(fp)
        fp.seek(0)
        return send_file(fp, mimetype='audio/mpeg', as_attachment=True, download_name='output.mp3')