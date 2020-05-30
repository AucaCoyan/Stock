"""
Questions:
load different files
split classes
load objects from an existent .csv / sqlite3
files about 300 lines long
"""

# -------------------------------------------------------------------------------
#                                      SECTION
# -------------------------------------------------------------------------------

import mysql.connector

# create the database
# conn = sqlite3.connect(":memory:")

# connect to the database
conn = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='stock'
)

# create the cursor
c = conn.cursor()

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


# -------------------SUBSECTION-------------------

# -------------------Libraries & files-------------------

# -------------------Classes-------------------
# import ui.py


class Product:
    def __init__(self, stock):  # When Object is created between () says the quantity
        self.stock = stock  # input("Insert the initial quantity:")  # quantity assignation

    pass


class Document:
    pass


class Worker:
    def __init__(self, name, sector):
        self.name = name
        self.sector = sector
        # self.name = input("Insert the name of the worker:")
        # self.sector = input("Insert the sector of the worker:")

    pass


class Receipt(Document):
    pass


class Lending(Document):
    pass

# -------------------Functions-------------------


def add_product():
    print('A new product will be created')
    name = input('Name of the new product: ')
    quantity = int(input('Enter the initial quantity of the new product: '))
    #                                                                        todo: try not integer
    c.execute("SELECT MAX(id) FROM products")       # search for the last id in the table products
    id = int((c.fetchall()[0])[0]) + 1              # sums 1 and assign it to id variable
    c.execute("INSERT INTO products VALUES (%s, %s, %s)", (name, quantity, id))
    conn.commit()
    print(name, ' was created with ', quantity, ' items.')


# .......................LOOKUPS...........................


def product_lookup(product):
    # if hasattr(product, "Object") is False:
    #     raise
    #   pass
    # else:
    lookup = c.execute("SELECT * FROM products WHERE name=%s", (product,))
    conn.commit()
    print(c.fetchall(lookup)[0])

    pass


# .......................TRY EXISTS...........................

def try_product(product):
    try:
        product.Object
    except:
        print("Product can't be found.")
        return False
    else:
        return True


# -------------------------------------------------------------------------------
#                            Star of the program
# -------------------------------------------------------------------------------


print('Welcome to the stock management software. \n')
while True:
    user_input = input('--------------------------------------\n'
                       'START. \n '
                       '\n'
                       'Choose an option: \n '
                       '1-Add Product \n '
                       '2-Look up for a product  \n'
                       '  \n'
                       'To exit, press N\n'
                       '\n'
                       'User input: ')
    if user_input == "1":
        add_product()
    if user_input == "2":
        product_lookup(input("Enter the name of the product to look up: "))
    # if user_input == "3":
    #     creartransaccion()
    # if user_input == "4":
    #     consultarcliente(int(input("Ingrese el CODIGO del cliente a buscar: ")))
    # if user_input == "5":
    #     buscarcliente(input("Ingrese nombre/apellido/CUIT del cliente a buscar: "))
    # if user_input == "6":
    #     borrarclientes(int(input("Ingrese el CODIGO del cliente a borrar: ")))
    # if user_input == "7":
    #     borrarproducto(int(input("Ingrese el CODIGO del producto a borrar: ")))
    # if user_input == "8":
    #     borrartransaccion(int(input("Ingrese el CODIGO de la transaccion a borrar: ")))
    # if user_input == "9":
    #     consultartransaccion(int(input("Ingrese el CODIGO de la transaccion a buscar: ")))
    # if user_input == "10":
    #     print(clientList)
    # if user_input == "11":
    #     print(transaccionList)
    # if user_input == "12":
    #     calculartransaccion(int(input("Ingrese el CODIGO de la transaccion a calcular: ")))
    # if user_input == "13":
    #     calculardeudacliente(int(input("Ingrese el CODIGO del cliente a calcular su deuda: ")))
    if user_input == "n" or user_input == "N":
        break

conn.close()
