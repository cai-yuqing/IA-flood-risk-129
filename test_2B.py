from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import station_level_over_threshold
from floodsystem.station import MonitoringStation

def test_station_level_over_threshold():
    """Test for Task2B function"""

    #create 4 test stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    river = "Test river"
    coord = (0.0, 0.0)
    typical_range = (0.0, 1.0)
    town = "Test Town"
    station1 = MonitoringStation(station_id, measure_id, "Station A", coord, typical_range, river, town)
    station2 = MonitoringStation(station_id, measure_id, "Station B", coord, typical_range, river, town)
    station3 = MonitoringStation(station_id, measure_id, "Station C", coord, typical_range, river, town)
    station4 = MonitoringStation(station_id, measure_id, "Station D", coord, typical_range, river, town)

    #set the latest level data for these 4 stations
    station1.latest_level = 0.1
    station2.latest_level = 0.6
    station3.latest_level = 0.9
    station4.latest_level = 0.99
    
    #test the function on these 4 stations, for toll = 0.8, should return station 4 and station 3 in this order in a tuple with their relative water level
    test = station_level_over_threshold([station1, station2, station3, station4], 0.8)

    assert test == [(station4, 0.99),(station3, 0.9)]
