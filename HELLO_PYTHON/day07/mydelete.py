import pymysql

e_id="3"

conn = pymysql.connect(host='localhost', user='root', password='python', port=3305,
                       db='python', charset='utf8')

curs = conn.cursor()
 
sql = f"""
    delete from emp
    where
        e_id = '{e_id}'
"""

cnt = curs.execute(sql)
print("cnt",cnt)

conn.commit()
curs.close()
conn.close()