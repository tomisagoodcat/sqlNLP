import pymssql
import pyltp
from pyltp import SentenceSplitter
conn = pymssql.connect(host='192.168.0.106\TOMISAGOODCAT',user='sa',
                       password='Tomis1cat',database='IASDB4Neo',
                      charset="utf8")
#查看连接是否成功
#print conn
cursor = conn.cursor()
sql = 'select * from dic'
cursor.execute(sql)
 
rs = cursor.fetchall()
print(rs)

import pyltp
 
