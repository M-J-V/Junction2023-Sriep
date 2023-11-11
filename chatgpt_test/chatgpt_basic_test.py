# python -m venv openai-env
# openai-env\Scripts\activate
# pip install --upgrade openai
# pip install python-dotenv

from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "You are helping a user practice their imagination skills. For this you generate a short scene that they can imagine to alleviate migraine symptoms. These should be no longer than 50 words. The user will give a short theme of what they want. The scenes should never be scary. The scenes should be simple, as if written for a younger audience. Though the scenes should still be enjoyable for adults."},
    # {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "I want a scene where I walk through a forest"}
  ]
)

print(completion.choices[0].message)