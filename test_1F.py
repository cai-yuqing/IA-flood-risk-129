from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation

def test_inconsistent_typical_range_stations():
    """Test for Task1F function"""

    #create 3 test stations
    station_id = "Test station_id"
    measure_id = "Test measure_id"
    river = "Test river"
    coord = (0.0, 0.0)
    town = "Test Town"
    station1 = MonitoringStation(station_id, measure_id, "Station A", coord, (0.0, 1.0), river, town)
    station2 = MonitoringStation(station_id, measure_id, "Station B", coord, (1.0, 0.0), river, town)
    station3 = MonitoringStation(station_id, measure_id, "Station C", coord, (0), river, town)
    station4 = MonitoringStation(station_id, measure_id, "Station D", coord, "string", river, town)

    test = inconsistent_typical_range_stations([station1, station2, station3, station4])

    #test for inconsistent typical ranges: 
    #A is consistent
    #B is inconsistent as typical_range[0]>typical_range
    #C is inconsistent as it only has one item in typical_range tuple
    #D is inconsistent as it its typical_range is a string not a tuple
    assert test == ["Station B", "Station C", "Station D"]
