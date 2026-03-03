from ollama import chat

request_obj = {'role': 'user', 'content': '미국과 이스라엘의 이번 이란 공격이 얼마나 길게 이어질까?'}

stream = chat(
    model='llama3.1',
    messages=[request_obj],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='\n', flush=True)