import mysql.connector
import pandas as pd
import os

print("------",os.getenv("DBPASS"))
con = mysql.connector.connect(user='litkeyuser'
							, password=os.getenv("DBPASS"), #'DBPASS',
                              host='127.0.0.1',
                              database='litkey')

print(con)

try:

    print(pd.read_sql('SELECT VERSION()', con))


finally:

    con.close()


#
#import pymysql
#
#connection = pymysql.connect(host='12.0.0.1',
#                             user='litkeyuser',
#                            password='DBPASS',
#                            db='litkey',
#                            port = 3306
#                             )
#
#
## 
## con = pymysql.connect('127.0.0.1'
## 						, 'litkeyuser'
##     					, 'DBPASS'
##     					, 'litkey')
#
#try:
#
#    with con.cursor() as cur:
#
#        cur.execute('SELECT VERSION()')
#
#        version = cur.fetchone()
#
#        print(f'Database version: {version[0]}')
#
#finally:
#
#    con.close()
