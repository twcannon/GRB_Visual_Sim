
import numpy as np
import os, sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as colors
from urllib2 import urlopen
from BATSEUtils import get_BATSE_bg_slope




def main():

    plot_size = 500

    ####################################
    #### Imports and Organizes Data ####
    ####################################

    ## get burst id from user ###
    burst_num = str(input("Enter Burst ID "))
    fname = '/Users/Thomas/Desktop/Code/Python_GRB/data/raw_data/cat64ms.' + burst_num.zfill(5)

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

    slope = get_BATSE_bg_slope(burst_num,four_channel)

    print slope

    # med_chan = np.median(four_channel)
    # zvals = np.random.poisson(lam=med_chan,size=(plot_size,plot_size))+med_chan
    # zvals[0][0] = max(four_channel)
    # zvals[plot_size-1][plot_size-1] = 0

    # # make a color map of fixed colors
    # cmap = colors.LinearSegmentedColormap.from_list('my_colormap', ['black','red'], 256)
    # # tell imshow about color map so that only set colors are used
    # img = plt.imshow(zvals,interpolation='nearest', cmap = cmap, origin='lower')
    # # make a color bar
    # plt.colorbar(img,cmap=cmap)

    # plt.show()


    # cnt = 0
    # color_arr = ('blue','green','yellow','red')
    # chan_arr = (chan1, chan2, chan3, chan4)
    # img = []
    # for i in range(len(chan_arr)):
        
    #     med_chan1 = np.median(chan_arr[i])
    #     zvals = np.random.poisson(lam=med_chan1,size=(plot_size,plot_size))+med_chan1
    #     zvals[0][0] = max(chan_arr[i])
    #     zvals[plot_size-1][plot_size-1] = 0
    #     if cnt > 0:
    #         print i
    #         # make a color map of fixed colors
    #         cmap = colors.LinearSegmentedColormap.from_list('my_colormap', ['black',color_arr[i]], 256)
    #         # tell imshow about color map so that only set colors are used
    #         img = plt.imshow(zvals,interpolation='nearest', cmap = cmap, origin='lower')
    #         img = blend(background, list(zvals), 0.25)
    #         # make a color bar
    #         plt.colorbar(img,cmap=cmap)
    #     background = zvals
    #     cnt = cnt+1
    #     print cnt
    # plt.show()


    print 'Done'

    # def animate(i):
    #     xMarker,yMarker = antPathY[:i+1],antPathX[:i+1]
    #     line.set_data(xMarker,yMarker)
    #     return line,
        
    # anim = animation.FuncAnimation(fig, animate, frames=iterations, interval=20, blit=False)
    # plt.show()


if __name__ == "__main__":
    main()