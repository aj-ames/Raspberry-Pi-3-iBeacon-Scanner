#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0
 
import os
from gps import *
from time import *
import time
import threading

# BLE Scanner Package Import
import blescan
import sys
import bluetooth._bluetooth as bluez
import urllib2

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)
 
gpsd = None #seting the global variable
 
os.system('clear') #clear the terminal (optional)
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:
      #It may take a second or two to get good data
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
 
      os.system('clear')
      print "--------------------------------------------------"
      print "Status : Beacon Device Detecting...."
      print "--------------------------------------------------"
      returnedList = blescan.parse_events(sock, 2)
      os.system('clear')
      print "--------------------------------------------------"
      print "Status : Device Detected!"
      print "--------------------------------------------------"
      time.sleep(1)
      os.system('clear')
      print "--------------------------------------------------"
      print "Status : Send To Server...."
      print "--------------------------------------------------"

      for beacon in returnedList:
	parameter = beacon + ',' + str(gpsd.fix.latitude) + ',' + str(gpsd.fix.longitude)
	print parameter
	url = "http://172.17.19.24:8082/Silla_Server/op/beacon?data=" + parameter
	response = urllib2.urlopen(url) 
      time.sleep(1) #set to whatever
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
