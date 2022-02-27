from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation

def test_stations_highest_rel_level():
    """Test for Task2E function"""

    #create 4 test stations
    station_id = "Test station_id"
    #measure_id = "Test measure_id"
    river = "Test river"
    coord = (0.0, 0.0)
    typical_range = (0.0, 1.0)
    town = "Test Town"
    A = [0.95,0.95,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]
    B = [0.95,0.7,0.7,0.8,0.3,0.3,0.3,0.3,0.3,0.3]
    C = [0.95,0.7,0.5,0.5,0.5,0.5,0.5,0.3,0.3,0.3]
    D = [0.95,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]

    station1 = MonitoringStation(station_id, A, "Station A", coord, typical_range, river, town)
    station2 = MonitoringStation(station_id, B, "Station B", coord, typical_range, river, town)
    station3 = MonitoringStation(station_id, C, "Station C", coord, typical_range, river, town)
    station4 = MonitoringStation(station_id, D, "Station D", coord, typical_range, river, town)
    stations = [station1, station2, station3, station4]

    severe = []
    high = []
    moderate = []
    low = []
    for station in stations:
        levels = station.measure_id
        a = 0
        b = 0
        c = 0
        d = 0
        for level in levels:
            if level >= 0.9:
                a += 1
            if 0.7<= level:
                b += 1
            if 0.5 <= level:
                c += 1
            if level >= 0:
                d += 1
        if a >= 10*0.2:
            severe.append(station.name)
        elif b >= 10*0.4:
            high.append(station.name)
        elif c >= 10*0.7:
            moderate.append(station.name)
        else:
            low.append(station.name)
    assert severe == ["Station A"]
    assert high == ["Station B"]
    assert moderate == ["Station C"]
    assert low == ["Station D"]
        