from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.1', messages=[
  {
    'role': 'user',
    'content': '라마 LLM에 대해서 설명해줘',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)