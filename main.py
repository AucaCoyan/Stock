"""
Questions:
A-Visual web or application

to do:
ui.py
load different files
load objects from an existent .csv

"""


# -------------------------------------------------------------------------------
#                                      SECTION
# -------------------------------------------------------------------------------

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
    print(type(product_quantity))
    product_name.Object = product_quantity + 1
    print(product_name, ' was created. With ', product_quantity, ' items.')
    pass


# .......................LOOKUPS...........................


def product_lookup(product):
    if try_product(product) is False:
        raise
    #   pass
    else:
        product = Object()
        print("The Product is %s \n " % product.stock)
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
