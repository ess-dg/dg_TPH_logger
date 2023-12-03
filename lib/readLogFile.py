#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 12/2023

@author: francescopiscitelli
"""
###############################################################################
###############################################################################
########    TPH logger for sensor MS8607_02BA file reader for Arduino  ######## 
########    V2.0  2023/12/03      francescopiscitelli                  ########
###############################################################################
###############################################################################

import numpy as np
import os

###############################################################################
###############################################################################

# path = '/Users/francescopiscitelli/Documents/PYTHON/TPH_Logger/TPH_logger_Utgard/LogFiles/'

# fileName = 'Utgard_TPHlog_2021-02-095.txt'

# fileHeader = 2

###############################################################################
###############################################################################

def readLogFile (path,fileName,fileHeader=2,Ncols=6):


# for k in [0]:
    
    fileh = path+fileName
    
    if not os.path.isfile(fileh):
           # print('\n \033[1;33mWARNING: Log file for this date does not exist -> skipped! \033[1;37m')
           flag = -1
           TPH  = np.array([])
           Time = []
           
    else:
            flag = 0
           # if the file exists open 
            fo = open(fileh, "r")
      
            temp  = fo.readlines()
            
            # dataList2 = temp[0]
            
            dataList = temp[fileHeader:]
            
            Nl   = len(dataList)
            Time = []
            TPH  = np.zeros((Nl,Ncols))
            for ll in range(Nl): 
                temp = dataList[ll].split()
                Time.append(temp[0])
                TPH[ll,:] = np.float64(temp[1:Ncols+1])
    
            fo.close()
            
    return Time, TPH, flag