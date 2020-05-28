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

import sqlite3
# create the database
conn = sqlite3.connect('database.db')
# create the cursor
c = conn.cursor()

# create the tables / Suspended because they are already created
# Should put this on a different file and check if the tables exist, and make them otherwise
#
# c.execute("""CREATE TABLE workers (
#             firstName text,
#             lastName text,
#             sector text,
#             boss text
#             )
#             """)

c.execute("DROP TABLE products")

c.execute("""CREATE TABLE products (
            productName text,
            productQuantity int
            )
            """)

conn.commit()


# -------------------SUBSECTION-------------------

# -------------------Libraries & files-------------------

# -------------------Classes-------------------
# import ui.py


class Object:
    def __init__(self):  # When Object is created between () says the quantity
        self.stock = input("Insert the initial quantity:")  # quantity assignation

    pass


# Hardcoded Objects

'''
pencil = Object()
print(pencil.stock)

pencil.stock = 10

print(pencil.stock)
'''

class Worker:
    def __init__(self, ):
        self.name = input("Insert the name of the worker:")
        self.sector = input("Insert the sector of the worker:")
    pass


'''

class Receipt:
    pass

class Supplier:
    pass

'''


# -------------------Functions-------------------


def add_product():
    print('A new product will be created')
    product_name = input('Name of the new product: ')
    product_quantity = int(input('Enter the initial quantity of the new product: '))
    c.execute("INSERT INTO product VALUES (?, ?)", (product_name, product_quantity))
    conn.commit()
    print(product_name, ' was created with ', product_quantity, ' items.')
    pass



# .......................LOOKUPS...........................


def product_lookup(product):
    # if hasattr(product, "Object") is False:
    #     raise
    #   pass
    # else:
    lookup = c.execute("SELECT * FROM products WHERE productName=?", (product))
    conn.commit()
    print(lookup)

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