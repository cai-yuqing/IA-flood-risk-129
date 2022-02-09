from floodsystem.station import MonitoringStation
from floodsystem.geo import station_by_distance

def test_station_by_distance():
    """Test for Task1B functions"""

    #create 4 test stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    river = "Test river"
    label = "Test label"
    town = "Test Town"
    typical_range = (0, 1)
    station1 = MonitoringStation(station_id, measure_id, "Station A", (0, 0), typical_range, river, town)
    station2 = MonitoringStation(station_id, measure_id, "Station B", (0, 1), typical_range, river, town)
    station3 = MonitoringStation(station_id, measure_id, "Station C", (0, 2), typical_range, river, town)
    station4 = MonitoringStation(station_id, measure_id, "Station D", (0, 3), typical_range, river, town)

    test = station_by_distance([station3, station2, station1, station4], (0, 0))

    #test for distance from a certain coordinate: 
    assert test == ["Station A", "Station B", "Station C", "Station D"]