from sql import c
from sql import conn
# import reportlab


class Product:
    def __init__(self, stock):  # When Object is created between () says the quantity
        self.stock = stock  # input("Insert the initial quantity:")  # quantity assignation


def add_product():
    print('A new product will be created')
    nameProduct = input('Name of the new product: ')
    stockProduct = int(input('Enter the initial quantity of the new product: '))
    #                                                                        todo: try not integer
    c.execute("SELECT MAX(idProduct) FROM products")  # search for the last id in the table products
    id = c.fetchall()
    id = id[0][0] + 1  # sums 1 and assign it to id variable
    print(id)
    # id = int(c.fetchall()[0][0]) + 1  # sums 1 and assign it to id variable
    #                                                                        todo: before creating, check if it's exist
    if product_lookup(nameProduct) is not None:
        print("The product already exists")
    else:
        c.execute("INSERT INTO products VALUES (?, ?, ?)", (nameProduct, stockProduct, id))
        conn.commit()
        print(nameProduct, ' was created with ', stockProduct, ' items.')


def product_lookup(nameProduct):
    """
    Finds a product,
    :param nameProduct: str
    :return: Returns the id of a product if it's found, else returns None
    """
    c.execute("SELECT * FROM products WHERE nameProduct=?", (nameProduct,))
    conn.commit()
    index = c.fetchall()  # saves the tuple result on index
    print(index)
    if index is None:
        print("product not found.")
        return  # print("The product doesn't exists")
    elif len(index) != 1:  # ask if there is more than one product with the same name
        print("There is more than one product")
        list_products()  # lists the products (actually not clear to the user)
        return
    else:
        print("The product is %s, quantity: %s, product id: %s" % (index[0][0], index[0][1], index[0][2]))


def del_product(nameProduct):
    if product_lookup(nameProduct) is None:
        return
    else:
        c.execute("DELETE FROM products WHERE name=?", (nameProduct,))  # todo: deletes all the products named "name"?
        print("Product deleted")


def list_products():
    c.execute("SELECT * FROM products")
    conn.commit()
    ptable = c.fetchall()
    print(ptable)


def printpdf(filename, ):
    filename = filename
