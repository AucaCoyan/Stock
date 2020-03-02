"""
Dudas:
A-Visual web or application
"""

# -------------------------------------------------------------------------------
#                                      SECTION
# -------------------------------------------------------------------------------

# -------------------SUBSECTION-------------------

# -------------------Libraries & files-------------------
# todo: load different files

# -------------------Classes-------------------
# import ui.py


class Object:
    def __init__(self, stock):
        self.stock = 0
    pass

# Hardcoded Objects todo: load objects from an existent .csv


pencil = Object(10)
print(pencil.stock)

pencil.stock = 10

print(pencil.stock)


'''
class Tool(Object):
    pass


class Worker:
    def __init__(self, name, sector,):
        self.name = name
        self.sector = none
    pass


class Receipt:
    pass


class Supplier:
    pass

'''

# -------------------Functions-------------------

def addProduct():
    print("A new product will be created")
    productname = input("Name of the new product: ")
    print(productname, " was created")
    pass


# -------------------------------------------------------------------------------
#                            Star of the program
# -------------------------------------------------------------------------------

print("Welcome to the stock management software. \n")
while True:
    userinput = input("--------------------------------------\n"
                      "START. \n "
                      "\n"
                      "Choose an option: \n "
                      "1-Add Product \n "
                      "2-Crear producto \n"
                      "3- \n"
                      "Para finalizar, presione N\n"
                      "\n"
                      "Opcion a elegir: ")
    if userinput == "1":
        addProduct()
    # if userinput == "2":
    #     crearproducto()
    # if userinput == "3":
    #     creartransaccion()
    # if userinput == "4":
    #     consultarcliente(int(input("Ingrese el CODIGO del cliente a buscar: ")))
    # if userinput == "5":
    #     buscarcliente(input("Ingrese nombre/apellido/CUIT del cliente a buscar: "))
    # if userinput == "6":
    #     borrarclientes(int(input("Ingrese el CODIGO del cliente a borrar: ")))
    # if userinput == "7":
    #     borrarproducto(int(input("Ingrese el CODIGO del producto a borrar: ")))
    # if userinput == "8":
    #     borrartransaccion(int(input("Ingrese el CODIGO de la transaccion a borrar: ")))
    # if userinput == "9":
    #     consultartransaccion(int(input("Ingrese el CODIGO de la transaccion a buscar: ")))
    # if userinput == "10":
    #     print(clientList)
    # if userinput == "11":
    #     print(transaccionList)
    # if userinput == "12":
    #     calculartransaccion(int(input("Ingrese el CODIGO de la transaccion a calcular: ")))
    # if userinput == "13":
    #     calculardeudacliente(int(input("Ingrese el CODIGO del cliente a calcular su deuda: ")))
    if userinput == "n" or userinput == "N":
        break
