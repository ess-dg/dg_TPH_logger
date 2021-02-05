#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:40:01 2021

@author: francescopiscitelli
"""
###############################################################################
###############################################################################
########    TPH logger watchdog                          ###################### 
########    V1.0  2021/02/04      francescopiscitelli    ######################
###############################################################################
###############################################################################

import datetime as dt
import time
import os
import glob

###############################################################################
###############################################################################

currentLoc = os.path.abspath(os.path.dirname(__file__))

###############################################################################
###############################################################################

# in sec, time of checks 
timeCheck = 900

# in sec, time if no new file or mod file, restart process  -> reboot 
timeInterval = 3600

###############################################################################
###############################################################################

tStep = dt.timedelta(seconds=timeCheck)

while True:
    
    nowTime = dt.datetime.now()
    
    ######################################
    # start of function check_if_running()
    ######################################
    
    # print('checking...')
    listOfFiles = glob.glob(currentLoc+'/LogFiles/*.txt') 
    latestFile  = max(listOfFiles, key=os.path.getmtime)
    
    # print('last file'+latestFile)
    
    mTime   = time.ctime(os.path.getmtime(latestFile))
    mTime2  = dt.datetime.strptime(mTime, "%a %b %d %H:%M:%S %Y")
    
    duration      = nowTime - mTime2
    duration_in_s = duration.total_seconds() 
    
    if duration_in_s > timeInterval:
        
        # print('restarting')
        os.system('sudo reboot')
    
    ######################################
    # end of function
    ######################################
    
    while dt.datetime.now() < nowTime + tStep:
        1==1



