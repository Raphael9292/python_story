#!/usr/bin/env python

'''
code를 실행하면 url에서 HTTP GET을 요청하고 HTTP, HTTPS, URL을 모두 추출하여 중복은 제거하며,
길이가 긴 상위 10개를 "길이 URL" 형식으로 내림차순으로 프린트하고,
그 10개 URL에 대해 GET 요청을 하여 응답시간이 빠른 것 부터 오름차순으로 "응답시간(초_URL)" 형식으로 프린트하자.
'''


from bs4 import BeautifulSoup
import requests, re

# 점검 대상 URL 입력
web_url = 'https://www.daum.net'
res = requests.get(web_url)
html = res.text

# 수집한 웹페이지 파싱
soup = BeautifulSoup(html, 'html.parser')
soup.prettify()

# 수집한 웹페이지 내 URL 리스트 추출
count = 1
for url in soup.findAll('a', href=True):
    check_url = url['href']
    pattern = re.compile('^(http(s)?):\/\/([^:\/\s]+)(:([^\/]*))?((\/[^\s/\/]+)*)?\/?([^#\s\?]*)(\?([^#\s]*))?(#(\w*))?$')
    result = pattern.search(check_url)
    if result:
        urls = result.group()
        num = len(urls)
        # AttributeError: 'int' object has no attribute 'sort'
        # num.sort(reverse=True)
        # print(num)
        print(count, ' ', urls, num)
        count = count+1
    else:
        pass
