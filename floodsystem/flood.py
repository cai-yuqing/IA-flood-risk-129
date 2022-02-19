from .station import MonitoringStation
from .utils import sorted_by_key

#Task2B
def station_level_over_threshold(stations, tol):
    """function that returns a list of tuples, where each tuble holds (i) a station (object) at which the latest relative water level is over tol and (ii) the relatvie water level at the station"""

    list1 = []
    for station in stations:

        #if latest level data not available, break out from that station's data and move on to the next station
        if station.latest_level == None:
            break
        
        #if latest level data not consistent, break out from that station's data and move on to the next station
        if MonitoringStation.typical_range_consistent(station) == False:
            break

        #for the rest, if relative water level > tol, append to list the station and the relative water level
        elif MonitoringStation.relative_water_level(station) > tol:
            list1.append((station, MonitoringStation.relative_water_level(station)))

    #sort list based on the relative water level using function in floodsystem
    return sorted_by_key(list1, 1, reverse=True)

#Task2C
def stations_highest_rel_level(stations, N):
    """function that returns a list of the N stations (object) at which the water level, relative to the typical range, is highest. List should be sorted in descending order by relative level"""
    
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
    return sorted_by_key(list1, 1, reverse=True)[:N]



