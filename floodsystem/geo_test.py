from .utils import sorted_by_key  # noqa
from .stationdata import build_station_list
from .haversine import haversine
from .station import MonitoringStation
from .datafetcher import fetch, fetch_latest_water_level_data,\
     fetch_measure_levels, fetch_station_data, dump, load

def rivers_with_station(stations):
    stations = build_station_list()
    rs_list = []
    for station in stations:
        rivers = station.river
        #rs_list.append(rivers)
        #river_list = set(rs_list)
        if rivers in rs_list:
            continue
        else:
            rs_list.append(rivers)
    rs_list.sort()
    return rs_list