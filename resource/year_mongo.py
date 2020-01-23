import csv
import readline
import pandas as pd
import pymongo
# C:/Users/admin/Desktop/새 폴더/python/resources/total.csv
f = open('C:/Users/admin/Desktop/mp01/resource/total_year.csv', 'r', encoding="euc-kr")
rdr = csv.reader(f)
column = next(rdr) #[컬럼명 읽기]

# next(rdr) #[컬럼명 읽기]
# #column = next(rdr) #[컬럼명 읽기]

# for line in rdr:
#    print(line)


conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("year_total") # 있으면 가져오고, 없으면 만들어
table = db.get_collection("year") # 있으면 가져오고, 없으면 만들어

# df = pd.read_csv('./resources/korean_chulguk.csv')
# print(df)
# dict1 = df.to_dict()
# print(dict1)

for line in rdr:
   
    dict1 = dict()    
    for idx, val in enumerate(line):
        if idx == 0:
            pass
        dict1[column[idx]] = val
    print(dict1)

    table.insert_one(dict1)
conn.close()