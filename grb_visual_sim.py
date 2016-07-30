
import numpy as np
import os, sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as colors
from urllib2 import urlopen



def main():

    plot_size = 500

    ####################################
    #### Imports and Organizes Data ####
    ####################################

    ## get burst id from user ###
    burst_num = str(input("Enter Burst ID "))
    fname = '/Users/Thomas/Desktop/Code/Python_GRB/data/raw_data/cat64ms.' + burst_num.zfill(5)


    ## check to see if t90 data exists for burst ##
    t90data = urlopen("http://gammaray.nsstc.nasa.gov/batse/grb/catalog/current/tables/duration_table.txt")
    exists = 0
    if len(burst_num) == 3:
        pad = '   '
    elif len(burst_num) ==4:
        pad = '  '
    else:
        pad = ' '
    for line in t90data:
        if line.startswith(pad + burst_num + ' '): 
            print "t90 data exists for " + burst_num
            split_string = line.split()
            t90_dur, t90_start = split_string[4], split_string[6]
            exists = 1
            break
    if exists == 0:
        print "t90 data does not exist for " + burst_num + ". This may cause the background noise to be simulated incorrectly"


    ## open and parse burst data into 64ms time format ##
    if not os.path.isfile(fname): 
        print "No data for Burst ID: " + burst_num
        return
    print 'Opening burst '+ burst_num
    chan1, chan2, chan3, chan4 = np.loadtxt(fname, dtype = float, unpack=True, skiprows=2)
    four_channel = np.add(np.add(np.add(chan1,chan2),chan3),chan4)
    # extra data not used in this program, but it is cool
    # trig_num, num_points, num_lasc, one_preb = chan1[0], chan2[0], chan3[0], chan4[0]
    # chan1, chan2, chan3, chan4 = chan1[+1:], chan2[+1:], chan3[+1:], chan4[+1:]
    # time = (np.arange(0,num_points).astype(int)-num_lasc)*.064

    med_chan1 = np.median(chan1)
    zvals = np.random.poisson(lam=np.sqrt(med_chan1),size=(plot_size,plot_size))+med_chan1
    zvals[0][0] = max(chan1)
    zvals[plot_size-1][plot_size-1] = 0

    # make a color map of fixed colors
    cmap = colors.LinearSegmentedColormap.from_list('my_colormap', ['black','red'], 256)
    # tell imshow about color map so that only set colors are used
    img = plt.imshow(zvals,interpolation='nearest', cmap = cmap, origin='lower')
    # make a color bar
    plt.colorbar(img,cmap=cmap)

    plt.show()


    print 'Done'

    # def animate(i):
    #     xMarker,yMarker = antPathY[:i+1],antPathX[:i+1]
    #     line.set_data(xMarker,yMarker)
    #     return line,
        
    # anim = animation.FuncAnimation(fig, animate, frames=iterations, interval=20, blit=False)
    # plt.show()


if __name__ == "__main__":
    main()