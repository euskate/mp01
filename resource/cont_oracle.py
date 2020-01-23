import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn.cursor()

conts = [
    ['asia', '아시아'],
    ['europe', '유럽'],
    ['africa', '아프리카'],
    ['america', '아메리카'],
    ['oceania', '오세아니아']
]

for data in conts:
    print(data)
    sql = """
        INSERT INTO COUNTRY_CONTINENTNAME(CONT, C_NAME)
        VALUES(:cont, :c_name)
    """
    cursor.execute(sql, cont=data[0], c_name=data[1])
    conn.commit()

conn.close()