import matplotlib

import numpy as np
import matplotlib.pyplot as plt

import datetime
from floodsystem.analysis import polyfit

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2F"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    #get the 5 stations with highest water level
    highest = stations_highest_rel_level(stations, 5)
    print(highest)
    highest_Sta = []
    p = 3
    for highest_sta in highest:
        highest_Sta.append(highest_sta[0])
    #iterate through the highest stations to get the dates and water levels
    for station in highest_Sta:
        dates, levels = fetch_measure_levels(
                station.measure_id, dt=datetime.timedelta(days=2))
        polyfit(dates, levels, p)
        
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()