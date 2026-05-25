# OpenAi chat with tools
## tools (see https://github.com/beersheba26-telran/ai-agent/blob/main/tools.py)
- get_current_weather
- get_exchange_rate
### Defining tools object for the above tools
- this tools object should be used in chat request
## application
### console application
- answer from user
- getting response
- appending response to messages history with appropriate roles ( user, assistant, tool ) and contents, for example {"role": "user", "content":"is there life in Mars"}, {"role":"assistant", "content": "No one knows"}
- printing response in readable message format, like "No one knows" or "One USD is 2.9 ILS"
