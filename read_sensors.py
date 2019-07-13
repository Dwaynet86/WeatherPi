#! /usr/bin/env python

#import OneWire
#import config
import Adafruit_DHT
from gpiozero import LightSensor, MCP3008


# Functions for getting weather data from sensors

def read_temperature(pin):
  sensor = Adafruit_DHT.DHT22
  #pin = 4
  humidity_raw, temperature_raw = Adafruit_DHT.read_retry(sensor, pin)
  if humidity_raw is not None and temperature_raw is not None:
    # Convert to F from C and drop excess after decimal
    temperature_new = round(temperature_raw * 1.8 + 32, 1) # Convert to farenheit then round value to 1 decimal place
    humidity_new = round(humidity_raw, 1) # Round value to 1 decimal place
  else:
    print('Failed to get reading from DHT22. Using previous readings.')
  return (humidity_new, temperature_new)



def read_adc(pin):
  #ldr = LightSensor(light_pin)  # alter if using a different pin
  
  ldr = MCP3008(channel = pin)
  print ("reading pin {}: {}" .format(pin, ldr.value))
  print (ldr.raw_value)
  
  
  
  
  return (ldr.raw_value)


  
def read_air_quality():
  # air_quality  = read.()
  
  return
