
import numpy as np
import os, sys
import math
import matplotlib.animation as animation
import matplotlib.colors as colors
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from BATSEUtils import get_BATSE_bg_slope, get_BATSE_basic_table, get_BATSE_burst_data, get_BATSE_durations




def main():

    plot_size = 500
    ## get burst id from user ###
    burst_num = str(input("Enter Burst ID "))

    header_data,chan1,chan2,chan3,chan4 = get_BATSE_burst_data(burst_num)
    four_channel = np.add(np.add(np.add(chan1,chan2),chan3),chan4)
    time = (np.arange(len(four_channel)))*0.064

    # trigger_index = (header_data[2]-1) + (32+1)
    # ctime=0.064*(np.arange(len(four_channel))-trigger_index)
    # basic_data = get_BATSE_basic_table(burst_num)
    # duration_data = get_BATSE_durations(burst_num)

    burst_id,start_bkgd_bound,end_bkgd_bound,background_slope,background_height = get_BATSE_bg_slope(burst_num)
    background = (np.ones(len(four_channel))*float(background_slope))+float(background_height)
    # plt.plot(time,four_channel)
    # plt.plot(time,background)
    # plt.show()


    # x = np.linspace(0, 5, 10, endpoint=False)
    # y = multivariate_normal.pdf(x, mean=2.5, cov=0.5); y
    # plt.plot(x, y)


    x, y = np.mgrid[-1:1:.01, -1:1:.01]
    pos = np.empty(x.shape + (2,))
    pos[:, :, 0] = x; pos[:, :, 1] = y
    rv = multivariate_normal([0.5, -0.2], [[2.0, 0.3], [0.3, 0.5]])
    # plt.contourf(x, y, rv.pdf(pos))

    # plt.show()



    # x, y = np.mgrid[-1.0:1.0:30j, -1.0:1.0:30j]
    # # Need an (N, 2) array of (x, y) pairs.
    # xy = np.column_stack([x.flat, y.flat])

    # mu = np.array([0.0, 0.0])

    # sigma = np.array([.025, .025])
    # covariance = np.diag(sigma**2)

    # z = multivariate_normal(xy, mean=mu, cov=covariance)

    # # Reshape back to a (30, 30) grid.
    # z = z.reshape(x.shape)
    # print z



    med_chan = np.median(four_channel)
    zvals = np.random.poisson(lam=med_chan,size=(plot_size,plot_size))+med_chan
    zvals[0][0] = max(four_channel)
    zvals[plot_size-1][plot_size-1] = 0

    # make a color map of fixed colors
    cmap = colors.LinearSegmentedColormap.from_list('my_colormap', ['black','red'], 256)
    # tell imshow about color map so that only set colors are used
    img = plt.imshow(rv.pdf(pos),interpolation='nearest', cmap = cmap, origin='lower')
    # make a color bar
    plt.colorbar(img,cmap=cmap)

    plt.show()


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