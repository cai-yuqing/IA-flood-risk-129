#from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib.pyplot as plt
import matplotlib.dates as mpdates
from datetime import date, timedelta
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels

def run():
    """Requirements for Task 2E"""

    # Build list of stations
    stations = build_station_list()

     # Update latest level data for all stations
    update_water_levels(stations)

    #low, high = station.typical_range
    #plt.axhline(y = low, color = 'r', linestyle = '-')
    # plt.axhline(y = low, color = 'b', linestyle = '-')

    #get the 5 stations with highest water level
    highest = stations_highest_rel_level(stations, 5)
    print(highest)
    highest_Sta = []
    for highest_sta in highest:
        highest_Sta.append(highest_sta[0])
    print(highest_Sta)
    #print(highest[0])
    # print(type(station))

    # t = []
    # for i in range(11):
    #     t.append(date.today() - timedelta(i))

    #list of stations from near to far
    for station in highest_Sta:
        print(type(station))
        

        dates, levels = fetch_measure_levels(
        station.measure_id, dt=timedelta(days=10))
        #print(station[0].name)
        #plot_water_levels(station, dates, levels)
        #plot_water_levels(station[0].name, dates, levels)

        # low, high = station.typical_range
        # plt.axhline(y = low, xmin=mpdates.date2num(dates[0]), xmax=mpdates.date2num(dates[-1]), color = 'r', linestyle = '-')
        # plt.axhline(y = high, xmin=mpdates.date2num(dates[0]), xmax=mpdates.date2num(dates[-1]), color = 'b', linestyle = '-')

        plt.plot(dates, levels)
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45);
        plt.title(station.name)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()



    


