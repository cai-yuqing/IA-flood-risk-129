# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    #Task1F
    def typical_range_consistent(self):
        """method to check the typical high/low range data for consistency"""

        #check if typical range data is a tuple, if not return False
        if isinstance(self.typical_range, tuple) == False:
            return False

        #check if typical high range is lower than typical low range, if not return False
        if self.typical_range[1] < self.typical_range[0]:
            return False
        
        #check if typical range has both high and low range data and nothing more, if not return False
        if len(self.typical_range) != 2:
            return False

        #any other case return True
        else:
            return True

    #Task2B
    def relative_water_level(self):
        """method that returns the latest water level as a fraction of the typical range"""
        
        #if the necessary data is not available, function should return None
        if self.latest_level == None:
            return None
        
        #if the necessary data is not consistent, function should return None
        if MonitoringStation.typical_range_consistent(self) == False:
            return False

        #if the necessary data is available and consistent, function should return ratio
        elif MonitoringStation.typical_range_consistent(self) == True:
            
            #return (latest - low)/(high-low)
            return (self.latest_level - self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])

#Task1F
def inconsistent_typical_range_stations(stations):
    """Requirements for Task 1F"""

    #list of stations with inconsistent typical range data
    inconsistent_list = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == False:
            inconsistent_list.append(station.name)

    #sort list of stations with inconsistent typical range data in alphabetical order
    inconsistent_list.sort()

    return inconsistent_list