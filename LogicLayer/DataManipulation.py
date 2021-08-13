from DataAccessLayer.MongoManagment import MongoManagement
from DataAccessLayer.SqlManagment import SqlManagement


class DataManipulation:
    __sqldb = SqlManagement("sql")
    __mongodb = MongoManagement("mongo")

    def insert(self, station_data):
        self.__sqldb.insert(station_data)

    def get_data_between_dates(self,dates):
        return self.__sqldb.get_data_between_dates(dates)

    def insert_mongo(self,station_data):
        self.__mongodb.insert(station_data)

    def get_data_between_dates_mongo(self,dates):
        return self.__mongodb.get_data_between_dates(dates)