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
except:
	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)
 
gpsd = None
 
os.system('clear') 
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE)
    self.current_value = None
    self.running = True 
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next()
 
if __name__ == '__main__':
  gpsp = GpsPoller()
  try:
    gpsp.start()
    while True:
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
	url = "<Your HTTP Server>" + parameter
	response = urllib2.urlopen(url) 
      time.sleep(1) #set to whatever
 
  except (KeyboardInterrupt, SystemExit):
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join()
  print "Done.\nExiting."
