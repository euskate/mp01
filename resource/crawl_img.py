from selenium import webdriver
import urllib.request
import os

options = webdriver.ChromeOptions()

options.add_argument('headless')        # 화면으로 표시 안함
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome('./chromedriver.exe', options=options)

url = "https://ko.wikipedia.org/wiki/%EA%B5%AD%EA%B0%80%EB%B3%84_%EA%B5%AD%EA%B0%80_%EC%BD%94%EB%93%9C_%EB%AA%A9%EB%A1%9D"

driver.get(url)

for i in range(0,64):
code = driver.find_element_by_css_selector("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr[1]/td[2]")
img = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr[1]/td[1]/span/a/img")
#mw-content-text > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > span > a > img
#mw-content-text > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > span > a > img
#mw-content-text > div > table > tbody > tr:nth-child(249) > td:nth-child(1) > span > a > img

filename = code.text
/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr[3]/td[1]/span/a/img

file = img.get_attribute("src") # 찾은 태그 중에서 src의 값

urllib.request.urlretrieve(file, "./static/img/"+ filename +".png")