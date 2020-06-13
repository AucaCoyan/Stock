from sql import c
from sql import conn
# import reportlab


class Product:
    def __init__(self, stock):  # When Object is created between () says the quantity
        self.stock = stock  # input("Insert the initial quantity:")  # quantity assignation


def add_product():
    print('A new product will be created')
    nameProduct = input('Name of the new product: ')
    while True:
        stockProduct = input('Enter the initial quantity of the new product: ')
        if stockProduct.isdigit():
            break
        else:
            print("Please insert a number.")
            continue
    stockProduct = int(stockProduct)
    c.execute("SELECT MAX(idProduct) FROM products")  # search for the last id in the table products
    id = c.fetchall()
    id = id[0][0] + 1  # sums 1 and assign it to id variable
    if product_lookup(nameProduct) != None:
        print("The product already exists")
    else:
        c.execute("INSERT INTO products VALUES (?, ?, ?)", (nameProduct, stockProduct, id))
        conn.commit()
        print(nameProduct, 'was created with ', stockProduct, ' items.')


def product_lookup(nameProduct):
    """
    Finds a product,
    :param nameProduct: str
    :return: Returns the info of the product if it's found, a statement if it found duplicates, or else returns None
    """
    print("Searching", nameProduct, "in database.")
    c.execute("SELECT * FROM products WHERE nameProduct=?", (nameProduct,))
    index = c.fetchall()  # saves the tuple result on index
    if index == []:
        print(nameProduct, "product couldn't be found.")
        return None
    elif len(index) > 1:    # ask if there is more than one product with the same name
        print("There is more than one product named", nameProduct)
        print(index)        # lists the products equally named nameProduct
        return len(index)   # returns the number of products with the same name (diffenent than return None)
    else:
        print("The product is %s, quantity: %s, product id: %s" % (index[0][0], index[0][1], index[0][2]))
        return 1            # the number of the products created


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
