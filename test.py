from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib.pyplot as plt
from datetime import date, timedelta
# from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels

    # Build list of stations
stations = build_station_list()

update_water_levels(stations)

    #get the 5 stations with highest water level
highest = stations_highest_rel_level(stations, 5)
print(highest)

    # t = []
    # for i in range(11):
    #     t.append(date.today() - timedelta(i))

    #list of stations from near to far
for station in highest:
    dates, levels = fetch_measure_levels(
     station.measure_id, dt=timedelta(days=10))
    print(station[0].name)
        #plot_water_levels(station, dates, levels)
        #plot_water_levels(station[0].name, dates, levels)

    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.tight_layout()
    plt.show()




    


