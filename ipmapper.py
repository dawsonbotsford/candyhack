"""
  Author: Dawson Botsford
  Date: 7/19/2014
  Purpose: Take inputted URL and return lat/longg
  Creds: github help from @mossberg
       http://stackoverflow.com/questions/4913349/havermath.sine-formula-in-python-bearing-and-distance-between-two-gps-points
"""
import sys
import socket
import subprocess
import math

#Havermath.sine estimation between two points in km
def get_dist(point1, point2):
  list1 = point1.split(',')   
  list2 = point2.split(',')   
# return point1
  lat1 = float(list1[0])
  long1 = float(list1[1])
  lat2 = float(list2[0])
  long2 = float(list2[1])
#convert decimal degrees to radians
  long1, lat1, long2, lat2 = map(math.radians, [long1, lat1, long2, lat2]) 
  print 'lat1: ' + str(lat1)
  print 'long1: ' + str(long1)
  print 'lat2: ' + str(lat2)
  print 'long2: ' + str(long2 )
  #haversine formula 
  dlong = long2 - long1 
  dlat = lat2 - lat1 
  a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlong/2)**2
#  c = 2 * math.asin(math.sqrt(a)) 
  c = 2 * math.atan2( math.sqrt(a), math.sqrt(1-a) ) 
  # 6367 km is the radius of the Earth
  km = 6367 * c
  return km  

#Get the lat/long from the ip
def get_loc(ip):
  cmd = 'curl -s ipinfo.io/' + ip + '/loc'
  proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
  (out, err) = proc.communicate()
  return out

#Get the lat/long for current network
def get_home_loc():
  cmd = 'curl -s ipinfo.io/loc'
  proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
  (out, err) = proc.communicate()
  return out

def main():
  if len(sys.argv) != 2:
       print "ERROR: please input 1 URL"
       return
 
  #User inputted one URL 
  url = sys.argv[1]
  ip = socket.gethostbyname(url)
  
  #Print distances 
  print 'distance from (' + get_loc(ip).rstrip() + ') to (' + get_home_loc().rstrip() + ') in km'
  distkm =  get_dist(get_loc(ip), get_home_loc()) 
  distmi = distkm * 0.621371
  print str(distkm) + ' km'
  print str(distmi) + ' mi'

main()
