from pymongo import MongoClient
from decimal import Decimal
from bson.objectid import ObjectId
import random

from DatabaseConfig import DataBase

class Product:

    def __init__(self,_id=None, name=None,price=None, stock=None,description=None,restock_level=None, category=None, sale_flag=None):
        if _id is not None:
            if type(_id) is not ObjectId:
                self._id = ObjectId(_id)
            else:
                self._id = _id 
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if stock is not None: 
            self.stock = stock
        if description is not None:
            self.description = description
        if restock_level is not None:
            self.restock_level = restock_level
        if category is not None:
            self.category =category
        if sale_flag is not None:
            self.sale_flag = sale_flag

    def __describe__(self):
        print("__init__(self,_id=None, name=None,price=None, stock=None,description=None,restock_level=None, category=None, sale_flag=None)")
        print("documentToProduct(self,product)")
        print("printObj(self)")
        print("QueryPrintFromDatabase(self)")
        print("updateProductObj(self,_id=None,name=None,price=None, stock=None,description=None,restock_level=None, category=None, sale_flag=None)")
        print("updateProductDocument(self,name=None,price=None, stock=None,description=None,restock_level=None, category=None, sale_flag=None)")
        print("insertDocumentIntoDB(self)")
        print("getDocumentProductFromDB(self)")

    def documentToProduct(self,product):
        return Product(_id=product['_id'],name=product['name'],price=product['price'], stock=product['stock'],description=product['description'],restock_level=product['restock_level'], category= product['category'], sale_flag=product['sale_flag'])

    def printObj(self):
        print("BeginObject:~~~~~~~~~~~~~~")
        print(self.__dict__)
        print("EndObject:~~~~~~~~~~~~~~")

    def QueryPrintFromDatabase(self):
        print("BeginprintFromDatabase:~~~~~~~~~~~~~~")
        mycol = DB.mycol
        try:
            mydoc = mycol.find(self.__dict__)
        except TypeError as te:
            print("issue looking up : {0}, Error Thrown : {1} ".format(self.__dict__,te))
        for doc in mydoc:
            print(doc)
        print("EndprintFromDatabase:~~~~~~~~~~~~~~")

    def updateProductDocument(self,name=None,price=None, stock=None,description=None,restock_level=None, category=None, sale_flag=None):
        mycol = DB.mycol
        result=not None
        try:
            if self._id is not None:
                pass
        except:
            result = self.getDocumentProductFromDB()
            pass

        if result == None:
            return None
        myquery = self.__dict__
        p=Product(_id=None,name=name,price=price, stock=stock,description=description,restock_level=restock_level, category=category, sale_flag=sale_flag)
        newvalues= p.__dict__
        mycol.find_one_and_update(myquery,{"$set":newvalues},upsert=True)
        self.updateProductObj(name=name,price=price, stock=stock,description=description,restock_level=restock_level, category=category, sale_flag=sale_flag)
        return self

    def updateProductObj(self,_id=None,name=None,price=None, stock=None,description=None,restock_level=None, category=None, sale_flag=None):
        if _id is not None:
            self._id= _id
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if stock is not None: 
            self.stock = stock
        if description is not None:
            self.description = description
        if restock_level is not None:
            self.restock_level = restock_level
        if category is not None:
            self.category =category
        if sale_flag is not None:
            self.sale_flag = sale_flag

    def insertDocumentIntoDB(self):
        mycol = DB.mycol
        mycol.insert_one(self.__dict__)

    def removeCustomerDocument(self):
        mycol = DB.mycol
        mycol.delete_one( self.__dict__)
    def removeAllCustomerDocument(self):
        mycol = DB.mycol
        mycol.delete_many(self.__dict__)  

    def getDocumentProductFromDB(self):
        mycol = DB.mycol
        myfields = self.__dict__
        try:
            mydoc = mycol.find(myfields)
        except TypeError as te:
            print("issue looking up : {0}, Error Thrown : {1} ".format(self.__dict__,te))
        count =0
        docs =[]

        for doc in mydoc:
            count +=1
            docs.append(doc)
        if count ==1:
            product = docs[0]
            self.updateProductObj(**product)
            return self
        print("incorrect or Not Specific enough Query object :{0}".format(self.__dict__))
        return None

class ProductTable():

    def __init__(self):
        self.mycol = DB.mycol
    
    def printProductTable(self):     
        for product in self.mycol.find(): 
            print(product)

    def dropTable(self):
        self.mycol.drop()

    def createProductTable(self):
        names = []
        populatetolist(names,'data/productNames.txt')

        descriptions = ['generic description 1', 'generic description 2']

        categorys = []
        populatetolist(categorys,'data/productCategorys.txt')
        productList = []
        createProductList(productList,names,descriptions,categorys)

        self.mycol.drop()

        for product in productList:
            product.insertDocumentIntoDB()

def populatetolist(names, filename):
        file1 = open(filename, 'r')
        Lines = file1.readlines()
        # Strips the newline character 
        for productname in Lines: 
            names.append(productname.rstrip())
        file1.close()

def createProductList(productList,names,descriptions,categorys):
    for product in names:
        productList.append(Product(name=product,price=float(format(random.uniform(0.1,1000.0),'.2f')),stock=random.randint(0,1000),description=random.choice(descriptions), restock_level=random.randint(0,10),category=random.choice(categorys), sale_flag= True if random.randint(0,1)==1 else False))


DB = DataBase("AMAZON","Product")