# MongoDBAmazonProject

## MongoDB Statements
### Install pymongo 
```bash
pip install pymongo
```
### Connect to the Mongo Client
```python
from pymongo import MongoClient
client = MongoClient('ip')
mydb = client[database]
mycol =mydb[ColumnName]
```
### Query, Add, Remove, and Modify Customer Information
```python
Mydoc =mycol.find({'firstname': 'Olivia', 'lastname': 'Brown', 'email': '526@aol.com'})
mycol.insert_one({'firstname': 'Olivia', 'lastname': 'Brown', 'email': '526@aol.com'})
mycol.delete_one({'firstname': 'Olivia', 'lastname': 'Brown', 'email': '526@aol.com'})
mycol.find_one_and_update({'firstname': 'Olivia', 'lastname': 'Brown', 'email': '526@aol.com'},{“$set”:{‘firstname’:’john’},upsert=True)
```
### Query, Add, Remove, and Modify Product Information
```python
mycol.find({'name': 'paper', 'price': 591.87, 'stock': 42, 'description': 'generic description 1', 'restock_level': 3, 'category': 'food', 'sale_flag': True})
mycol.insert_one({'name': 'paper', 'price': 591.87, 'stock': 42, 'description': 'generic description 1', 'restock_level': 3, 'category': 'food', 'sale_flag': True})
mycol.delete_one({'name': 'paper', 'price': 591.87, 'stock': 42, 'description': 'generic description 1', 'restock_level': 3, 'category': 'food', 'sale_flag': True})
mycol.find_one_and_update({'name': 'paper', 'price': 591.87, 'stock': 30, 'description': 'generic description 1', 'restock_level': 3, 'category': 'food', 'sale_flag': True})
```
### Query Products by Category
```python
mycol.find({'category': 'food'})
```
### Query, Add, Remove, and Modify Supplier Information
```python

```

### Query Products Whose Inventory Has Fallen Below the Minimum Stock Level
```python
mycol.find({ "$where": 'this.stock < this.restock_level' } )
```
## Python Data Access Objects
### Customer Document
[CusomerDocumentReadMe](https://github.com/Dylanshapiro/MongoDBAmazonProject/blob/master/src/CustomerDocument.txt.md)                                                             
### Order Document
[OrderDocumentReadMe](https://github.com/Dylanshapiro/MongoDBAmazonProject/blob/master/src/OrderDocument.txt.md)                                                                  
### Product Document
[ProductDocumentReadMe](https://github.com/Dylanshapiro/MongoDBAmazonProject/blob/master/src/ProductDocument.txt.md)                                                                    
