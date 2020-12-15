import pymysql

connection = pymysql.connect(host='127.0.0.1',
                             user='litkeyuser',
                            password='DBPASS',
                            db='litkey',
                            port = 3306
                             )
print(connection)
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
