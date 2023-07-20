import sqlite3
conn=sqlite3.connect('laptop.db')
c=conn.cursor()
import re
# out=re.sub(' ','','14s - dy2507TU')
# print(out)
# out=out.upper()
# print(out)
# query="""select model_"""
# c.execute("""drop table product""")
# conn.commit()
# c.execute("""CREATE  TABLE product(
#           model_number TEXT PRIMARY KEY,amazon_price INT ,amazon_link TEXT ,flipkart_price INT ,flipkart_link TEXT
#           );""")
# conn.commit()
c.execute("""select * from product  """)
rows=c.fetchall()
# print(rows)
for row in rows:
    print(row)
conn.commit()
# for row in rows:
#     my_list=list(row)
#     out=re.sub(' ','',row[0])
#     out=out.upper()
#     my_list[0]=out
#     row=tuple(my_list)
#     print(row[0])
#     # c.execute("""insert or ignore """)
#     c.execute('INSERT OR IGNORE INTO product VALUES(?,?,?,?,?)',row)
#     if(row[1]==''):
#         rr=(row[3],row[4],row[0])
#         c.execute('update product set flipkart_price=?,flipkart_link=? where model_number=?',rr)
#     if(row[3]==''):
#         rr=(row[1],row[2],row[0])
#         c.execute('update product set amazon_price=?,amazon_link=? where model_number=?', rr)
#     conn.commit()
# # # # conn.commit()
# # # # conn.close()
# # # # data_tuple = ("MADh","",94)
# # # # # # c.execute(query,data_tuple)
# # # # data_t=("MADH",44,"MADh")
# # # # c.execute('INSERT OR IGNORE INTO TEST VALUES(?,?,?)', data_tuple)
# # # # c.execute('update TEST SET name=?,price=? WHERE name=?', data_t)
# # # # # # c.execute("INSERT INTO  TEST VALUES ('MADHU',999)")
# # # # conn.commit()
# # # # sqlite_select_query = """SELECT * from TEST"""
# # # # c.execute(sqlite_select_query)
# # # # records = c.fetchall()
# # # # print(records)
# # # # conn.close()
# # # # # import sqlite3
# # # # # # conn=sqlite3.connect('laptop.db')
# # # # # # c=conn.cursor()
# # # # # # # c.execute("DROP TABLE IF EXISTS one")
# # # # # # # c.execute("""CREATE  TABLE  one(
# # # # # # #           model_number TEXT PRIMARY KEY,price INT NOT NULL,link TEXT NOT NULL
# # # # # # #           );""")
# # # # # # # conn.commit()
# # # # # # # c.execute("""delete  from one""")
# # # # # # c.execute("""select * from one""")
# # # # # # c.execute("DROP TABLE IF EXISTS one")
# # # # # data=c.fetchall()
# # # # print(data)
# # conn.commit()