from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # create a list using stations_highest_rel_level function that has top N stations with highest rel water level
    list1 = stations_highest_rel_level(stations, 10)

    # iterate across the list and print out each station with its ratio
    for station in list1:
        print(station[0].name + " " + str(station[1]))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
