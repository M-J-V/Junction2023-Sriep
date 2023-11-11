from io import BytesIO
from flask import request, send_file
from flask_restful import Resource
from gtts import gTTS
import json

from query_chatgpt_singleton import QueryChatGPTSingleton

class QueryProcessRequest(Resource):
    def post(self):

        #{"scene":"Clouds","sounds:["Zen Garden", "Fire Crackling", "Ocean Waves"]","length:100"}
        # curl -X POST -H "Content-Type: application/json" -d '{\"scene\": \"Clouds\", \"sounds\": [\"Zen Garden\", \"Fire Crackling\", \"Ocean Waves\"], \"length\": 100}' http://127.0.0.1:5000/query
        data = request.get_json()
        scene = data.get('scene')
        sounds = data.get('sounds')
        length = data.get('length')
        print(data)
        print(scene)
        print(sounds)
        print(length)

        processed_input = QueryChatGPTSingleton().query(scene, sounds, length)
        speech = gTTS(processed_input, lang='en', tld='us')

        fp = BytesIO()
        speech.write_to_fp(fp)
        fp.seek(0)

        return send_file(fp, mimetype='audio/mpeg', as_attachment=True, download_name='output.mp3')

    # def get(self):
    #     # scene = request.form['scene']
    #     # sounds = json.loads(request.form['scene'])
    #     # sounds = ["sound1", "sound2"]
    #     # processed_input = QueryChatGPTSingleton().query(scene, sounds)

    #     example_scene = "Clouds"
    #     example_sounds = ["Zen Garden", "Fire Crackling", "Ocean Waves"]
    #     example_length = 50
    #     processed_input = QueryChatGPTSingleton().query(example_scene, example_sounds, example_length)

    #     return processed_input