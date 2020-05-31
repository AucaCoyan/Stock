import sql.connector
# -------------------DATABASE-------------------
# create the database
conn = sqlite3.connect(":memory:")

# create the cursor
c = conn.cursor(buffered=True)

# create the tables / Suspended because they are already created
# Should put this on a different file and check if the tables exist, and make them otherwise
#
# c.execute("""CREATE TABLE workers (
#             name text,
#             sector text,
#             boss text
#             )
#             """)
#
# c.execute("DROP TABLE products")

# c.execute("""CREATE TABLE products (
#             name text,
#             quantity int,
#             id int AUTO_INCREMENT PRIMARY KEY
#             )
#             """)

conn.commit()
