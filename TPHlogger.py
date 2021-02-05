#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:22:57 2021

@author: francescopiscitelli

"""
###############################################################################
###############################################################################
########    TPH logger for sensor MS8607_02BA            ###################### 
########    V1.0  2021/01/28      francescopiscitelli    ######################
###############################################################################
###############################################################################

from lib import MS8607_02BA as sensor 
# import numpy as np

from datetime import datetime
import time
import os

###############################################################################
###############################################################################

currentLoc = os.path.abspath(os.path.dirname(__file__))

###############################################################################
###############################################################################

# time interval to log (s)
timeInterval = 1800

# split files every day at 00:00

# folder to dump log files 
folderPath = currentLoc+'/LogFiles/'

# file base name 
fileNameBase = 'Utgard_TPHlog'


###############################################################################
###############################################################################

nowTime = datetime.now()
current_date = nowTime.strftime("%Y-%m-%d")
current_time = nowTime.strftime("%H:%M:%S")
# fileh = folderPath+fileNameBase+'_'+current_date+'.txt'
# if os.path.exists(fileh):
#    print('\n \033[1;33mWARNING: Log file for this date already file exists, it will be overwritten!\033[1;37m')
#    os.system('rm '+fileh)
   
filepower = folderPath+fileNameBase+'_'+current_date+'_PowerFailure.txt' 
if os.path.isfile(filepower):
   # if the file already exists open it appending
   fop = open(filepower, "a")
else:
    # open/create a new file and add the field names
   fop = open(filepower, "w")
   
stringa1 = 'Logging restarted at '+  current_date+ '\t' + current_time +'\n'

fop.writelines(stringa1)

fop.close()
   

while True:
    
    (temperature, humidity, pressure) = sensor.get_THP_from_MS8607() 
    
    # temperature = 23+np.random.rand()
    # humidity = 40+np.random.rand()
    # pressure = 950+np.random.rand()
    
    nowTime = datetime.now()
    
    current_date = nowTime.strftime("%Y-%m-%d")
    current_time = nowTime.strftime("%H:%M:%S")

    ####### Output data to screen ###############
    print("date: %s" %current_date)
    print("time: %s" %current_time)
    print("Temperature in Celsius : %.2f C" %temperature)
    print("Pressure is : %.2f mbar" %pressure)
    print("Relative Humidity : %.2f %%" %humidity)
    print("--------------------------------------")
    #############################################
    
    fileh = folderPath+fileNameBase+'_'+current_date+'.txt'
    
    temp = '%.2f\t%.2f\t%.2f\n' % (temperature, pressure, humidity)
    stringa = current_time+'\t'+temp
        
    if os.path.isfile(fileh):
       # if the file already exists open it appending
       fo = open(fileh, "a")
    else:
       # open/create a new file and add the field names
       fo = open(fileh, "w")
       fo.writelines("Log File for date: " + current_date + "\n")
       fo.writelines("columns: time, T(C), P(mBar), RH(%) \n")
                
    fo.writelines(stringa)

    fo.close()     
    
    time.sleep(timeInterval)
        

    
    