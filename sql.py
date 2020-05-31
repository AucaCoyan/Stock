import sqlite3

# -------------------DATABASE-------------------
# create the database
conn = sqlite3.connect(":memory:")

# create the cursor
c = conn.cursor()

# create the tables

c.execute("""CREATE TABLE workers (
            name text,
            sector text,
            boss text
            )
            """)

c.execute("""CREATE TABLE products (
            name text,
            quantity int,
            id int 
            )
            """)

first_product = ["Hammer", 5, 1]

print(first_product[2])
c.execute("INSERT INTO products VALUES (:name, :quantity, :id)",
          {'name': first_product[0],
           'quantity': first_product[1],
           'id': first_product[2]}
          )

# c.execute("DROP TABLE products")

conn.commit()

# conn.close()
