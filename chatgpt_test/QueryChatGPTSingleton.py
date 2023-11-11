class QueryChatGPTSingleton():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(QueryChatGPTSingleton, cls).__new__(cls)
        return cls.instance
    
    def setup(self, client):
        self.client = client

    def query(self, input):
        completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are helping a user practice their imagination skills. For this you generate a short scene that they can imagine to alleviate migraine symptoms. These should be no longer than 50 words. The user will give a short theme of what they want. The scenes should never be scary. The scenes should be simple, as if written for a younger audience. Though the scenes should still be enjoyable for adults."},
            {"role": "user", "content": input}
        ]
        )

        # print(completion.choices[0].message.content)

        return completion.choices[0].message.content
