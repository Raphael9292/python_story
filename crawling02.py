# openAPI(NAVER)
# https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4

import urllib.request
import config

client_id = config.NAVER_CLIENTID
client_secret = config.NAVER_SECRET

search_keyword = ("비트코인")

encText = urllib.parse.quote(search_keyword)
url = "https://openapi.naver.com/v1/search/news.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/news.json?query=" + encText # xml 결과


request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)

# response_code
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
