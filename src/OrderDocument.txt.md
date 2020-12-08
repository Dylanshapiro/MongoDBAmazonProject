# OrderDocument

```python
from OrderDocument import OrderTable
#Create OrderTable Object
table = OrderTable()
#drops current MongoDB Table "Order" and recreates it with random data
table.createOrderTable()
#print the OrderTable from Mongodb
table.printOrderTable()
#drop MongoDB Table
table.dropTable()

from OrderDocument import Order
#Create Order Object all variables are optional
order = Order(_id="3241d2543f3245", customer_id="243234fcidr2", _OrderItemDocument=False, purchasedate=10/22/2020, shipdate=None,city="freehold", state="NJ", address=6 drive ave, zipcode=0784834, orderItem=OrderItem(product_id="exampleid",quantity=3))
#prints all functions and its paramaters 
order.__describe__()
#print current Order Obj
order.printObj()
#query current Order Obj
order.QueryPrintFromDatabase()
#Create OrderDocumet in MongoDB
order.insertDocumentIntoDB()
#update Order Object
order.updateOrderObj(_id="OPTIONAL", customer_id="OPTIONAL", _OrderItemDocument=OPTIONAL, purchasedate=OPTIONAL, shipdate=OPTIONAL,city="OPTIONAL", state="OPTIONAL", address=OPTIONAL, zipcode=OPTIONAL, orderItem=OrderItem(product_id="exampleid",quantity=3))
order.updateOrderObj(_id="OPTIONAL", customer_id="OPTIONAL", _OrderItemDocument=OPTIONAL, purchasedate=OPTIONAL, shipdate=OPTIONAL,city="OPTIONAL", state="OPTIONAL", address=OPTIONAL, zipcode=OPTIONAL, orderItem=[OrderItem(product_id="exampleid",quantity=3),OrderItem(product_id="exampleid",quantity=3)])
order.updateOrderObj(_id="OPTIONAL", customer_id="OPTIONAL", _OrderItemDocument=OPTIONAL, purchasedate=OPTIONAL, shipdate=OPTIONAL,city="OPTIONAL", state="OPTIONAL", address=OPTIONAL, zipcode=OPTIONAL, orderItem=OrderItem(product_id="exampleid",quantity=3))
order.updateOrderObj(_id="OPTIONAL", customer_id="OPTIONAL", _OrderItemDocument=OPTIONAL, purchasedate=OPTIONAL, shipdate=OPTIONAL,city="OPTIONAL", state="OPTIONAL", address=OPTIONAL, zipcode=OPTIONAL)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Query w current object, update current object, and return current object updated
#CAUTION: if Query returns multiple Documents it doesnt update current object it just returns null
#HOW TO AVOID THIS: provide unique identifiers or _id
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
order.getDocumentOrderFromDB()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#if _id is not set: calls getDocumentOrderFromDB()
#CAUTION: if Query returns multiple Documents it doesnt update current object it just returns null
#HOW TO AVOID THIS: provide unique identifiers or _id
#this function will update the document in the database
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
order.updateOrderDocument(customer_id="Optional",purchasedate="Optional", shipdate="Optional",city="Optional",state="Optional", address="Optional", zipcode="Optional", orderItem=OrderItem(product_id="NOTOptional",quantity=Optional))
#delete_one(self.__dict__) mongodb method deletes first instance of query provide unique identifiers or _id for more accuracy
order.removeOrderDocument()
#remove all Order Documents based on current object query dont use _id ['delete_many(self.__dict__)'] mongodb method
order.removeAllOrderDocument()
```
