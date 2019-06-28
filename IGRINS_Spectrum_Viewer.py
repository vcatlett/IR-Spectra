#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import astropy.io.fits as fits
import matplotlib.pyplot as plt

# -------------------------------FUNCTIONS----------------------------------- #

def pulldata(fcount, fnames):
    '''Pulls data from the new file'''
    global starname, wave, flux, snr, nord
    hdu = fits.open(pathname + fnames[fcount])  # opens data for specific star and band
    starname = hdu[0].header['OBJECT']  # pulls name of the star from fits header
    flux = hdu[0].data  # the corrected target spectrum
    wave = hdu[1].data  # the wavelength data in angstroms
    snr = hdu[3].data  # the signal-to-noise ratio 
    nord = wave.shape[0]  # establishes the number of orders in the data


def figure(order):
    '''Plots the data for a given band and order'''
    global fcount, fnames
    x = wave[order]  # makes 1D wavelength array for specified order                         
    y1 = flux[order]  # makes 1D flux array for specified order
    y2 = snr[order]  # makes 1D array of A0V spectrum for specified order
    
    ax1.plot(x,y1,'r-o',ms=1.0,lw=0.5)  # plots wavelength vs. flux
    ax1.set_ylim((0.5,1.75))
    ax1.set_ylabel('Flux', fontsize=12)

    ax2.plot(x,y2,'b-o',ms=1.0,lw=0.5)  # plots wavelength vs. SNR
    ax2.set_ylabel('SNR', fontsize=12)
    
    plt.xlabel('Wavelength ($\AA$)', fontsize=12)  # sets x axis label
    fig.suptitle('%s%i Spectrum for %s' %(band,order,starname), fontsize=14)


def pltrefresh():
    '''Clears the figure and updates the plot'''
    global order
    ax1.clear()
    ax2.clear()
    figure(order) #calls figure function
    plt.draw() #draws updated plot


def down():
    '''Goes to the next file in the same band/order'''
    global fnames, fcount, nfiles, order
    fcount += 1
    fcount %= nfiles  # keeps fcount variable from exceeding the array size 
    pulldata(fcount,fnames)  # pulls data for new file
    pltrefresh()


def up():
    '''Goes to the previous file in the same band/order'''
    global fnames, fcount, nfiles, order
    fcount -= 1 
    fcount %= nfiles  # keeps order variable from dropping below zero 
    pulldata(fcount,fnames)  # pulls data for new file
    pltrefresh()


def orderinc():
    '''Increases the order by 1 and updates the plot'''
    global order, nord
    order += 1
    order %= nord  # keeps fcount variable from exceeding the array size
    pltrefresh()


def orderdec():
    '''Decreases the order by 1 and updates the plot'''
    global order, nord
    order -= 1
    order %= nord  # keeps order variable from dropping below zero  
    pltrefresh()


def switchband():
    '''Switches the band and loads new file names'''
    global band, fcount, fnames, order
    if band == 'H':
        band = 'K'
        if order == 26 or order == 27:  # Since H has 2 more orders than K
            order = 0
        fnames = np.load(pathname + band + '_star_names.npy')
        pulldata(fcount,fnames)
    else:        
        band = 'H'
        fnames = np.load(pathname + band + '_star_names.npy')
        pulldata(fcount,fnames)
    pltrefresh()


def press(event):
    '''Uses keyboard input to call functions'''
    if event.key == 'down':  # down arrow key
        down()
    elif event.key == 'up':  # up arrow key
        up()
    elif event.key == 'left':  # left arrow key
        orderinc()
    elif event.key == 'right':  # right arrow key
        orderdec()
    elif event.key == ' ':  # spacebar
        switchband()
    elif event.key == 'x':  # the letter x
        pltrefresh()
 
# -----------------------------END FUNCTIONS--------------------------------- #
    
# ----------------------------------MAIN------------------------------------- #

var = input("Enter desired band and order (K# or H#): ")  # asks user for starting band/order
band = var[0]  # pulls the first character of the input. Must be 'H' or 'K'
order = int(var[1:])  # pulls the remaining characters from the input 
fcount = 0  # initial file count. Will go from 0 -> # of files - 1
nord = 0  # Initial order count. Will change to 26 or 28 depending on the band

pathname = '/Your/Path/Name/'  # change to path where your data is
fnames = np.load(pathname + band + '_star_names.npy')  # all of the star names for given band
pulldata(fcount,fnames)  # pulls data for initial file and given band+order 
nfiles = np.size(fnames)  # finds number of files to cycle through

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)  # creates the figure
plt.subplots_adjust(hspace=0.1, wspace=1.0)
fig.text(1, 0, 'VCatlett/MGutierrez 2019', style='italic', fontsize=8, 
         color='black', ha='right', va='bottom', alpha=0.3)
figure(order)
plt.show()

fig.canvas.mpl_connect('key_press_event', press)  # ready for keyboard input

# ----------------------------------END MAIN--------------------------------- #