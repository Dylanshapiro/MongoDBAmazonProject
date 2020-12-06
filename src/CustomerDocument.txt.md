# CustomerDocument

```python
from CustomerDocument import CustomerTable
#Create CustomerTable Object
table = CustomerTable()
#drops current MongoDB Table "Customer" and recreates it with random data
table.createCustomerTable()
#print the CustomerTable from Mongodb
table.printCustomerTable()
#drop MongoDB Table
table.dropTable()

from CustomerDocument import Customer
#Create Customer Object
customer = Customer(firstname="example",lastname="example", email="example@gmail.com")
#prints all functions and its paramaters 
customer.__describe__()
#print current Customer Obj
customer.printObj()
#query current Customer Obj
customer.QueryPrintFromDatabase()
#Create CustomerDocumet in MongoDB
customer.insertDocumentIntoDB()
#update Customer Object
customer.updateCustomerObj(_id="OPTIONAL",firstname="OPTIONAL",lastname="OPTIONAL", email="OPTIONAL")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Query w current object, update current object, and return current object updated
#CAUTION: if Query returns multiple Documents it doesnt update current object it just returns null
#HOW TO AVOID THIS: provide unique identifiers or _id
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
customer.getDocumentCustomerFromDB()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#if _id is not set: calls getDocumentCustomerFromDB()
#CAUTION: if Query returns multiple Documents it doesnt update current object it just returns null
#HOW TO AVOID THIS: provide unique identifiers or _id
#this function will update the document in the database
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
customer.updateCustomerDocument(firstname="OPTIONAL",lastname="OPTIONAL", email="OPTIONAL")
#delete_one(self.__dict__) mongodb method deletes first instance of query provide unique identifiers or _id for more accuracy
customer.removeCustomerDocument()
#remove all Customer Documents based on current object query dont use _id ['delete_many(self.__dict__)'] mongodb method
customer.removeAllCustomerDocument()
```