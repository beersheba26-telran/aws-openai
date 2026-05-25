from dotenv import load_dotenv
from os import getenv
from openai import OpenAI
load_dotenv()
client = OpenAI(
   
)

response = client.chat.completions.create(
    model="openai.gpt-oss-20b",
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

print(response.choices[0].message.content)