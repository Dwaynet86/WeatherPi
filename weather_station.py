#! /usr/bin/env python

# Written by Dwayne Truex June 2019
# Written for PiZeroW
# Contact: dwaynetruex@yahoo.com

# This program was designed to read
# multiple inputs for the purpose of 
# monitoring and recording weather data

# Main program for weather monitoring

# Import any needed files

from config import *  #Import configuration file
from time import sleep # Import sleep Module for timing
import RPi.GPIO as GPIO
import pymysql # Import py to mysql connector

# Setup GPIO Pins 

GPIO.setmode(GPIO.BCM)  # Configures how we are describing our pin numbering
GPIO.setwarnings(False)  # Disable Warnings



# define variables
temperature = 0
humidity = 0
pressure = 0
wind_speed = 0
wind_direction = "N"
rain_drops = 0
luminance = 0


def read_sensors():
  temperature
  humidity
  pressure
  wind_speed
  wind_direction
  rain_drops
  luminance
  
  return

  
def store_readings():
  # Create a timestamp and store all readings on the MySQL database
  
  conn, curs = open_database_connection()
  # curs.execute("INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);")
  
  curs.execute("INSERT INTO weather_data (temperature, humidity, wind_speed, wind_direction, pressure, luminance) VALUES (temperature, humidity, wind_speed, wind_direction, pressure, luminance);")
  
  # Verify 
  #curs.execute("SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 1;")
  
  
  close_database_connection(conn, curs)
  return
  
def open_database_connection():
  conn = pymysql.connect(db_host, db_user, db_password, db_name)
  curs = conn.cursor()
  curs.execute("SET sql_notes = 0; ")  # Hide Warnings

  return conn, curs

def close_database_connection(conn, curs):

    curs.execute("SET sql_notes = 1; ")
    conn.commit()
    conn.close()


def create_database():

    conn = pymysql.connect(db_host, db_user, db_password)
    curs = conn.cursor()
    curs.execute("SET sql_notes = 0; ")  # Hide Warnings

    curs.execute("CREATE DATABASE IF NOT EXISTS {}".format(db_name))

    curs.execute("SET sql_notes = 1; ")  # Show Warnings
    conn.commit()
    
    #curs = conn.cursor()
    #curs.execute()
    # Try to connect to table 
    
    conn.close()
    return
    
# First run check if database exsists    
create_database()

#Main Loop
while True: # Loop Continuously
    
    read_sensors() # poll sensor data
    store_readings() # store data from sensors
    
    sleep(10)
