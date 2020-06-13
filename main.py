"""
Questions:
files about 300 lines long
"""

# -------------------------------------------------------------------------------
#                                      SECTION
# -------------------------------------------------------------------------------

# -------------------SUBSECTION-------------------

# -------------------Libraries & files-------------------

import document
import product
import sql

print(sql.first_product[2])

# import ui.py

# check if Document module is working

# receipt_1: object = document.Receipt()
# print(receipt_1)


# -------------------Classes-------------------


class Worker:
    def __init__(self, name, sector):
        self.name = name
        self.sector = sector
    pass


# -------------------Functions-------------------


# -------------------------------------------------------------------------------
#                            Star of the program
# -------------------------------------------------------------------------------


print('Welcome to the stock management software. \n')
while True:
    user_input = input("--------------------------------------\n"
                       "\n"
                       "Choose an option: \n "
                       "1-Add product \n "
                       "2-Look up for a product  \n"
                       "3-Delete a product \n"
                       "4-Create receipt \n"
                       "5-Look up for a receipt \n"
                       "6-Delete a reciept \n"
                       "7-List products  \n"
                       "8-List recipts  \n"
                       "  \n"
                       "To exit, press N\n"
                       "\n"
                       "User input: ")
    if user_input == "1":
        product.add_product()
    if user_input == "2":
        product.product_lookup(input("Enter the name of the product to look up: "))
    if user_input == "3":
        product.del_product(str(input("Enter the product name to delete: ")))
    if user_input == "4":
        document.add_receipt()
    if user_input == "5":
        document.receipt_lookup(int(input("Enter the number of the receipt to look up: ")))
    if user_input == "6":
        document.del_receipt()
    if user_input == "7":
        product.list_products()
    if user_input == "8":
        document.list_receipts()
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

# conn.close()
