# MongoDBAmazonProject



## Table of contents
* [MongoDB Statements](#MongoDB-Statements)
* [Python Data Access Objects](#Python-Data-Access-Objects)





## MongoDB Statements
### Install pymongo 
```bash
pip install pymongo
```
### Connect to the Mongo Client
```python
from pymongo import MongoClient
client = MongoClient('ip')
mydb = client['database']
mycol =mydb['ColumnName']
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
### Query, Add, Remove, and Modify Order Information
```python
mycol.find({'customer_id': ObjectId('5fd568e18f232403dfc2f127'), 'purchasedate': '2020-12-12T20:05:37.315430', 'city': 'freehold', 'state': 'FL', 'address': '94 cuba way', 'zipcode': 82, 'orderItems': [{'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 18}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf7'), 'quantity': 19}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 8}, {'product_id': ObjectId('5fd568d9b25a47377d8edd04'), 'quantity': 10}, {'product_id': ObjectId('5fd568d9b25a47377d8edcfe'), 'quantity': 7}, {'product_id': ObjectId('5fd568d9b25a47377d8edcff'), 'quantity': 8}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 15}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 19}, {'product_id': ObjectId('5fd568d9b25a47377d8edcff'), 'quantity': 13}]})

mycol.insert_one({'customer_id': ObjectId('5fd568e18f232403dfc2f127'), 'purchasedate': '2020-12-12T20:05:37.315430', 'city': 'freehold', 'state': 'FL', 'address': '94 cuba way', 'zipcode': 82, 'orderItems': [{'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 18}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf7'), 'quantity': 19}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 8}, {'product_id': ObjectId('5fd568d9b25a47377d8edd04'), 'quantity': 10}, {'product_id': ObjectId('5fd568d9b25a47377d8edcfe'), 'quantity': 7}, {'product_id': ObjectId('5fd568d9b25a47377d8edcff'), 'quantity': 8}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 15}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 19}, {'product_id': ObjectId('5fd568d9b25a47377d8edcff'), 'quantity': 13}]})

mycol.delete_one({'customer_id': ObjectId('5fd568e18f232403dfc2f127'), 'purchasedate': '2020-12-12T20:05:37.315430', 'city': 'freehold', 'state': 'FL', 'address': '94 cuba way', 'zipcode': 82, 'orderItems': [{'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 18}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf7'), 'quantity': 19}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 8}, {'product_id': ObjectId('5fd568d9b25a47377d8edd04'), 'quantity': 10}, {'product_id': ObjectId('5fd568d9b25a47377d8edcfe'), 'quantity': 7}, {'product_id': ObjectId('5fd568d9b25a47377d8edcff'), 'quantity': 8}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 15}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 19}, {'product_id': ObjectId('5fd568d9b25a47377d8edcff'), 'quantity': 13}]})

mycol.find_one_and_update({'customer_id': ObjectId('5fd568e18f232403dfc2f127'), 'purchasedate': '2020-12-12T20:05:37.315430', 'city': 'freehold', 'state': 'NJ', 'address': '94 cuba way', 'zipcode': 82, 'orderItems': [{'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 18}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf7'), 'quantity': 19}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 8}, {'product_id': ObjectId('5fd568d9b25a47377d8edd04'), 'quantity': 10}, {'product_id': ObjectId('5fd568d9b25a47377d8edcfe'), 'quantity': 7}, {'product_id': ObjectId('5fd568d9b25a47377d8edcff'), 'quantity': 8}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 15}, {'product_id': ObjectId('5fd568d9b25a47377d8edcf9'), 'quantity': 19}, {'product_id': ObjectId('5fd568d9b25a47377d8edcff'), 'quantity': 13}]})
```

## Python Data Access Objects
### Customer Document
[CusomerDocumentReadMe](https://github.com/Dylanshapiro/MongoDBAmazonProject/blob/master/src/CustomerDocument.txt.md)                                                             
### Order Document
[OrderDocumentReadMe](https://github.com/Dylanshapiro/MongoDBAmazonProject/blob/master/src/OrderDocument.txt.md)                                                                  
### Product Document
[ProductDocumentReadMe](https://github.com/Dylanshapiro/MongoDBAmazonProject/blob/master/src/ProductDocument.txt.md)                                                                    
