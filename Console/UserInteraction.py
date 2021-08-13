from datetime import datetime
import threading
import plotly.express as px

from LogicLayer.LoactionParser import LoactionParser
from LogicLayer.PlotGraph import plot_graph

if __name__ == '__main__':
    database_list = ["sql", "mongo"]
    t1 = threading.Thread(target=LoactionParser.loc_parser())

    date_entry = input('Enter start day in YYYY-MM-DD hh:mm:ss format: ')
    start = datetime.strptime(date_entry, '%Y-%m-%d %H:%M:%S')

    date_entry = input('Enter end day in YYYY-MM-DD hh:mm:ss format: ')
    end = datetime.strptime(date_entry, '%Y-%m-%d %H:%M:%S')

    date_entry = input('Type "Mongo" for mongoDB and "SQL" for sqlite: ')

    plot = plot_graph()
    if date_entry.lower() in database_list:
        data = plot.plot_from_sqlite(start, end)
        fig = px.scatter_geo(data, lat="latt", lon="long")
        fig.write_html('first_figure.html', auto_open=True)

