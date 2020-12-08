
from CustomerDocument import CustomerTable
table = CustomerTable()
table.createCustomerTable()
table.printCustomerTable()
table.dropTable()
table.createCustomerTable()
table.printCustomerTable()

from CustomerDocument import Customer
customer = Customer(firstname="example",lastname="example", email="example@gmail.com")
customer.__describe__()
customer.printObj()
customer.QueryPrintFromDatabase()
if customer.getDocumentCustomerFromDB() is not None:
    print("ERROR~~~~~~~~~~~~~~~~~~~~~~~~getDocumentCustomerFromDB~~~~~~~~~~~~~~~~~~~~~~~~~")

customer.insertDocumentIntoDB()

if customer.getDocumentCustomerFromDB() is  None:
    print("ERROR~~~~~~~~~~~~~~~~~~~~~~~~insertDocumentIntoDB~~~~~~~~~~~~~~~~~~~~~~~~~")


if customer.updateCustomerDocument(firstname="joe") is None:
    print("ERROR~~~~~~~~~~~~~~~~~~~~~~~~updateCustomerDocument~~~~~~~~~~~~~~~~~~~~~~~~~")

if customer.getDocumentCustomerFromDB() is None:
    print("ERROR~~~~~~~~~updateCustomerDocument~~~~~~~~~~~~~~~getDocumentCustomerFromDB~~~~~~~~~~~~~~~~~~~~~~~~~")

customer.updateCustomerObj(firstname="OPTIONAL",lastname="OPTIONAL", email="OPTIONAL")

if customer.getDocumentCustomerFromDB() is not None:
    print("ERROR~~~~~~~~~~~updateCustomerObj~~~~~~~~~~~~~getDocumentCustomerFromDB~~~~~~~~~~~~~~~~~~~~~~~~~")

