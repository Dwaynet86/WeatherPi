#! /usr/bin/env python

#import OneWire
import Adafruit_DHT



# Functions for getting weather data from sensors

def read_temperature():
  sensor = Adafruit_DHT.DHT22
  pin = 4
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  print (temperature, humidity)
  print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
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
