import json

from openai import OpenAI
from dotenv import load_dotenv  
from os import getenv
from tools import TOOL_FUNCTIONS, tools 
load_dotenv()
client = OpenAI()
response = client.chat.completions.create(
    model="openai.gpt-oss-20b",
    messages=[
        {"role": "user", "content": "What is the currency name in Israel and what is the weather in Rehovot?"}],
    tools=tools,
    tool_choice="auto"
)
print(response.usage)  # Print usage information
message = response.choices[0].message
if message.tool_calls:
    tool_call = message.tool_calls[0]
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    print("Tool requested:", function_name)
    print("Arguments:", arguments)
    print (TOOL_FUNCTIONS[function_name](**arguments))
if message.content:    
    print(f"Model response: {message.content}")
else :
    print(message)