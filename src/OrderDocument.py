from pymongo import MongoClient
from decimal import Decimal
from bson.objectid import ObjectId
import random
from DatabaseConfig import DataBase
import datetime
from OrderItemDocument import OrderItem
from OrderItemDocument import OrderItemHelper
import datetime
import random
from CustomerDocument import CustomerTable
from CustomerDocument import Customer


def random_date(start, end):
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )


class Order:
    def __init__(self,_id=None, customer_id=None, _OrderItemDocument=False, purchasedate=None, shipdate=None,city=None, state=None, address=None, zipcode=None, orderItem=None):
        if _id is not None:
            if type(_id) is not ObjectId:
                self._id = ObjectId(_id)
            else:
                self._id = _id 
        if customer_id is not None:
            if type(customer_id) is not ObjectId:
                self.customer_id = ObjectId(customer_id)
            else:
                self.customer_id = customer_id
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
            if _OrderItemDocument == False:
                if type(orderItem) is not list:
                    if type(orderItem) is dict:
                        self.orderItems =orderItem
                    if type(orderItem) is OrderItem:
                        self.orderItems = orderItem.__dict__
                if type(orderItem) is list:
                    self.orderItems = []
                    for item in orderItem:
                        if type(item) is OrderItem:
                            self.orderItems.append(item.__dict__)
                        if type(item) is dict:
                            self.orderItems.append(item)
            else:
                print("this is not an orderItem doc implemetation")
                
        
    def printObj(self):
        print(self.__dict__)   

    def __describe__(self):
        print("__init__(self,_id=None,_OrderItemDocument=False, purchasedate=None, shipdate=None,city=None, state=None, address=None, zipcode=None, orderItem=None)")
        print("documentToOrder(self,Order)")
        print("printObj(self)")
        print("QueryPrintFromDatabase(self)")
        print("updateOrderDocument(self, purchasedate=None, shipdate=None,city=None, state=None, address=None, zipcode=None, orderItem=None)")
        print("updateOrderObj(self,_id=None, purchasedate=None, shipdate=None,city=None, state=None, address=None, zipcode=None, orderItems=None)")
        print("insertDocumentIntoDB(self)")
        print("getDocumentOrderFromDB(self)")
        print("removeOrderDocument(self)")
        print("removeAllOrderDocument(self)")
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

    def updateOrderDocument(self, customer_id=None, purchasedate=None, shipdate=None,city=None, state=None, address=None, zipcode=None, orderItem=None):
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
        newvalues= p.__dict__
        mycol.find_one_and_update(myquery,{"$set":newvalues},upsert=True)
        self.updateOrderObj(customer_id=None,purchasedate=purchasedate, shipdate=shipdate,city=city, state=state, address=address, zipcode=zipcode, orderItems=orderItem)
        return self

    def updateOrderObj(self,_id=None,customer_id=None,_OrderItemDocument=False, purchasedate=None, shipdate=None,city=None, state=None, address=None, zipcode=None, orderItems=None):
        if _id is not None:
            if type(_id) is not ObjectId:
                self._id = ObjectId(_id)
            else:
                self._id = _id 
        if customer_id is not None:
            if type(customer_id) is not ObjectId:
                self.customer_id = ObjectId(customer_id)
            else:
                self.customer_id = customer_id
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

        if orderItems is not None:
            if _OrderItemDocument == False:
                if type(orderItems) is not list:
                    if type(orderItems) is dict:
                        self.orderItems =orderItems
                    if type(orderItems) is OrderItem:
                        self.orderItems = orderItems.__dict__
                if type(orderItems) is list:
                    self.orderItems = []
                    for item in orderItems:
                        if type(item) is OrderItem:
                            self.orderItems.append(item.__dict__)
                        if type(item) is dict:
                            self.orderItems.append(item)

    def insertDocumentIntoDB(self):
        mycol = DB.mycol
        print(self.__dict__)
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
        # Strips the newline character orderItemHelper.createrRandomOrderItem()

    def dropTable(self):
        self.mycol.drop()

    def createOrderTable(self):

        self.dropTable()
        orderList=[]
        orderItemHelper = OrderItemHelper()
        numbers = [0,1,2,3,4,5,6,7,8,9]

        citys = ["manalapan", "freehold", "howell", "cherry hill", "moorestown"]

        states = ["NJ", "NY", "PA", "TX", "FL"]

        streets = ["Cornel", "gordans corner", "Rowan Blvd ", "precedent place", "cherry road", "cuba way"]

        orderitemlistrandom =[]
        for y in range (20):
            x =random.choice(numbers)
            for x in range (9):
                orderitemlistrandom.append(orderItemHelper.createrRandomOrderItem())
            orderList.append(Order(customer_id=CustomerTable().createRandomCustomer()._id,_OrderItemDocument=False,orderItem=orderitemlistrandom,purchasedate=datetime.datetime.now().isoformat(),city=random.choice(citys),state=random.choice(states), address="{0} {1}".format(random.randint(10, 100),random.choice(streets)), zipcode=random.randint(10, 100)))
            orderitemlistrandom =[]

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
