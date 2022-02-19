from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import station_level_over_threshold

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # create a list using station_level_over_threshold function that has stations with ratio > 0.8
    list1 = station_level_over_threshold(stations, 0.8)

    # iterate across the list and print out each station with its ratio
    for station in list1:
        print(station[0].name + " " + str(station[1]))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
