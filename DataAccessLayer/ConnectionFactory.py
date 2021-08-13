import pymongo
import sqlite3

class ConnectionFactory:

    # create create_connection static method
    @staticmethod
    def create_connection(connectionname):
        conn = None
        if connectionname == "mongo":
            conn = pymongo.MongoClient("mongodb://loca lhost:27017/")
        elif connectionname == "sql":
            conn = sqlite3.connect(r"D:\sqlite\db\pythonsqlite.db", check_same_thread=False)
        elif connectionname == "sqlserver":
            print("Not done yet")

        return conn
