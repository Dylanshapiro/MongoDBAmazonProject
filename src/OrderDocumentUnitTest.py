from OrderDocument import OrderTable
from OrderDocument import Order
from OrderItemDocument import OrderItem
from OrderItemDocument import OrderItemHelper
oTable = OrderTable()
oTable.createOrderTable()
oTable.printOrderTable()
helper = OrderItemHelper()

randomorderitem = helper.createrRandomOrderItem()
order = Order(address="example", city="example", purchasedate="example", shipdate="example", state="example", zipcode="example", orderItem=randomorderitem)
order.__describe__()
order.printObj()
order.QueryPrintFromDatabase()
if order.getDocumentOrderFromDB() is not None:
    print("ERROR~~~~~~~~~~~~~~~~~~~~~~~~getDocumentOrderFromDB~~~~~~~~~~~~~~~~~~~~~~~~~")
order.insertDocumentIntoDB()

if order.getDocumentOrderFromDB() is  None:
    print("ERROR~~~~~~~~~~~~~~~~~~~~~~~~insertDocumentIntoDB~~~~~~~~~~~~~~~~~~~~~~~~~")


if order.updateOrderDocument(address="JUst updated this") is None:
    print("ERROR~~~~~~~~~~~~~~~~~~~~~~~~updateOrderDocument~~~~~~~~~~~~~~~~~~~~~~~~~")

if order.getDocumentOrderFromDB() is None:
    print("ERROR~~~~~~~~~updateOrderDocument~~~~~~~~~~~~~~~getDocumentOrderFromDB~~~~~~~~~~~~~~~~~~~~~~~~~")

randomorderitem = helper.createrRandomOrderItem()

order.updateOrderObj(address="example", city="example", purchasedate="example", shipdate="example", state="example", zipcode="example", orderItems=randomorderitem)

if order.getDocumentOrderFromDB() is not None:
    print("ERROR~~~~~~~~~~~updateOrderObj~~~~~~~~~~~~~getDocumentOrderFromDB~~~~~~~~~~~~~~~~~~~~~~~~~")




#orderToRemove= Order(_id="5fced67a49d6ed4dcb4fa9e0")
#print (orderToRemove.__dict__)
#orderToRemove.QueryPrintFromDatabase()
#print (orderToRemove.__dict__)
#orderToRemove.getDocumentOrderFromDB()
#print (orderToRemove.__dict__)