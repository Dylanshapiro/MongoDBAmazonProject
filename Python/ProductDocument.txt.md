# ProductDocument

```python
from ProductDocument import ProductTable
#Create ProductTable Object
table = ProductTable()
#drops current MongoDB Table "Product" and recreates it with random data
table.createProductTable()
#print the ProductTable from Mongodb
table.printProductTable()
#drop MongoDB Table
table.dropTable()

from ProductDocument import Product
#Create Product Object all variables are optional
product = Product(_id="sd2134204do234re9", name="example",price=21333.44, stock=4,description="this is my dope discription",restock_level=100, category= food, sale_flag=False)
#prints all functions and its paramaters 
product.__describe__()
#print current Product Obj
product.printObj()
#query current Product Obj
product.QueryPrintFromDatabase()
#Create ProductDocumet in MongoDB
product.insertDocumentIntoDB()
#update Product Object
product.updateProductObj(_id="Optional",name="Optional",price="Optional", stock="Optional",description="Optional",restock_level="Optional", category="Optional", sale_flag="Optional")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Query w current object, update current object, and return current object updated
#CAUTION: if Query returns multiple Documents it doesnt update current object it just returns null
#HOW TO AVOID THIS: provide unique identifiers or _id
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
product.getDocumentProductFromDB()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#if _id is not set: calls getDocumentProductFromDB()
#CAUTION: if Query returns multiple Documents it doesnt update current object it just returns null
#HOW TO AVOID THIS: provide unique identifiers or _id
#this function will update the document in the database
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
product.updateProductDocument(name="Optional",price="Optional", stock="Optional",description="Optional",restock_level="Optional", category="Optional", sale_flag="Optional")
#delete_one(self.__dict__) mongodb method deletes first instance of query provide unique identifiers or _id for more accuracy
product.removeProductDocument()
#remove all Product Documents based on current object query dont use _id ['delete_many(self.__dict__)'] mongodb method
product.removeAllProductDocument()
```