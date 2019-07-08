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
from sys import exit

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
    # First check if database exsists if not then create and populate
    try:  # Try to open connection to mysql server
      print ("Connecting to server...")
      
      conn = pymysql.connect(db_host, db_user, db_password) # Open the connection
      curs = conn.cursor()
      curs.execute("SET sql_notes = 0; ")  # Hide Warnings
      
      print ("Connection established...") # Connection established let user know and keep going
      print ("Verifying database {} exsists...".format(db_name))  # Check if db_name is real database
      
      try: # Connection open verify database exisists
        result = curs.execute("SHOW DATABASES LIKE '{}';".format(db_name))
        #result = curs.execute("SELECT schema_name FROM information_schema.schemata;")
        #print ("Found {} Databases".format(result
        if result:  # Show that the database does exsist
          print ("Found database {}".format(db_name))
    
     # Were done close the connection
     curs.execute("SET sql_notes = 1; ")  # Show Warnings
     conn.commit() 
     conn.close()
     print ("Connection closed...")
        
      except: # Database does not exsist lets create it
        print ("Database not found... Creating database {} now".format(db_name))
        curs.execute("CREATE DATABASE IF NOT EXISTS {}".format(db_name))
    except:    
      print ("Connection failed... Check credentials in config file and try again.")      
      
      
create_database()     

print ("Quiting...Before entering loop")
exit()

#Main Loop
while True: # Loop Continuously
    
    #read_sensors() # poll sensor data
    #store_readings() # store data from sensors
    print ("sleeping.....")
    sleep(10)
