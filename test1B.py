from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance

def test_stations_by_distance():
    """Test for Task1B functions"""

    #create 4 test stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    river = "Test river"
    label = "Test label"
    town = "Test Town"
    typical_range = (0, 1)
    station1 = MonitoringStation(station_id, measure_id, "Station A", (0, 0), typical_range, river, town)
    station2 = MonitoringStation(station_id, measure_id, "Station B", (3, 4), typical_range, river, town)
    station3 = MonitoringStation(station_id, measure_id, "Station C", (12, 5), typical_range, river, town)
    station4 = MonitoringStation(station_id, measure_id, "Station D", (7, 24), typical_range, river, town)

    test = stations_by_distance([station3, station2, station1, station4], (0, 0))

    #test for distance from a certain coordinate: 
    assert test == [("Station A", 0), ("Station B", 5) , ("Station C", 13) , ("Station D", 25)]