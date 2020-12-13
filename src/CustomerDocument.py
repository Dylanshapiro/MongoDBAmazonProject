from pymongo import MongoClient
from decimal import Decimal
from bson.objectid import ObjectId
import random
from DatabaseConfig import DataBase

class Customer:
    def __init__(self,_id=None, firstname=None,lastname=None, email=None):
        if _id is not None:
            if type(_id) is not ObjectId:
                self._id = ObjectId(_id)
            else:
                self._id = _id 
        if firstname is not None:
            self.firstname = firstname 
        if lastname is not None:
            self.lastname = lastname 
        if email is not None:
            self.email = email 

    def __describe__(self):
        print("__init__(self,_id=None, firstname=None,lastname=None, email=None)")
        print("documentToCustomer(self,Customer)")
        print("printObj(self)")
        print("QueryPrintFromDatabase(self)")
        print("updateCustomerDocument(self,firstname=None,lastname=None, email=None)")
        print("updateCustomerObj(self,firstname=None,lastname=None, email=None)")
        print("insertDocumentIntoDB(self)")
        print("getDocumentCustomerFromDB(self)")
        print("removeCustomerDocument(self)")
        print("removeAllCustomerDocument(self)")

    def documentToCustomer(self,Customer):
        return Customer(**Customer)

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

    def removeCustomerDocument(self):
        mycol = DB.mycol
        mycol.delete_one( self.__dict__)


    def removeAllCustomerDocument(self):
        mycol = DB.mycol
        mycol.delete_many(self.__dict__)  


    def updateCustomerDocument(self,firstname=None,lastname=None, email=None):
        mycol = DB.mycol
        result=not None
        try:
            if self._id is not None:
                pass
        except:
            result = self.getDocumentCustomerFromDB()
            pass
        if result == None:
            return None
        myquery = self.__dict__
        p=Customer(_id=None,firstname=firstname,lastname=lastname, email=email)
        newvalues= p.__dict__
        mycol.find_one_and_update(myquery,{"$set":newvalues},upsert=True)
        self.updateCustomerObj(firstname=firstname,lastname=lastname, email=email)
        return self

    def updateCustomerObj(self,_id=None,firstname=None,lastname=None, email=None):
        if _id is not None:
            if type(_id) is not ObjectId:
                self._id = ObjectId(_id)
            else:
                self._id = _id 
        if firstname is not None:
            self.firstname = firstname 
        if lastname is not None:
            self.lastname = lastname 
        if email is not None:
            self.email = email 

    def insertDocumentIntoDB(self):
        mycol = DB.mycol
        print(self.__dict__)
        mycol.insert_one(self.__dict__)

    def getDocumentCustomerFromDB(self):
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
            customer = docs[0]
            self.updateCustomerObj(**customer)
            return self
        print("incorrect or Not Specific enough Query object :{0}".format(self.__dict__))
        return None

class CustomerTable():

    def __init__(self):
        self.mycol = DB.mycol
    
    def printCustomerTable(self):     
        for Customer in self.mycol.find(): 
            print(Customer)

    def populatetolist(self, customer_names, filename):
        file1 = open(filename, 'r')
        Lines = file1.readlines()
        # Strips the newline character 
        for Customername in Lines: 
            customer_names.append(Customername.rstrip())
        file1.close()


    def createRandomCustomer(self):
        firstnames = []
        self.populatetolist(firstnames, "firstNames.txt")
        lastnames = []
        self.populatetolist(lastnames,"lastNames.txt")
        emailproviders = []
        self.populatetolist(emailproviders, "emailProviders.txt")
        customer = Customer(firstname=random.choice(firstnames),lastname=random.choice(lastnames)  , email=""+str(random.randint(100,999))+"@"+random.choice(emailproviders))
        customer.insertDocumentIntoDB()
        return customer.getDocumentCustomerFromDB()

    def dropTable(self):
        self.mycol.drop()

    def createCustomerTable(self):
        firstnames = []
        self.populatetolist(firstnames, "firstNames.txt")
        lastnames = []
        self.populatetolist(lastnames,"lastNames.txt")
        emailproviders = []
        self.populatetolist(emailproviders, "emailProviders.txt")

        self.dropTable()
        customerList=[]
        for x in range(20):
            customerList.append(Customer(firstname=random.choice(firstnames),lastname=random.choice(lastnames)  , email=""+str(random.randint(100,999))+"@"+random.choice(emailproviders)))
    
        
        for customer in customerList:
            #customer.printObj()
            customer.insertDocumentIntoDB()

def populatetolist(self, customer_names, filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    # Strips the newline character 
    for Customername in Lines: 
        customer_names.append(Customername.rstrip())
    file1.close()

DB = DataBase("AMAZON","Customer")
