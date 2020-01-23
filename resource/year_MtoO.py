import pymongo
import re
import cx_Oracle as oci
conn_o=oci.connect('admin/1234@192.168.99.100:32764/xe',encoding="euc-kr")
cursor=conn_o.cursor()

conn=pymongo.MongoClient('192.168.99.100',32766)
db=conn.get_database("csv_total") # 데이터가 들어가져야 몽고 만들어짐 없으면 db1생성 있으면 가져오는거
coll=db.get_collection("total1") # collection 있으면 가져오고 없으면 생성 이까지 테이블 만든거 데이터 들어기야 몽고에 들어감

data1=coll.find({},{'_id':False})
for tmp in data1:
    dict1=dict()
    dict1['a']=tmp['continent']
    dict1['b']=tmp['country']

    dict1['c'] = '0'

    if(tmp['2000'] != '' and tmp['2000'].strip() != '-'):
        dict1['c'] = tmp['2000'].replace(",","")
    dict1['d'] = '0'
    if(tmp['2001'] != '' and tmp['2001'].strip() != '-'):
        dict1['d'] = tmp['2001'].replace(",","")   
    dict1['e'] = '0'
    if(tmp['2002'] != '' and tmp['2002'].strip() != '-'):
        dict1['e'] = tmp['2002'].replace(",","")  
    dict1['f'] = '0'
    if(tmp['2003'] != '' and tmp['2003'].strip() != '-'):
        dict1['f'] = tmp['2003'].replace(",","")  
    dict1['g'] = '0'
    if(tmp['2004'] != '' and tmp['2004'].strip() != '-'):
        dict1['g'] = tmp['2004'].replace(",","")  
    dict1['h'] = '0'
    if(tmp['2005'] != '' and tmp['2005'].strip() != '-'):
        dict1['h'] = tmp['2005'].replace(",","")  
    dict1['i'] = '0'
    if(tmp['2006'] != '' and tmp['2006'].strip() != '-'):
        dict1['i'] = tmp['2006'].replace(",","")  
    dict1['j'] = '0'
    if(tmp['2007'] != '' and tmp['2007'].strip()!= '-'):
        dict1['j'] = tmp['2007'].replace(",","")  
    dict1['k'] = '0'
    if(tmp['2008'] != '' and tmp['2008'].strip() != '-'):
        dict1['k'] = tmp['2008'].replace(",","")  
    dict1['l'] = '0'
    if(tmp['2009'] != '' and tmp['2009'].strip() != '-'):
        dict1['l'] = tmp['2009'].replace(",","")  
    dict1['m'] = '0'
    if(tmp['2010'] != '' and tmp['2010'].strip() != '-'):
        dict1['m'] = tmp['2010'].replace(",","")  
    dict1['n'] = '0'
    if(tmp['2011'] != '' and tmp['2011'].strip() != '-'):
        dict1['n'] = tmp['2011'].replace(",","")  
    dict1['o'] = '0'
    if(tmp['2012'] != '' and tmp['2012'].strip() != '-'):
        dict1['o'] = tmp['2012'].replace(",","")  
    dict1['p'] = '0'
    if(tmp['2013'] != '' and tmp['2013'].strip() != '-'):
        dict1['p'] = tmp['2013'].replace(",","")  
    dict1['q'] = '0'
    if(tmp['2014'] != '' and tmp['2014'].strip() != '-'):
        dict1['q'] = tmp['2014'].replace(",","")  
    dict1['r'] = '0'
    if(tmp['2015'] != '' and tmp['2015'].strip() != '-'):
        dict1['r'] = tmp['2015'].replace(",","")  
    dict1['s'] = '0'
    if(tmp['2016'] != '' and tmp['2016'].strip() != '-'):
        dict1['s'] = tmp['2016'].replace(",","")  
    dict1['t'] = '0'
    if(tmp['2017'] != '' and tmp['2017'].strip() != '-'):
        dict1['t'] = tmp['2017'].replace(",","")  
    dict1['u'] = '0'
    if(tmp['2018'] != '' and tmp['2018'].strip() != '-'):
        dict1['u'] = tmp['2018'].replace(",","") 
    dict1['v'] = '0'
    if(tmp['2019'] != '' and tmp['2019'].strip() != '-'):
        dict1['v'] = tmp['2019'].replace(",","")         


    print("aaaa:",dict1)


    sql= """
        INSERT INTO COUNTRY_TRAVELBYCOUNTRY(CONTINENT, COUNTRY,Y2000,Y2001,Y2002,Y2003,Y2004,Y2005,Y2006,Y2007,Y2008,Y2009,Y2010,Y2011,Y2012,Y2013,Y2014,Y2015,Y2016,Y2017,Y2018,Y2019)
        VALUES(:a, :b, :c, :d, :e, :f, :g, :h, :i, :j,:k,:l,:m,:n,:o,:p,:q,:r,:s,:t,:u ,:v)
    """
    

    cursor.execute(sql,dict1)
    conn_o.commit()

conn_o.close() # 오라클 연결 끊기
conn.close()  # 몽고DB 연결 끊기COUNTRY_TRAVELBYCOUNTRY