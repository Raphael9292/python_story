import json
import os

import config
import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

ID = config.IDENTITY
PW = config.PASSWORD
SLACK_WEBHOOK_URL = config.SLACK_WEBHOOK_URL

AUTO_LOTTO_COUNT = '2'
HEADERS = {
    "Content-type": "application/json"
}

# For windows crontab
# C:\Program Files (x86)\cron\cron.tab
# change current directory
os.chdir('C:\\Users\\Administrator\\Desktop\\python_story')

DRIVER_PATH = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# Login
LOTTO_URL = 'https://www.dhlottery.co.kr/user.do?method=login&returnUrl='
driver.get(LOTTO_URL)

# account_ID
elem_login = driver.find_element_by_id('userId')
elem_login.send_keys(ID)

# account_PW
elem_login = driver.find_element_by_name('password')
elem_login.clear()
elem_login.send_keys(PW)

# Login Click
LOGIN_XPATH = '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a'
driver.find_element_by_xpath(LOGIN_XPATH).click()

# 구매창 이동
driver.get('https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40')

# 자동번호발급 이동
# UnexpectedAlertPresentException
try:
    driver.switch_to.frame('ifrm_tab')
    driver.find_element_by_xpath('//*[@id="num2"]').click()

# 실패시 에러원인 슬랙 & 세션 종료
except Exception as e:
    fail_data = {
        "username": "Fail-Buy",
        "text": '<@UUTQGQDS6>' + str(e)
    }
    res = requests.post(SLACK_WEBHOOK_URL, headers=HEADERS, data=json.dumps(fail_data))
    driver.close()

# 적용 수량 선택
select = Select(driver.find_element_by_xpath('//*[@id="amoundApply"]'))
select.select_by_value(AUTO_LOTTO_COUNT)

# 확인 버튼 클릭
driver.find_element_by_xpath('//*[@id="btnSelectNum"]').click()

# 나의로또번호 이동
# driver.switch_to.frame('ifrm_tab')
driver.find_element_by_xpath('//*[@id="num4"]').click()

# myList 선택
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element
wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="myList"]/li[1]/input'))).click()
# driver.find_element_by_xpath('//*[@id="myList"]/li[1]/input').click()
driver.find_element_by_xpath('//*[@id="myList"]/li[2]/input').click()
driver.find_element_by_xpath('//*[@id="myList"]/li[3]/input').click()

# 확인 버튼 클릭
driver.find_element_by_xpath('//*[@id="divWay2Buy3"]/div[2]/input[1]').click()

# 구매하기 클릭
driver.find_element_by_xpath('//*[@id="btnBuy"]').click()

# 알람창 확인
alert = driver.switch_to.alert
alert.accept()

# 성공 슬랙
success_data = {
    "username" : "Success-Buy",
    "text" : '<@UUTQGQDS6>' + 'Check your result'
}
res = requests.post(SLACK_WEBHOOK_URL, headers=HEADERS, data=json.dumps(success_data))

# chrome 종료
driver.close()

# 예치금 부족이라면?