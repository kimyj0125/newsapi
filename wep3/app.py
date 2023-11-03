from flask import Flask, render_template, request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openai
import json
import threading

app = Flask(__name__)

# OpenAI API 키 설정
openai.api_key = "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"

content=''
messages=[]
completion=''

@app.route('/', methods=['GET', 'POST'])



def index():
    global content
    global completion
    global messages
    
    if request.method == 'POST':
        # HTML 폼에서 'text' 필드에서 데이터를 가져옵니다.
        input_url = request.form['url']
        
        # url 입력받아 기사 본문 크롤링
        html = urlopen(input_url)
        bs = BeautifulSoup(html.read(), 'html.parser')

        content = bs.find('article', {'id':'dic_area'}).get_text()
        content = f"{content.split('기자 = ')[-1]}를 간략히 요약해 줘"
        
        messages.append({"role":"user", "content":content})
        
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, stream=True)
        
    return render_template('index.html')


def stream_response():
    
    global completion

    for item in completion:
        message = item.choices[0].delta.content
        messages.append({"role": "assistant", "content": message})



@app.route('/get_messages')
def get_messages():
    
    return json.dumps(messages)

@app.after_request
def after_request(response):
    t = threading.Thread(target=stream_response)
    t.start()
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)