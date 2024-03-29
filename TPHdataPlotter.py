#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:38:36 2021

@author: francescopiscitelli
"""
###############################################################################
###############################################################################
########    TPH logger for sensor MS8607_02BA file reader    ################## 
########    V1.1  2021/02/11      francescopiscitelli        ##################
###############################################################################
###############################################################################

import numpy as np
import os
import matplotlib.pyplot as plt
import datetime  
# import matplotlib

from lib import readLogFile as rlf 
from lib import syncUtil 

###############################################################################
###############################################################################
print('----------------------------------------------------------------------')
plt.close("all")
currentLoc = os.path.abspath(os.path.dirname(__file__))
###############################################################################
###############################################################################

SYNC = False    # ON/OFF if you want to tranfer the logFiles in your local Folder 

# location where log files are stored in raspPi
sourcePath = 'pi@172.30.244.189:/home/pi/dg_TPH_logger/LogFiles/'

# location where you want to copy the files in your local folder 
# destinationPath = currentLoc+'/LogFiles/'
destinationPath ='/Users/francescopiscitelli/Documents/DOC/DATA/00_logFiles_TPH_sensor_Utgard/'

# location from where to load the log files 
dataPath = destinationPath

# file base name 
fileNameBase = 'Utgard_TPHlog_'

# plot these dates from (included) ... to ...(excluded)
dateStart = '2023-09-20'
# dateStart = '2022-04-05'
dateEnd   = '2023-09-30'

###############################################################################
###############################################################################
########    end of with all the settings you can choose   #####################
########        DO NOT EDIT BELOW THIS LINE!!!!           #####################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
##############################################################################

if SYNC == True:
    syncUtil.syncData(sourcePath,destinationPath)

###############################################################################

start = datetime.datetime.strptime(dateStart, "%Y-%m-%d")
end   = datetime.datetime.strptime(dateEnd, "%Y-%m-%d")

dates = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

###############################################################################

Tg   = []
TPHg = np.empty((0,3), dtype=float)

for dd in dates:
    
    currentDate = datetime.datetime.strftime(dd, '%Y-%m-%d') 
    
    currentFile = fileNameBase+currentDate+'.txt'
    
    Time, TPH, flag = rlf.readLogFile(dataPath,currentFile,fileHeader=2,Ncols=3)
    
    if flag == -1 :
        print('\033[1;33mWARNING: Log file for date '+ currentDate +' does not exist -> skipped! \033[1;37m')
        continue
    
    else:
         
        Time2 = [currentDate +' '+ s for s in Time]
              
        for tt in range(len(Time2)):
            
            Time2[tt] =  datetime.datetime.strptime(Time2[tt], '%Y-%m-%d %H:%M:%S') 
         
        TPHg = np.append(TPHg,TPH,axis=0)
        Tg   = np.append(Tg,Time2,axis=0)
  

###############################################################################

# windowSize = 7



############
   
fig, ax = plt.subplots(num=1, figsize=(10,7), nrows=3, ncols=1, sharex=True, sharey=False)    
ax[0].plot(Tg,TPHg[:,0],linestyle='None',color='r',marker='o',markersize=3)
ax[1].plot(Tg,TPHg[:,1],linestyle='None',color='g',marker='o',markersize=3)
ax[2].plot(Tg,TPHg[:,2],linestyle='None',color='b',marker='o',markersize=3)
    

# formatter = matplotlib.dates.DateFormatter('%y-%m-%d %H:%M')
# ax[2].xaxis.set_major_formatter(formatter)
# ax[2].xaxis.set_minor_formatter(formatter)
fig.autofmt_xdate()
# ax[2].set_xlabel('Date - Time') 

ax[0].set_ylabel('T ($^o$C)') 
ax[1].set_ylabel('P (mbar)')
ax[2].set_ylabel('RH (%)')

plt.minorticks_on()

ax[0].grid()
ax[1].grid()
ax[2].grid()

# LastDays = 7

# Trange = -LastDays*48

# Tmax = -30

# fig, ax = plt.subplots(num=2, figsize=(10,7), nrows=3, ncols=1, sharex=True, sharey=False)    
# ax[0].plot(Tg[Trange:Tmax],TPHg[Trange:Tmax,0],linestyle='None',color='r',marker='o',markersize=3)
# ax[1].plot(Tg[Trange:Tmax],TPHg[Trange:Tmax,1],linestyle='None',color='g',marker='o',markersize=3)
# ax[2].plot(Tg[Trange:Tmax],TPHg[Trange:Tmax,2],linestyle='None',color='b',marker='o',markersize=3)
    

# # formatter = matplotlib.dates.DateFormatter('%y-%m-%d %H:%M')
# # ax[2].xaxis.set_major_formatter(formatter)
# # ax[2].xaxis.set_minor_formatter(formatter)
# fig.autofmt_xdate()
# # ax[2].set_xlabel('Date - Time') 

# ax[0].set_ylabel('T ($^o$C)') 
# ax[1].set_ylabel('P (mbar)')
# ax[2].set_ylabel('RH (%)')

# plt.minorticks_on()

# ax[0].grid()
# ax[1].grid()
# ax[2].grid()

plt.show()
   
###############################################################################