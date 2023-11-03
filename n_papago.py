# papago 번역 API 사용 - 함수 활용
import requests
import json
 
 
# translate 함수 선언
def translate(text, source='ko', target='en'):
    CLIENT_ID, CLIENT_SECRET = '0At29T7vkcGGyngOl5BY', 'DJShkQKQXe'
    url = 'https://openapi.naver.com/v1/papago/n2mt'
    headers = {
        'Content-Type': 'application/json',
        'X-Naver-Client-Id': CLIENT_ID,
        'X-Naver-Client-Secret': CLIENT_SECRET
    }
    data = {'source': 'ko', 'target': 'en', 'text': text}       #한글을 영어로
    response = requests.post(url, json.dumps(data), headers=headers)
    return response.json()['message']['result']['translatedText']
 
 
# 번역할 문장 입력 후 함수에 전달
text = input("입력하세요 : ")
en_text = translate(text)
print(en_text)
 
# 출처 :  https://icedhotchoco.tistory.com/entry/Papago-API