#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:38:36 2021

@author: francescopiscitelli
"""
###############################################################################
###############################################################################
########    TPH logger for sensor MS8607_02BA file reader    ################## 
########    V1.0  2021/02/01      francescopiscitelli        ##################
###############################################################################
###############################################################################

import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
# import datetime
# import matplotlib

from lib import readLogFile as rlf 

###############################################################################
###############################################################################
print('----------------------------------------------------------------------')
plt.close("all")
currentLoc = os.path.abspath(os.path.dirname(__file__))
###############################################################################
###############################################################################

dataPath = currentLoc+'/LogFiles/'

# file base name 
fileNameBase = 'Utgard_TPHlog_'

# plot these dates in this senquence 
dates = ['2021-01-30','2021-01-31','2021-02-01']

###############################################################################
###############################################################################

palette = sns.color_palette(palette = 'bright' ,n_colors = len(dates))

###############################################################################
###############################################################################

fig, ax = plt.subplots(num=1, figsize=(12,12), nrows=3, ncols=len(dates), sharex=True, sharey=False)
ax.shape  = (3,len(dates))
ax        = np.atleast_2d(ax)

for dd in range(len(dates)):

    currentFile = fileNameBase+dates[dd]+'.txt'
    
    Time, TPH = rlf.readLogFile(dataPath,currentFile,fileHeader=2)
    
    
    
    ax[0][dd].set_title('date '+dates[dd])
    ax[0][dd].plot(Time,TPH[:,0],color=palette[dd])
    ax[1][dd].plot(Time,TPH[:,1],color=palette[dd])
    ax[2][dd].plot(Time,TPH[:,2],color=palette[dd])
    
    ax[2][dd].set_xlabel('Time') 
    # plt.xticks(rotation=90)
    
    # ax[0][dd].set_ylim([10,30]) 
    # ax[1][dd].set_ylim([960,1030]) 
    # ax[2][dd].set_ylim([20,90]) 

    # plt.xticks(rotation=90)
    # plt.setp(ax[0][dd].get_xticklabels(), rotation=90)

ax[0][0].set_ylabel('T (C)') 
ax[1][0].set_ylabel('P (mBar)')
ax[2][0].set_ylabel('RH (%)')
   