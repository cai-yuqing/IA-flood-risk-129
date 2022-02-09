from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_with_station, stations_by_river

def test_rivers_with_station():
    """Test for Task1D functions"""

    #create 4 test stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    #river = "Test river"
    #coord = (0.0, 0.0)
    label = "Test label"
    town = "Test Town"
    typical_range = (0, 1)
    station1 = MonitoringStation(station_id, measure_id, "Station A", (0, 0), typical_range, "River A", town)
    station2 = MonitoringStation(station_id, measure_id, "Station B", (0, 1), typical_range, "River A", town)
    station3 = MonitoringStation(station_id, measure_id, "Station C", (0, 2), typical_range, "River B", town)
    station4 = MonitoringStation(station_id, measure_id, "Station D", (0, 3), typical_range, "River C", town)

    test = rivers_with_station([station3, station2, station1, station4])

    #test for distance from a certain coordinate: 
    assert test == "3"+ ["River A", "River B", "River C"]



def test_stations_by_river():
    """Test for Task1B functions"""

    #create 4 test stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    #river = "Test river"
    #coord = (0.0, 0.0)
    label = "Test label"
    town = "Test Town"
    typical_range = (0, 1)
    station1 = MonitoringStation(station_id, measure_id, "Station A", (0, 0), typical_range, "River A", town)
    station2 = MonitoringStation(station_id, measure_id, "Station B", (0, 1), typical_range, "River A", town)
    station3 = MonitoringStation(station_id, measure_id, "Station C", (0, 2), typical_range, "River B", town)
    station4 = MonitoringStation(station_id, measure_id, "Station D", (0, 3), typical_range, "River C", town)

    test = stations_by_river([station3, station2, station1, station4])

    #test for distance from a certain coordinate: 
    assert test["River A"] == ["Station A", "Station B"]
    assert test["River B"] == ["Station C"]
    assert test["River C"] == ["Station D"]

