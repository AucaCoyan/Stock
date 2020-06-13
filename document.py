class Document:
    pass


class Receipt(Document):
    pass


class Lending(Document):
    pass


def add_receipt():
    print("not implemented yet")


def receipt_lookup(receipt):
    """
    :param receipt: int
    :return: details of the reciept
    """
    print("not implemented yet" + receipt)
    pass


def del_receipt():
    pass


def list_receipts():
    pass


# from reportlab.pdfgen import canvas
#
#
# def hello(c):
#     c.drawString(100, 100, "Hello World")
#
#
# c = canvas.Canvas("hello.pdf")
# hello(c)
# c.showPage()
# c.save()