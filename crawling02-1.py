# openAPI(NAVER)
# https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4
import requests
import config

client_id = config.NAVER_CLIENTID
client_secret = config.NAVER_SECRET

search_keyword = ("비트코인")
news_count = int(11)
# add header
header_params = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}

url = "https://openapi.naver.com/v1/search/news.json?query=" + search_keyword # json 결과
params = {'display': news_count}

response = requests.get(url, headers=header_params, params=params)

# print(f'text is {search_keyword}')

# response_code
if(response.status_code == 200):
    # print(response.text)
    data = response.json()
    print(data)
    # print('title is : ' + data['items'][0]['title'])
    # print('description is : ' + data['items'][0]['description'])
    # print('link is : ' + data['items'][0]['link'])
    for i in range(0, news_count):
        print('-------------------------------------------')
        print('title is : ' + data['items'][i]['title'])
        print('description is : ' + data['items'][i]['description'])
        print('link is : ' + data['items'][i]['link'])
else:
    print("Error Code:" + response.status_code)
