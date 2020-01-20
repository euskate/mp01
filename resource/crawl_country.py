###### 국가명, 국가 코드 크롤링 - 리스트에 저장

from bs4 import BeautifulSoup
import requests   

url="https://ko.wikipedia.org/wiki/%EA%B5%AD%EA%B0%80%EB%B3%84_%EA%B5%AD%EA%B0%80_%EC%BD%94%EB%93%9C_%EB%AA%A9%EB%A1%9D"
str=requests.get(url)

soup = BeautifulSoup(str.text, 'html.parser')

all_tds_on=soup.find_all('tr')


list1 = list()

for tmp in all_tds_on:
    n = tmp.text.split('\n')
    countryname = n[1].strip()
    countrycode = n[2]
    a = countrycode, countryname
    list1.append(a)

print(list1)

##### list -> 몽고DB에 저장

import pymongo

conn_m = pymongo.MongoClient('192.168.99.100',32766)
db = conn_m.get_database("mp01")
coll = db.get_collection("countrycode")

for cc, cn in list1:
    one = dict()
    one['code'] = cc
    one['c_name'] = cn
    coll.insert_one(one)
conn_m.close()

##### 몽고DB -> oracle에 저장