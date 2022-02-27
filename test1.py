from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key



stations = build_station_list()
    
list1 = []
for station in stations:

        #if latest level data not available, break out from that station's data and move on to the next station
    if station.latest_level == None:
        break
        
        #if latest level data not consistent, break out from that station's data and move on to the next station
    if MonitoringStation.typical_range_consistent(station) == False:
        break

        #append the rest of the station and its relative water level
    else:
        list1.append((station, MonitoringStation.relative_water_level(station)))

    #sort list based on the relative water level using function in floodsystem and fetch first N items
sorted_by_key(list1, 1, reverse=True)
print(type(sorted_by_key(list1, 1, reverse=True)))