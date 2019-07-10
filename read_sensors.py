#! /usr/bin/env python

#import OneWire
import Adafruit_DHT



# Functions for getting weather data from sensors

def read_temperature():
  sensor = Adafruit_DHT.DHT22
  pin = 4
  humidity_raw, temperature_raw = Adafruit_DHT.read_retry(sensor, pin)
  if humidity_raw is not None and temperature_raw is not None:
    # Convert to F from C
    temperature_new = temperature_raw * 1.8 + 32
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature_raw, humidity_raw))
    print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature_new, humidity_new))
  else:
    print('Failed to get reading from DHT22. Using previous readings.')
  return
  
def read_wind():
 # wind speed
  # wind_direction = read.direction()
  return
  
def read_precipitation():
  # is_raining = read.()
  # rain_drops = 
  return
  
def read_air_quality():
  # air_quality  = read.()
  
  return
