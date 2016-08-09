
import numpy as np
from urllib2 import urlopen



def get_BATSE_durations(burst_num):
    ###############################
    # Given a burst ID, this function retrieves the duration data for the burst
    # and returns it into an array.
    #
    # ARRAY INDICIES:
    #   The BATSE trigger number. This number can be used for cross-referencing with other tables in this BATSE catalog.
    #   T50.
    #   Uncertainty in T50.
    #   The start time of the T50 interval, relative to the trigger time. The trigger time can be found in the BASIC Table.
    #   T90.
    #   Uncertainty in T90.
    #   The start time of the T90 interval, relative to the trigger time.
    #   All columns are in units of seconds. 
    ###############################

    # check to see if duration data exists for burst ##
    data = urlopen("http://gammaray.nsstc.nasa.gov/batse/grb/catalog/current/tables/duration_table.txt")
    exists = 0

    # pad the burst ID for searching the duration table
    if len(burst_num) == 3:
        pad = '   '
    elif len(burst_num) == 4:
        pad = '  '
    else:
        pad = ' '

    # earch the duration table and return results
    for line in data:
        if line.startswith(pad + burst_num + ' '): 
            print "duration data exists for " + burst_num
            exists = 1
            break
    if exists == 0:
        return "duration data does not exist for " + burst_num

    dur_data_array = line.split()
    return dur_data_array



def get_BATSE_basic_table(burst_num):
    ###############################
    # Given a burst ID, this function retrieves the bacis table data for the burst
    # and returns it into an array.
    #
    # ARRAY INDICIES:
    #   The BATSE trigger number.
    #   The BATSE Catalog burst name.
    #   The truncated Julian Date (TJD) of the trigger TJD = JD - 2440000.5
    #   The time in decimal seconds of day (UT) of the trigger.
    #   right ascension (J2000) in decimal degrees.
    #   declination (J2000) in decimal degrees.
    #   Galactic longitude in decimal degrees.
    #   Galactic latitude in decimal degrees.
    #   radius in decimal degrees of positional error box.
    #   angle in decimal degrees of geocenter (the angle between the burst and the nadir, as measured from the satellite).
    #   overwrite flag: Y(true) if this burst overwrote an earlier, weaker trigger. N(false) otherwise.
    #   overwritten flag: Y(true) if this burst was overwritten by a later, more intense trigger. N(false) otherwise.
    ###############################

    # check to see if basic data exists for burst ##
    data = urlopen("http://gammaray.nsstc.nasa.gov/batse/grb/catalog/current/tables/basic_table.txt")
    exists = 0

    # pad the burst ID for searching the basic table
    if len(burst_num) == 3:
        pad = '  '
    elif len(burst_num) == 4:
        pad = ' '
    else:
        pad = ''

    # earch the basic table and return results
    for line in data:
        if line.startswith(pad + burst_num + ' '): 
            print "basic data exists for " + burst_num
            exists = 1
            break
    if exists == 0:
        return "basic data does not exist for " + burst_num

    basic_data_array = line.split()
    return basic_data_array



def get_BATSE_bg_slope(burst_num,data):
    ###############################
    # Given a burst ID and an array of BATSE time-series data, this function calculates the background
    # slope of a burst and returns it as a float.
    # Slope is calculated by removing the data between the t90 start and end points,
    # and then running a least squares on the remainder. (not a perfect method, but it gets the idea across)
    ###############################

    # get duration data
    duration_data = get_BATSE_durations(burst_num)
    basic_data = get_BATSE_basic_table(burst_num)

    t90_dur, t90_start = duration_data[4], duration_data[6]

    print basic_data