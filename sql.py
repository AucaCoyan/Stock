import sqlite3

# -------------------DATABASE-------------------
# create the database
conn = sqlite3.connect(":memory:")

# create the cursor
c = conn.cursor()

# create the tables

c.execute("""CREATE TABLE workers (
            nameWorker text,
            sectorWorker text,
            boss text
            )
            """)

c.execute("""CREATE TABLE products (
            nameProduct text,
            stockProduct int,
            idProduct int 
            )
            """)

c.execute("""CREATE TABLE receipt (
            isEntry bol,
            worker str,
            sector str,
            idReceipt int,
            date timestamp
            )
            """)

c.execute("""CREATE TABLE itemsInReceipt(
            idReceipt int,
            idProduct int,
            nameProduct str, 
            quantityProduct int
            )
            """)

first_product = ["Hammer", 5, 1]


c.execute("INSERT INTO products VALUES (:name, :quantity, :id)",
          {'name': first_product[0],
           'quantity': first_product[1],
           'id': first_product[2]}
          )

# c.execute("DROP TABLE products")

conn.commit()

# conn.close()
