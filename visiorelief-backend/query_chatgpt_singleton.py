class QueryChatGPTSingleton():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(QueryChatGPTSingleton, cls).__new__(cls)
        return cls.instance
    
    # Setup the system prompt that is prepended before every request
    def setup(self, client):
        self.client = client
        self.system = """
        Helping a user practice their imagination skills, generate a serene scene that they can visualize to ease migraine symptoms. 
        Specify the scene in present tense and narrate it in a storytelling voice. 
        Keep the description grounded in reality without fantastical elements. 
        Avoid directly mentioning the user's feelings. 
        Provide a theme, including sounds in the scene, and ensure the overall atmosphere is calm. 
        Be vivid in describing the visuals, keeping the language simple as if written for a younger audience. 
        Make sure the scene is enjoyable for adults as well. 
        Steer clear of using the words 'scene,' 'sound,' and 'soundtrack' directly in the prompt.
        Also steer clear of describing the user.
        """

        # self.system = """
        #     You are helping a user practice their imagination skills. 
        #     For this you generate a short scene that they can imagine to alleviate migraine symptoms.

        #     Describe the scene in present tense and in story telling voice.
        #     Keep the scene realistic, do not include fantasy elements.
        #     Do not describe how the user is feeling.

        #     The user will give a theme including sounds playing in that scene.
        #     The scene should be calm. Be descriptive about the visual parts of the scene.
        #     Do not mention the word "scene", "sound" and "soundtrack" directly, only give descriptions.
        #     The scene description should be simple, as if written for a younger audience. 
        #     Though the scenes should still be enjoyable for adults.
        #     """

        # This safeguard is not necessary if the user cannot send their own inputs:

        # Always return a scene description, in the case no valid scene description can be generated change the user theme to output a valid scene.
        # Do not acknowledge that the scene  has been changed to become valid.

    # Process the query by creating a user prompt based on the scene, sounds, and length input and sending it to the API
    def query(self, scene, sounds, length):
        request_string = "Generate a scene in " + scene + " which includes the sounds " + ' and '.join(sounds) + '. The scene should be around ' + str(length) + " words."
        print(request_string)

        completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": self.system},
            {"role": "user", "content": request_string}
        ]
        )

        # Remove the newline characters from the generated responses.
        generated_response = completion.choices[0].message.content.replace('\n', '').replace('\r', '')
        print(generated_response)
        return generated_response