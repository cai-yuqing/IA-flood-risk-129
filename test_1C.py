from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius

def test_stations_within_radius():
    """Test for Task1C functions"""

    #create 4 test stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    river = "Test river"
    label = "Test label"
    town = "Test Town"
    typical_range = (0, 1)
    station1 = MonitoringStation(station_id, measure_id, "Station A", (0, 0), typical_range, river, town)
    station2 = MonitoringStation(station_id, measure_id, "Station B", (0, 5), typical_range, river, town)
    station3 = MonitoringStation(station_id, measure_id, "Station C", (0, 10), typical_range, river, town)
    station4 = MonitoringStation(station_id, measure_id, "Station D", (0, 20), typical_range, river, town)

    test = stations_within_radius([station3, station2, station1, station4], (0, 0), 10)

    #test for station within a radius of 10km to origin: 
    assert test == ["Station B", "Station A"]