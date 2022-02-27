import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    """Requirements for Task 2G"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # create lists for each category
    severe = []
    high = []
    moderate = []
    low = []

    #get the 5 stations with highest water level
    highest = stations_highest_rel_level(stations, 5)
    print(highest)
    highest_Sta = []
    for highest_sta in highest:
        highest_Sta.append(highest_sta[0])

    #iterate through the highest stations to get the dates and water levels
    for station in highest_Sta:
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=10))
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
        if a >= len(dates)*0.2:
            severe.append(station.name)
        elif b >= len(dates)*0.4:
            high.append(station.name)
        elif c >= len(dates)*0.7:
            moderate.append(station.name)
        else:
            low.append(station.name)
    print('Stations with greatest flooding risk:', severe)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
