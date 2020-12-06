from pymongo import MongoClient
from decimal import Decimal
from bson.objectid import ObjectId
import random
from DatabaseConfig import DataBase

class Order:
    def __init__(self,_id=None, purchasedate=None, shipdate=None,city=None, state=None, address=None, zipcode=None, orderItem=None):
        if _id is not None:
            if type(_id) is not ObjectId:
                self._id = ObjectId(_id)
            else:
                self._id = _id 
        if purchasedate is not None:
            self.purchasedate = purchasedate 
        if shipdate is not None:
            self.shipdate = shipdate 
        if city is not None:
            self.city = city 
        if state is not None:
            self.state = state
        if address is not None:
            self.address = address
        if zipcode is not None:
            self.zipcode= zipcode
        if orderItem is not None:
            self.orderItems = []
            if type(orderItem) is not list:
                if type(orderItem) is dict:
                    self.orderItems.append(OrderItem(**orderItem))
                if type(orderItem) is OrderItem:
                    self.orderItems.append(orderItem)
            if type(orderItem) is list:
                for item in orderItem:
                    if type(item) is Item:
                        self.orderItems.append(item)
                    if type(item) is dict:
                        self.item.append(orderItwDem(**item))
                
        
        

    def __describe__(self):
        print("__init__(self,_id=None, purchasedate=None, shipdate=None,city=None, state=None, address=None, zipcode=None, orderItem=None)")
        print("documentToOrder(self,Order)")
        print("printObj(self)")
        print("QueryPrintFromDatabase(self)")
        print("updateOrderDocument(self, purchasedate=None, shipdate=None,city=None, state=None, address=None, zipcode=None, orderItem=None)")
        print("updateOrderObj(self,_id=None, purchasedate=None, shipdate=None,city=None, state=None, address=None, zipcode=None, orderItem=None)")
        print("insertDocumentIntoDB(self)")
        print("getDocumentOrderFromDB(self)")
        print("removeOrderDocument(self)")
        print("removeAllOrderDocument(self)")

    def documentToOrder(self,Order):
        return Order(**Order)

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

    def removeOrderDocument(self):
        mycol = DB.mycol
        mycol.delete_one( self.__dict__)


    def removeAllOrderDocument(self):
        mycol = DB.mycol
        mycol.delete_many(self.__dict__)  


    def __dict__(self):
        wD

    def updateOrderDocument(self, purchasedate=None, shipdate=None,city=None, state=None, address=None, zipcode=None, orderItem=None):
        mycol = DB.mycol
        result=not None
        try:
            if self._id is not None:
                pass
        except:
            result = self.getDocumentOrderFromDB()
            pass
        if result == None:
            return None
        myquery = self.__dict__
        p=Order(_id=None,purchasedate=purchasedate, shipdate=shipdate,city=city, state=state, address=address, zipcode=zipcode, orderItem=orderItem)
        newvalues= p.__dict__()
        mycol.find_one_and_update(myquery,{"$set":newvalues},upsert=True)
        self.updateOrderObj(purchasedate=purchasedate, shipdate=shipdate,city=city, state=state, address=address, zipcode=zipcode, orderItem=orderItem)
        return self

    def updateOrderObj(self,_id=None, purchasedate=None, shipdate=None,city=None, state=None, address=None, zipcode=None, orderItem=None):
        if _id is not None:
            if type(_id) is not ObjectId:
                self._id = ObjectId(_id)
            else:
                self._id = _id 
        if purchasedate is not None:
            self.purchasedate = purchasedate 
        if shipdate is not None:
            self.shipdate = shipdate 
        if city is not None:
            self.city = city 
        if state is not None:
            self.state = state
        if address is not None:
            self.address = address
        if zipcode is not None:
            self.zipcode= zipcode

    def insertDocumentIntoDB(self):
        mycol = DB.mycol
        mycol.insert_one(self.__dict__)

    def getDocumentOrderFromDB(self):
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
            order = docs[0]
            self.updateOrderObj(**order)
            return self
        print("incorrect or Not Specific enough Query object :{0}".format(self.__dict__))
        return None

class OrderTable():

    def __init__(self):
        self.mycol = DB.mycol
    
    def printOrderTable(self):     
        for Order in self.mycol.find(): 
            print(Order)

    def populatetolist(self, order_names, filename):
        file1 = open(filename, 'r')
        Lines = file1.readlines()
        # Strips the newline character 
        for Ordername in Lines: 
            order_names.append(Ordername.rstrip())
        file1.close()


    def dropTable(self):
        self.mycol.drop()

    def createOrderTable(self):
        firstnames = []
        self.populatetolist(firstnames, "data/firstNames.txt")
        lastnames = []
        self.populatetolist(lastnames,"data/lastNames.txt")
        emailproviders = []
        self.populatetolist(emailproviders, "data/emailProviders.txt")

        self.dropTable()
        orderList=[]
        for x in range(20):
            orderList.append(Order(firstname=random.choice(firstnames),lastname=random.choice(lastnames)  , email=""+str(random.randint(100,999))+"@"+random.choice(emailproviders)))
    
        
        for order in orderList:
            #order.printObj()
            order.insertDocumentIntoDB()

def populatetolist(self, order_names, filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    # Strips the newline character 
    for Ordername in Lines: 
        order_names.append(Ordername.rstrip())
    file1.close()

DB = DataBase("AMAZON","Order")
