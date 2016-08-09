
import numpy as np
import os, sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as colors
from urllib2 import urlopen
from BATSEUtils import get_BATSE_bg_slope, get_BATSE_basic_table, get_BATSE_burst_data, get_BATSE_durations




def main():

    plot_size = 500
    ## get burst id from user ###
    burst_num = str(input("Enter Burst ID "))

    header_data,chan1,chan2,chan3,chan4 = get_BATSE_burst_data(burst_num)
    four_channel = np.add(np.add(np.add(chan1,chan2),chan3),chan4)

    # time calculated off of npts and nlasc from basic table data
    time = (np.arange(0,header_data[1]).astype(int)-header_data[2])*.064
    # might not be correct -> start_time = header_data[2] + header_data[3]

    basic_data = get_BATSE_basic_table(burst_num)
    duration_data = get_BATSE_durations(burst_num)

    # slope = get_BATSE_bg_slope(burst_num,four_channel,time,t90_dur,t90_start,trigger)

    print basic_data

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