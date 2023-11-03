from flask import Flask, render_template, request

import os
import sys
import json
import urllib.request

client_id = "0At29T7vkcGGyngOl5BY"
client_secret = "DJShkQKQXe"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", message="")


@app.route("/result", methods=["POST"])
def result():
    

    text = request.form["input_data"]
    encText = urllib.parse.quote(text)  #  " "에 검색할 입력값

    url = "https://openapi.naver.com/v1/search/news?query=" + encText  # JSON 결과 뉴스검색
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    news = urllib.request.Request(url)
    news.add_header("X-Naver-Client-Id", client_id)
    news.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(news)

    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        newsdata = response_body.decode("utf-8")
        newsdatas = json.loads(newsdata)
        #titles = [item['title'] for item in newsdatas['items']]     #제목
        links = [item['link'] for item in newsdatas['items']]       #링크
        naver_links = [link for link in links if 'naver.com' in link]
        n_link = naver_links[0]
        
    else:
        print("Error Code:" + rescode)

    user_input = n_link         #출력값
    return render_template("index.html", message=f"You entered: {user_input}")

if __name__ == "__main__":
    app.run(debug=True)
