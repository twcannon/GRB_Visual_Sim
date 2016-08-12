
from os import path
from scipy import stats
import numpy as np
from urllib2 import urlopen




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

    # check to see if basic data exists for burst #
    data = urlopen("http://gammaray.nsstc.nasa.gov/batse/grb/catalog/current/tables/basic_table.txt")
    exists = 0

    # pad the burst ID for searching the basic table
    if len(burst_num) == 3:
        pad = '  '
    elif len(burst_num) == 4:
        pad = ' '
    else:
        pad = ''

    # search the basic table and return results
    for line in data:
        if line.startswith(pad + burst_num + ' '): 
            print "basic data exists for " + burst_num
            exists = 1
            break
    if exists == 0:
        return "basic data does not exist for " + burst_num

    basic_data_array = line.split()
    return basic_data_array



def get_BATSE_bg_slope(burst_num):
    ###############################
    # Given a burst ID, this function returns the start and end background bounds
    #   relative to the trigger, the background slope, and the background height.
    # Slope and height in the table was calculated by removing the data between the t90 start and end points,
    #   and running a linear least squares on the remaining data. (not a perfect method, but it gets the point)
    # NOTE: Some values turn up null/nan. This is most likely due to incorrectly calculated t90 times.
    # values returned are:
    #     [burst_id  start_bkgd_bound  end_bkgd_bound  background_slope  background_height]
    ###############################
    data = open("background_data.txt")
    exists = 0

    # search the background table and return results
    for line in data:
        if line.startswith(burst_num + ' '): 
            print "background data exists for " + burst_num
            exists = 1
            break
    if exists == 0:
        return "background data does not exist for " + burst_num

    basic_data_array = line.split()
    return basic_data_array




def get_BATSE_burst_data(burst_num):
    ###############################
    # Given a burst ID, this function retrieves the burst data
    # and returns it into two arrays. One for the header data 
    # and one for the time-series data
    #
    # HEADER ARRAY INDICIES:
    #   (trig#): unique BATSE trigger number
    #   (npts): total number of samples to follow, per energy channel
    #   (nlasc): total number of DISCLA 64-ms samples concatenated prior to PREB
    #   (1preb): first PREB sample number after last 1.024-s DISCLA sample
    #
    # TIME SERIES ARRAYS: channels 1 - 4
    ###############################

    fname = '/Users/Thomas/Desktop/Code/Python_GRB/data/raw_data/cat64ms.' + burst_num.zfill(5)
    # open and parse burst data into 64ms time format
    if not path.isfile(fname): 
        print "No data for Burst ID: " + burst_num
        return
    print 'Opening burst '+ burst_num
    chan1, chan2, chan3, chan4 = np.loadtxt(fname, dtype = float, unpack=True, skiprows=2)
    header_array = [chan1[0], chan2[0], chan3[0], chan4[0]]
    chan1, chan2, chan3, chan4 = chan1[+1:], chan2[+1:], chan3[+1:], chan4[+1:]

    return header_array, chan1, chan2, chan3, chan4




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

    # check to see if duration data exists for burst #
    data = urlopen("http://gammaray.nsstc.nasa.gov/batse/grb/catalog/current/tables/duration_table.txt")
    exists = 0

    # pad the burst ID for searching the duration table
    if len(burst_num) == 3:
        pad = '   '
    elif len(burst_num) == 4:
        pad = '  '
    else:
        pad = ' '

    # search the duration table and return results
    for line in data:
        if line.startswith(pad + burst_num + ' '): 
            print "duration data exists for " + burst_num
            exists = 1
            break
    if exists == 0:
        return "duration data does not exist for " + burst_num

    dur_data_array = line.split()
    return dur_data_array





