#! /usr/bin/env python

#import OneWire
import config
import Adafruit_DHT
from gpiozero import LightSensor, MCP3008


# Functions for getting weather data from sensors

def read_temperature():
  sensor = Adafruit_DHT.DHT22
  #pin = 4
  humidity_raw, temperature_raw = Adafruit_DHT.read_retry(sensor, temperature_pin)
  if humidity_raw is not None and temperature_raw is not None:
    # Convert to F from C and drop excess after decimal
    temperature_new = round(temperature_raw * 1.8 + 32, 1) # Convert to farenheit then round value to 1 decimal place
    humidity_new = round(humidity_raw, 1) # Round value to 1 decimal place
  else:
    print('Failed to get reading from DHT22. Using previous readings.')
  return (humidity_new, temperature_new)

def read_light():
  #ldr = LightSensor(light_pin)  # alter if using a different pin
  for x in range (10):
    ldr = MCP3008(7)
    print (ldr.value)
    
  return (ldr)

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
