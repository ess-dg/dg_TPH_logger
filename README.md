This code writes log files for Temp, Pressure and RH from sensor MS8607_02BA.

Contents: python scripts and subfolder.
- TPHlogger.py the script itself managing the log
- TPHdataPlotter.py a very simple plotting tool for the log files with sync option too 
- WatchMe.py a watchdog that reboots the raspberry if the logging is not happening anymore 
- lib/MS8607_02BA.py is the sensor reader
- lib/readLogFile.py a reader for the log files
- lib/syncUtil.py a py for a bash command rsync to sync the data from one computer to another 
- subfolder LogFiles/ where the log files are stored

Note: the WatchMe.py works based on the fact that both TPHlogger.py and WatchMe.py are added as cron jobs at reboot.
Cronttab -e add the following lines: 

    @reboot python /home/pi/dg_TPH_logger/TPHlogger.py
    @reboot python /home/pi/dg_TPH_logger/WatchMe.py

changing the path /home/pi according to your path where the logger folder is locagted. 

In the LogFiles folder there are two types of files:
Utgard_TPHlog_<current_date>_PowerFailure.txt 
Utgard_TPHlog_<current_date>.txt
The T, P, RH is logged in the Utgard_TPHlog_<current_date>.txt file every 30 minutes.  Every day at midnight a new file is created with the relative new date. This file has two header lines and 4 columns following with time, T, P, RH.

Credits:
https://github.com/anirudh-ramesh/MS8607-02BA01/blob/master/Python/MS8607_02BA.py