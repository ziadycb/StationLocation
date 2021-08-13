import datetime
import threading
import urllib.request, json

from LogicLayer.DataManipulation import DataManipulation


class LoactionParser:
    # create loc_parser as static method
    @staticmethod
    def loc_parser():
        threading.Timer(300.0, LoactionParser.loc_parser).start()

        data_manager = DataManipulation()

        with urllib.request.urlopen("http://api.open-notify.org/iss-now.json") as url:
            data = json.loads(url.read().decode())


        date = datetime.datetime.fromtimestamp(data["timestamp"])
        long = data["iss_position"]["longitude"]
        latt = data["iss_position"]["latitude"]
        station_data = (latt, long, date)
        data_manager.insert(station_data)
        data_manager.insert_mongo(station_data)
