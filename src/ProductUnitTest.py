
from ProductDocument import ProductTable
table = ProductTable()
table.createProductTable()
table.printProductTable()
table.dropTable()
table.createProductTable()
table.printProductTable()

from ProductDocument import Product
product = Product(name="example",price=21333.44, stock=4,description="this is my dope discription",restock_level=100, category="food", sale_flag=False)
product.__describe__()
product.printObj()
product.QueryPrintFromDatabase()
if product.getDocumentProductFromDB() is not None:
    print("ERROR~~~~~~~~~~~~~~~~~~~~~~~~getDocumentProductFromDB~~~~~~~~~~~~~~~~~~~~~~~~~")

product.insertDocumentIntoDB()

if product.getDocumentProductFromDB() is  None:
    print("ERROR~~~~~~~~~~~~~~~~~~~~~~~~insertDocumentIntoDB~~~~~~~~~~~~~~~~~~~~~~~~~")


if product.updateProductDocument(name="joe") is None:
    print("ERROR~~~~~~~~~~~~~~~~~~~~~~~~updateProductDocument~~~~~~~~~~~~~~~~~~~~~~~~~")

if product.getDocumentProductFromDB() is None:
    print("ERROR~~~~~~~~~updateProductDocument~~~~~~~~~~~~~~~getDocumentProductFromDB~~~~~~~~~~~~~~~~~~~~~~~~~")

product.updateProductObj(_id="Optional",name="Optional",price="Optional", stock="Optional",description="Optional",restock_level="Optional", category="Optional", sale_flag="Optional")

if product.getDocumentProductFromDB() is not None:
    print("ERROR~~~~~~~~~~~updateProductObj~~~~~~~~~~~~~getDocumentProductFromDB~~~~~~~~~~~~~~~~~~~~~~~~~")

