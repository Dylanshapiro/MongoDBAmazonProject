from pymongo import MongoClient
from decimal import Decimal
from bson.objectid import ObjectId
import random
from DatabaseConfig import DataBase
from ProductDocument import ProductTable
from ProductDocument import Product

class OrderItem:
    def __init__(self, product_id=None, quantity=None):
        product =Product(_id= product_id).getDocumentProductFromDB()
        if product is not None:
            if product_id is not None:
                if type(product_id) is not ObjectId:
                    self.product_id = ObjectId(product_id)
                else :
                    self.product_id = product_id
            if quantity is not None: 
                self.quantity= quantity
            else:
                self.quantity=1
        else:
            print("item not found")

    def getOrderItemProduct(self):
        if self.product_id is not None:
            return Product(self.product_id).getDocumentProductFromDB()

    def documentToOrderItem(self,orderItem):
        return OrderItem(**orderItem)

    def printObj(self):
        print("BeginObject:~~~~~~~~~~~~~~")
        print(self.__dict__)
        print("EndObject:~~~~~~~~~~~~~~")

    def QueryPrintFromDatabase(self):
        mycol = DB.mycol
        print("BeginprintFromDatabase:~~~~~~~~~~~~~~")
        try:
            mydoc = mycol.find(self.__dict__)
        except TypeError as te:
            print("issue looking up : {0}, Error Thrown : {1} ".format(self.__dict__,te))
        for doc in mydoc:
            print(doc)
        print("EndprintFromDatabase:~~~~~~~~~~~~~~")

    def removeOrderItemDocument(self):
        mycol = DB.mycol
        mycol.delete_one( self.__dict__)


    def removeAllOrderItemDocument(self):
        mycol = DB.mycol
        mycol.delete_many(self.__dict__)  



    def updateOrderItemDocument(self,product_id=None, quantity=None):
        mycol = DB.mycol
        result= not None
        try:
            if self.product_id is not None:
                pass
        except:
            result = self.getDocumentOrderItemFromDB()
            pass
        if result == None:
            return None
        myquery = self.__dict__
        p=OrderItem(product_id=product_id, quantity=quantity)
        newvalues= p.__dict__
        mycol.find_one_and_update(myquery,{"$set":newvalues},upsert=True)
        self.updateOrderItemObj(product_id=product_id, quantity=quantity)
        return self

    def updateOrderItemObj(self, product_id=None, quantity=None):
        if product_id is not None:
            product =Product(_id= product_id).getDocumentProductFromDB()
            if product is not None:
                if type(product_id) is not ObjectId:
                    self.product_id = ObjectId(product_id)
        if quantity is not None: 
            self.quantity= quantity
        else:
            self.quantity=1

    def insertDocumentIntoDB(self):
        mycol = DB.mycol
        mycol.insert_one(self.__dict__)

    def getDocumentOrderItemFromDB(self):
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
            orderItem = docs[0]
            self.updateOrderItemObj(**orderItem)
            return self
        print("incorrect or Not Specific enough Query object :{0}".format(self.__dict__))
        return None

class OrderItemHelper:
    def createrRandomOrderItem(self):

        productTable = ProductTable()

        return OrderItem(product_id=productTable.getRandomProductId(), quantity=random.randint(0,20))

def populatetolist(self, orderItem_names, filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    # Strips the newline character 
    for OrderItemname in Lines: 
        orderItem_names.append(OrderItemname.rstrip())
    file1.close()

       
DB = DataBase("AMAZON","Order")