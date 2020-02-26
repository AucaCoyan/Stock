
# -------------------------------------------------------------------------------
#                                      SECTION
# -------------------------------------------------------------------------------

# -------------------SUBSECTION-------------------


# -------------------Classes-------------------

class Object:
    def __init__(self, name):
        self.name = name
        self.Deposit = []
        self.Deposit.append(Available)


# -------------------------------------------------------------------------------
#                            Star of the program
# -------------------------------------------------------------------------------

print("Welcome to the stock management software. \n")
while True:
    userinput = input("--------------------------------------\n"
                           "START. \n "
                           "\n"
                           "Choose an option: \n "
                           "1-Crear cliente \n "
                           "2-Crear producto \n"
                           "3- \n"
                           "4- \n"
                           "5- \n"
                           "6- \n"
                           "7- \n"
                           "8- \n"
                           "9- \n"
                           "10- \n"
                           "11- \n"
                           "12- \n"
                           "13-"
                           "\n"
                           "Para finalizar, presione N\n"
                           "\n"
                           "Opcion a elegir: ")
    if userinput == "1":
        crearcliente()
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
    if ingresousuario == "n" or ingresousuario =="N":
        break
