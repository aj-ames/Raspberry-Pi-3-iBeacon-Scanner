# Raspberry-Pi-3-iBeacon-Scanner

Because gps data and HTTP transport are required, This program need bluez, urllib, gpsd package.

You can get these package
<pre>
pip install bluez
pip install urllib
pip install gps
</pre>

Also, The program sends the measured data to your web server.

<pre>
  for beacon in returnedList:
  parameter = beacon + ',' + str(gpsd.fix.latitude) + ',' + str(gpsd.fix.longitude)
  print parameter
  url = [Your HTTP Server] + parameter
  response = urllib2.urlopen(url)
  time.sleep(1)
</pre>


You should replace url with [Your HTTP Server] with your web server address.

*****
This program refers to the original source at<br>
**BLE Scanner** : https://github.com/switchdoclabs/iBeacon-Scanner-/blob/master/testblescan.py
**GPSD** :http://www.danmandle.com/blog/getting-gpsd-to-work-with-python/

