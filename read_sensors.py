#! /usr/bin/env python

#import OneWire
import Adafruit_DHT
from gpiozero import LightSensor


# Functions for getting weather data from sensors

def read_temperature():
  sensor = Adafruit_DHT.DHT22
  pin = 4
  humidity_raw, temperature_raw = Adafruit_DHT.read_retry(sensor, pin)
  if humidity_raw is not None and temperature_raw is not None:
    # Convert to F from C and drop excess after decimal
    temperature_new = round(temperature_raw * 1.8 + 32, 1)
    humidity_new = round(humidity_raw, 1)
    
    #print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature_new, humidity_new)) # for demo only
    
    
    
  else:
    print('Failed to get reading from DHT22. Using previous readings.')
  return (humidity_new, temperature_new)

def read_light():
  ldr = LightSensor(17)  # alter if using a different pin
  while True:
    print(ldr.value)
  
  
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
