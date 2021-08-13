from pymongo import cursor
import pandas as pd

from LogicLayer.DataManipulation import DataManipulation


class plot_graph:
    __db = DataManipulation()

    def __parse_data(self,cursor):
        i = 0
        df = 0
        for row in cursor:
            if i == 0:
                ob = pd.DataFrame.from_dict(row)
                i += 1
            else:
                ob.insert(0, i, pd.DataFrame.from_dict(row))
                i += 1
        ob = ob.transpose()
        ob.columns = ['latt', 'long']
        return ob

    def plot_from_sqlite(self,start,end):
        dates = (start,end)
        cursor = self.__db.get_data_between_dates(dates)
        return self.__parse_data(cursor)

    def plot_from_mongo(self, start, end):
        dates = (start, end)
        cursor = self.__db.get_data_between_dates_mongo(dates)
        return self.__parse_data(cursor)
