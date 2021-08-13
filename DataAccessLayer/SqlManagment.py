from DataAccessLayer.ConnectionFactory import ConnectionFactory


class SqlManagement:
    conn = None
    cursor = None
    def __init__(self, connectionname):
        self.conn = ConnectionFactory.create_connection(connectionname)
        self.cursor = self.conn.cursor()

    def insert(self, station_data):
        sql = ''' INSERT INTO ISSLocation(latitude,longitude,date)
                      VALUES(?,?,?) '''
        self.cursor.execute(sql, station_data)
        self.conn.commit()

    def get_data_between_dates(self,dates):
        sql = '''SELECT latitude,longitude FROM ISSLocation where date BETWEEN ? AND ? '''
        self.cursor.execute(sql, dates)

        return self.cursor
