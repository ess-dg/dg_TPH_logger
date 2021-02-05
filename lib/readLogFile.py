#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:32:52 2021

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

###############################################################################
###############################################################################

# path = '/Users/francescopiscitelli/Documents/PYTHON/THP_Logger/TPH_logger_Utgard/LogFiles/'

# fileName = 'Utgard_TPHlog_2021-01-31.txt'

# fileHeader = 2

###############################################################################
###############################################################################

def readLogFile (path,fileName,fileHeader=2):

    fileh = path+fileName
    
    if not os.path.isfile(fileh):
           print('\n \033[1;33mWARNING: Log file for this date does not exist -> skipped! \033[1;37m')
           # Time = list(range(48))
           # TPH  = np.zeros((48,3))
           Time = [0]
           TPH  = np.zeros((1,3))
    else:
           # if the file exists open 
            fo = open(fileh, "r")
      
            temp  = fo.readlines()
            
            # dataList2 = temp[0]
            
            dataList = temp[fileHeader:]
            
            Nl   = len(dataList)
            Time = []
            TPH  = np.zeros((Nl,3))
            for ll in range(Nl): 
                temp = dataList[ll].split()
                Time.append(temp[0])
                TPH[ll,:] = np.float64(temp[1:4])
    
            fo.close()
            
    return Time, TPH