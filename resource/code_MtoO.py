##### 몽고DB -> Oracle

import pymongo
import cx_Oracle as oci

conn_o = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn_o.cursor()

conn_m = pymongo.MongoClient('192.168.99.100',32766)
db = conn_m.get_database("mp01")
coll = db.get_collection("countrycode")

data1 = coll.find({},{'_id':False}) # id값 빼기
# data1 = coll.find()

for tmp in data1:
    print(tmp)
    sql = """
        INSERT INTO COUNTRY_COUNTRYNAME(CODE, C_NAME)
        VALUES(:code, :c_name)
    """
    cursor.execute(sql, tmp)
    conn_o.commit()

conn_o.close()      # 오라클 연결 끊기
conn_m.close()      # 몽고DB 연결 끊기