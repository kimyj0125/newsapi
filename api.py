#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
import openai

openai.api_key = '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'  # <- api_key 입력

while True:
  # 사용자 질문 입력
  prompt = input('Q:')

  # 응답
  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", # 사용할 모델
                                            # 보낼 메세지 목록
                                            messages=[{"role": "system", "content":"챗봇"},
                                                      {"role": "user", "content": prompt}]) # 사용자

  # 출력
  response = completion.choices[0].message.content
  print(f'A: {response}')

  #출처 : https://passwd.tistory.com/entry/Python-OpenAI-API-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0