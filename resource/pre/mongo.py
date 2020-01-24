import csv
import readline
import pandas as pd
import pymongo
import os
print(os.getcwd())

f = open('./resource/asia.csv', 'r', encoding="utf-8")
rdr = csv.reader(f)
column = next(rdr) #[컬럼명 읽기]


# next(rdr) #[컬럼명 읽기]
# #column = next(rdr) #[컬럼명 읽기]

# for line in rdr:
#    print(line)

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("csv_chulguk1") # 있으면 가져오고, 없으면 만들어
table = db.get_collection("africa") # 있으면 가져오고, 없으면 만들어

df = pd.read_csv('africa.csv')
print(df)
dict1 = df.to_dict()
print(dict1)

# for line in rdr:
   
#     dict1 = dict()    
#     for idx, val in enumerate(line):
#         dict1[column[idx]] = val
#     print(dict1)

#     table.insert_one(dict1)
conn.close()