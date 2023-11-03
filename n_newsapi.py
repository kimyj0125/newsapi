# 0At29T7vkcGGyngOl5BY  DJShkQKQXe

# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import json
import urllib.request
import re

#client_id = "YOUR_CLIENT_ID"
#client_secret = "YOUR_CLIENT_SECRET"
client_id = "0At29T7vkcGGyngOl5BY"
client_secret = "DJShkQKQXe"

text = input("입력하세요 : ")
encText = urllib.parse.quote(text)  #  " "에 검색할 입력값

url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과 뉴스검색
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)

rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    newsdata = response_body.decode('utf-8')
    newsdatas = json.loads(newsdata)
    titles = [item['title'] for item in newsdatas['items']]     #제목
    links = [item['link'] for item in newsdatas['items']]       #링크
    naver_links = [link for link in links if 'naver.com' in link]

    clean_title = re.sub(r"[^가-힣\s]", "", titles[0]).strip()  # 한글과 공백을 제외한 나머지 문자 제거
    print(titles[0])
    print(clean_title)    
    print(naver_links[0])

else:
    print("Error Code:" + rescode)


# 출처 : https://developers.naver.com/docs/serviceapi/search/blog/blog.md