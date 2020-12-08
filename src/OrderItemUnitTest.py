from OrderItemDocument import OrderItemHelper
from ProductDocument import ProductTable
from ProductDocument import Product
from OrderDocument import Order
from OrderItemDocument import OrderItem

helper = OrderItemHelper()
orderitem =helper.createrRandomOrderItem()
addorder = Order(orderItem=orderitem)
addorder.QueryPrintFromDatabase()
addorder.insertDocumentIntoDB()
addorder.QueryPrintFromDatabase()


orderitem.QueryPrintFromDatabase()