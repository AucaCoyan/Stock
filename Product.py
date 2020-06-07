from sql import c
from sql import conn
import reportlab


class Product:
    def __init__(self, stock):  # When Object is created between () says the quantity
        self.stock = stock  # input("Insert the initial quantity:")  # quantity assignation


def add_product():
    print('A new product will be created')
    name = input('Name of the new product: ')
    stockProduct = int(input('Enter the initial quantity of the new product: '))
    #                                                                        todo: try not integer
    c.execute("SELECT MAX(id) FROM products")  # search for the last id in the table products
    id = c.fetchall()
    print(id)
    print(id[0][0])
    id = id[0][0] + 1  # sums 1 and assign it to id variable
    print(id)
    # id = int(c.fetchall()[0][0]) + 1  # sums 1 and assign it to id variable
    #                                                                        todo: before creating, check if it's exist
    if product_lookup(name) is not None:
        print("The product already exists")
    else:
        c.execute("INSERT INTO products VALUES (?, ?, ?)", (name, stockProduct, id))
        conn.commit()
        print(name, ' was created with ', stockProduct, ' items.')


# .......................LOOKUPS...........................

def product_lookup(product):
    if try_product(product) is None:
        return  # print("The product doesn't exists")
    else:
        c.execute("SELECT * FROM products WHERE nameProduct=?", (product, ))
    conn.commit()
    index = c.fetchall()  # saves the tuple result on index
    try:
        index[1]
    except IndexError:
        # print(index[1])
        print("There is more than one product")
    else: # not working
        print("The product is %s, quantity: %s, product id: %s" % (index[0][0], index[0][1], index[0][2]))


def del_product(product):
    if try_product(product) is None:
        return
    else:
        c.execute("DELETE FROM products WHERE name=?", (product, ))
        print("Product deleted")


# .......................TRY EXISTS...........................

def try_product(product):
    '''
    Finds a products,
    :param product: str
    :return: Returns the id of a product if it's found, else returns None
    '''
    c.execute("SELECT * FROM products WHERE nameProduct=?", (product, ))
    conn.commit()
    index = c.fetchone()  # saves the tuple result on index
    if index is not None:
        # print("index is not None")
        print("product found.")
        return index[2]  # returns the product_id
    else:
        # print("index IS None")
        print("Couldn't find the product.")
        return None


def list_products():
    c.execute("SELECT * FROM products")
    conn.commit()
    ptable = c.fetchall()
    print(ptable)

def printpdf(filename, ):
    filename = filename
