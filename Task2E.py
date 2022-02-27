from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib.pyplot as plt
from datetime import date, timedelta
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
import matplotlib.dates as mpdates

def run():
    """Requirements for Task 2E"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    #get the 5 stations with highest water level
    highest = stations_highest_rel_level(stations, 5)
    print(highest)
    highest_Sta = []
    for highest_sta in highest:
        highest_Sta.append(highest_sta[0])
    print(highest_Sta)
    
    #get the corresponding dates and water levels of stations
    for station in highest_Sta:
        print(type(station))
        dates, levels = fetch_measure_levels(
        station.measure_id, dt=timedelta(days=10))

        #plot the typical range of stations
        low, high = station.typical_range
        a = [low] * len(dates)
        b = [high] * len(dates)
        plt.plot(dates, a)
        plt.plot(dates, b)
        plot_water_levels(station, dates, levels)
        

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()



    


