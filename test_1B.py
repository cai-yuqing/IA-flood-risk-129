from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from floodsystem.haversine import haversine

def test_stations_by_distance():
    """Tests for Task 1Bfunction"""

    #create 2 stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    typical_range = (0, 1)
    river = "Test river"
    town = "Test Town"
    station1 = MonitoringStation(station_id, measure_id, "Station A", (53.2053, 0.1218), typical_range, river, town)
    station2 = MonitoringStation(station_id, measure_id, "Station B", (53.2053, 1.1218), typical_range, river, town)

    stations = [station1, station2]
    p = (52.2053, 0.1218)
    dist1 = haversine(p[0], p[1], 53.2053, 0.1218)
    dist2 = haversine(p[0], p[1], 53.2053, 1.1218)

    list1 = stations_by_distance(stations, p)

    assert list1 == [("Station A", dist1), ("Station B", dist2)]
