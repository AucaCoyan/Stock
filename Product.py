from sql import c
from sql import conn


class Product:
    def __init__(self, stock):  # When Object is created between () says the quantity
        self.stock = stock  # input("Insert the initial quantity:")  # quantity assignation


def add_product():
    print('A new product will be created')
    name = input('Name of the new product: ')
    quantity = int(input('Enter the initial quantity of the new product: '))
    #                                                                        todo: try not integer
    c.execute("SELECT MAX(id) FROM products")  # search for the last id in the table products
    id = int((c.fetchall()[0])[0]) + 1  # sums 1 and assign it to id variable
    #                                                                        todo: before creating, check if it's exist
    if product_lookup(name) is not None:
        print("The product already exists")
    else:
        c.execute("INSERT INTO products VALUES (%s, %s, %s)", (name, quantity, id))
        conn.commit()
        print(name, ' was created with ', quantity, ' items.')


# .......................LOOKUPS...........................

def product_lookup(product):
    if try_product(product) is None:
        return
    else:
        c.execute("SELECT * FROM products WHERE name=%s", (product,))
    conn.commit()
    index = c.fetchone()  # saves the tuple result on index
    # print(index)
    print("The product is %s, quantity: %s, product id: %s" % (index[0][0], index[0][1], index[0][2]))
    return None


def del_product(product):
    if try_product(product) is None:
        return
    else:
        c.execute("DELETE FROM products WHERE name=%s", (product,))
        print("Product deleted")


# .......................TRY EXISTS...........................

def try_product(product):
    '''
    Finds a products,
    :param product:
    :return: Returns the id of a product if it's found, else returns None
    '''
    c.execute("SELECT * FROM products WHERE name=%s", (product,))
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