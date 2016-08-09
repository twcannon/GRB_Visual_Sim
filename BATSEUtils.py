
import numpy as np
from urllib2 import urlopen




def get_BATSE_durations(burst_num):
    ###############################
    # Given a burst ID, this function retrieves the duration data for the burst
    # and returns it into an array.
    #
    # Returned Array indices: 
    #     [burst_ID, T50_duration, T50_uncert, T50_start, T90_duration, T90_uncert, T90_start]
    ###############################

    # check to see if t90 data exists for burst ##
    t90data = urlopen("http://gammaray.nsstc.nasa.gov/batse/grb/catalog/current/tables/duration_table.txt")
    exists = 0

    # pad the burst ID for searching the duration table
    if len(burst_num) == 3:
        pad = '   '
    elif len(burst_num) ==4:
        pad = '  '
    else:
        pad = ' '

    # earch the duration table and return results
    for line in t90data:
        if line.startswith(pad + burst_num + ' '): 
            print "t90 data exists for " + burst_num
            split_string = line.split()
            t90_dur, t90_start = split_string[4], split_string[6]
            exists = 1
            break
    if exists == 0:
        return "t90 data does not exist for " + burst_num + ". This may cause the background noise to be simulated incorrectly"

    t90_data = line.split()
    return t90_data




def get_BATSE_bg_slope(burst_num,data):
    ###############################
    # Given a burst ID and an array of BATSE time-series data, this function calculates the background
    # slope of a burst and returns it as a float.
    ###############################

    # get duration data
    t90_data = get_BATSE_durations(burst_num)



