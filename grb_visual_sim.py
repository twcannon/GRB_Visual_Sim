
import numpy as np
import os, sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl



def main():

    ####################################
    #### Imports and Organizes Data ####
    ####################################

    ## open and parse burst data into 64ms time format ###
    burst_num = str(input("Enter Burst ID ")).zfill(5)
    fname = '/path/to/cat64ms.' + burst_num
    if not os.path.isfile(fname): 
        print "No data for Burst ID: " + burst_num
        return
    print 'Opening burst '+ burst_num

    chan1, chan2, chan3, chan4 = np.loadtxt(fname, dtype = float, unpack=True, skiprows=2)
    four_channel = np.add(np.add(np.add(chan1,chan2),chan3),chan4)
    # trig_num, num_points, num_lasc, one_preb = chan1[0], chan2[0], chan3[0], chan4[0]
    # chan1, chan2, chan3, chan4 = chan1[+1:], chan2[+1:], chan3[+1:], chan4[+1:]
    # time = (np.arange(0,num_points).astype(int)-num_lasc)*.064


    zvals = np.random.poisson(size=(100,100))*10

    # make a color map of fixed colors
    cmap = mpl.colors.LinearSegmentedColormap.from_list('my_colormap', ['black','red'], 256)
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