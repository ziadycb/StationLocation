from DataAccessLayer.ConnectionFactory import ConnectionFactory


class MongoManagement:
    myclient = None
    mydb = None

    def __init__(self, connectionname):
        self.myclient = ConnectionFactory.create_connection(connectionname)
        self.mydb = self.myclient["ISSLoc"]

    def insert(self, station_data):
        mycol = self.mydb["ISSLoc"]

        mydict = {
            "long": station_data[0],
            "latt": station_data[1],
            "date": station_data[2]
        }

        mycol.insert_one(mydict)

    def get_data_between_dates(self, dates):
         cursor = self.mydb['ISSLoc'].find({'date': {'$gte': dates[0], '$lt': dates[1]}})
         return cursor