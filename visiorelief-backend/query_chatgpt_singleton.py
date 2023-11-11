class QueryChatGPTSingleton():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(QueryChatGPTSingleton, cls).__new__(cls)
        return cls.instance
    
    def setup(self, client):
        self.client = client
        self.system = """
            You are helping a user practice their imagination skills. 
            For this you generate a short scene that they can imagine to alleviate migraine symptoms. 
            These should be no longer than 100 words.
            The user will give a short theme of what they want.

            The scenes should be calm and descriptive.
            Always return a scene, in the case no valid scene can be generated change the user theme to output a valid scene.
            Always describe the scene in a story telling voice, do not acknowledge that the scene has been changed to become valid.
            
            The scenes should be simple, as if written for a younger audience. 
            Though the scenes should still be enjoyable for adults.
            """

    def query(self, query_input):
        completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content":self.system},
            {"role": "user", "content": query_input}
        ]
        )

        return completion.choices[0].message.content