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
order = Order(_id="sd2134204do234re9", name="example",price=21333.44, stock=4,description="this is my dope discription",restock_level=100, category= food, sale_flag=False)
#prints all functions and its paramaters 
order.__describe__()
#print current Order Obj
order.printObj()
#query current Order Obj
order.QueryPrintFromDatabase()
#Create OrderDocumet in MongoDB
order.insertDocumentIntoDB()
#update Order Object
order.updateOrderObj(_id="Optional",name="Optional",price="Optional", stock="Optional",description="Optional",restock_level="Optional", category="Optional", sale_flag="Optional")
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
order.updateOrderDocument(name="Optional",price="Optional", stock="Optional",description="Optional",restock_level="Optional", category="Optional", sale_flag="Optional")
#delete_one(self.__dict__) mongodb method deletes first instance of query provide unique identifiers or _id for more accuracy
order.removeOrderDocument()
#remove all Order Documents based on current object query dont use _id ['delete_many(self.__dict__)'] mongodb method
order.removeAllOrderDocument()
```