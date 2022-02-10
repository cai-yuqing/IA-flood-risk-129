from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation

def test_stations_within_radius():
    """Tests for Task 1C function"""

    #create 2 stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    typical_range = (1.0, 2.0)
    river = "Test river"
    town = "Test Town"
    station1 = MonitoringStation(station_id, measure_id, "Station A", (52.2053, 0.1218), typical_range, river, town)
    station2 = MonitoringStation(station_id, measure_id, "Station B", (52.2053, 10.1218), typical_range, river, town)

    stations = [station1, station2]
    centre = (52.2053, 0.1218)
    r = 10

    list1 = stations_within_radius(stations, centre, r)

    assert list1 == ["Station A"]
