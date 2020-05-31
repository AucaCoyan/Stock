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

# -------------------SUBSECTION-------------------

# -------------------Libraries & files-------------------

import document
import product
import sqlite3

# import ui.py

# check if Document module is working
from product import Product

receipt_1: object = document.Receipt()
print(receipt_1)


# -------------------Classes-------------------


class Worker:
    def __init__(self, name, sector):
        self.name = name
        self.sector = sector
        # self.name = input("Insert the name of the worker:")
        # self.sector = input("Insert the sector of the worker:")

    pass


# -------------------Functions-------------------


# -------------------------------------------------------------------------------
#                            Star of the program
# -------------------------------------------------------------------------------


print('Welcome to the stock management software. \n')
while True:
    user_input = input("--------------------------------------\n"
                       "START. \n "
                       "\n"
                       "Choose an option: \n "
                       "1-Add Product \n "
                       "2-Look up for a product  \n"
                       "7-Delete a product  \n"
                       "  \n"
                       "To exit, press N\n"
                       "\n"
                       "User input: ")
    if user_input == "1":
        product.add_product()
    if user_input == "2":
        product.product_lookup(input("Enter the name of the product to look up: "))
    # if user_input == "3":
    #     creartransaccion()
    # if user_input == "4":
    #     consultarcliente(int(input("Ingrese el CODIGO del cliente a buscar: ")))
    # if user_input == "5":
    #     buscarcliente(input("Ingrese nombre/apellido/CUIT del cliente a buscar: "))
    # if user_input == "6":
    #     borrarclientes(int(input("Ingrese el CODIGO del cliente a borrar: ")))
    if user_input == "7":
        product.del_product(str(input("Enter the product name to delete: ")))
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
