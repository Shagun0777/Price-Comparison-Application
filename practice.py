import sqlite3
conn=sqlite3.connect('laptop.db')
c=conn.cursor()
# c.execute("DROP TABLE IF EXISTS one")
# c.execute("""CREATE  TABLE  one(
#           model_number TEXT PRIMARY KEY,price INT NOT NULL,link TEXT NOT NULL
#           );""")
# conn.commit()
# c.execute("""delete  from one""")
c.execute(""" select count(*) from one """)
# c.execute("DROP TABLE IF EXISTS one")
# c.execute("""update  one set amazon_price='',amazon_link='' where amazon_price is NULL""")
# c.execute("""update  one set filpkart_price='',flipkart_link='' where filpkart_price is NULL""")
data=c.fetchall()
print(data)
conn.commit()