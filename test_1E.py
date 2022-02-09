from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_by_station_number

def test_rivers_by_station_number():
    """Test for Task1E functions"""

    #create 4 test stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    label = "Test station"
    coord = (0.0, 0.0)
    typical_range = (0.0, 1.0)
    town = "Test Town"
    station1 = MonitoringStation(station_id, measure_id, label, coord, typical_range, "River A", town)
    station2 = MonitoringStation(station_id, measure_id, label, coord, typical_range, "River A", town)
    station3 = MonitoringStation(station_id, measure_id, label, coord, typical_range, "River B", town)
    station4 = MonitoringStation(station_id, measure_id, label, coord, typical_range, "River C", town)

    x = rivers_by_station_number([station1, station2, station3, station4], 1)
    y = rivers_by_station_number([station1, station2, station3, station4], 2)

    #test for N = 1, return most number of stations: A with 2
    assert x == [("River A", 2)]

    #test for N = 2, return most number of stations: A, B and C since they have the same number of stations
    assert y == [("River A", 2), ("River B", 1), ("River C", 1)]

