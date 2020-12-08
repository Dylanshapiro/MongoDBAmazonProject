import os
import datetime
from pymongo import MongoClient
class  DataBase: 
    def __init__(self,database,table):
        os.system('./startServer.sh')
        client = MongoClient('mongodb://###################')
        mydb = client[database]
        self.mycol =mydb[table]

    
def readTextFileConfig():
        file1 = open('data/databaseConfig.private', 'r')
        Lines = file1.readlines()
        # Strips the newline character
        lines=[] 
        for l in Lines: 
            lines.append(l.rstrip())
        file1.close()
        return lines[0]
