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
from read_sensors import * # Import all sensor functions
from time import sleep # Import sleep from time Module 
import datetime # Import time
import RPi.GPIO as GPIO
import pymysql # Import py to mysql connector
from sys import exit

# Setup GPIO Pins 

GPIO.setmode(GPIO.BCM)  # Configures how we are describing our pin numbering
GPIO.setwarnings(False)  # Disable Warnings



# define variables
reading_date = "01/01/0000"
reading_time = "00:00"
temperature = 0
humidity = 0
pressure = 0
wind_speed = 0
wind_direction = "N"
rain_drops = 0
luminance = 0
last_reading = "00:00"



  
def store_readings():
  # Create a timestamp and store all readings on the MySQL database
  
  conn, curs = open_database_connection()
  try:   
    curs.execute("INSERT INTO weather_data "
               "(reading_date, reading_time, temperature, humidity, wind_speed, wind_direction, pressure, luminance)"
               " VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');"
               .format(reading_date, reading_time, temperature, humidity, wind_speed, wind_direction, pressure, luminance))
  
  except Exception as ex:
    print ("Error storing readings: {}".format(ex))
    
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
    # First check if database exists if not then create and populate
    try:  # Try to open connection to mysql server
      conn = pymysql.connect(db_host, db_user, db_password) # Open the connection
      curs = conn.cursor()
      curs.execute("SET sql_notes = 0; ")  # Hide Warnings
      
      print ("Connection established...") # Connection established let user know and keep going
            
      try: # Connection open, verify database exisists
        result = curs.execute("SHOW DATABASES LIKE '{}';".format(db_name))
        #result = curs.execute("SELECT schema_name FROM information_schema.schemata;")
        #print ("Found {} Databases".format(result))
        
        #if result:  # Show that the database does exsist
          #print ("Found database {}".format(db_name))
        if not result:
          print ("Database not found... Creating database {} now".format(db_name))
          curs.execute("CREATE DATABASE IF NOT EXISTS {}".format(db_name))          
      except Exception as ex: # Database does not exist lets create it
        print ("Error creating database: {}".format(ex))
      
     
      # Were done close the connection
      curs.execute("SET sql_notes = 1; ")  # Show Warnings
      conn.commit() 
      conn.close()
      #print ("Connection closed...")
    except Exception as ex:    
      print ("Error verifying database: {}".format(ex))      

      
def create_table():
   # Check if tables exist if not create them
      try: 
        result = curs.execute("SHOW TABLES FROM {} LIKE 'weather_data';".format(db_name))
      
        if result <> 0: # Table exists 	        
          #print ("Found exsiting table..")
          return
        else: # Table does not exist 
          #print ("Building table")
          curs.execute("CREATE TABLE {}.weather_data "
               "(id INT(11) UNSIGNED AUTO_INCREMENT, PRIMARY KEY (id),"
               " timestamp TIMESTAMP NOT NULL,"
               " reading_date DATE NOT NULL,"
               " reading_time TIME NOT NULL,"
               " temperature DECIMAL(3,1) NOT NULL,"
               " humidity DECIMAL(3,1) NOT NULL,"
               " wind_speed INT(3) NOT NULL,"
               " wind_direction VARCHAR(3) NOT NULL,"
               " pressure INT(3) NOT NULL,"
               " luminance INT(3) NOT NULL);".format(db_name))
  
          print ("Created table weather_data")
      except Exception as ex:
        print ("Error creating table: {}".format(ex))
        
        
def create_settings_table():
  # Create a table to store settings changes
  try:
    result = curs.execute("SHOW TABLES FROM {} LIKE 'settings';".format(db_name))
    
    if result <> 0: # Table exists 
          #print ("Found exsiting table..")
        return
    else:
     curs.execute("CREATE TABLE {}.settings "
                  "(setting_name VARCHAR(25) NOT NULL,"
                  " setting_value VARCHAR(25) NOT NULL,"
                  " setting_descrption VARCHAR(255) NOT NULL,"
                  " PRIMARY KEY (setting_name);".format(db_name))
     # Add default setting data
      
      
      
     print ("Created table settings")
  except Exception as ex:
      print ("Error creating table: {}".format(ex))
      
      
create_database()     
conn, curs = open_database_connection()
create_table()
#create_settings_table()
close_database_connection(conn, curs)

print ("Weather Station started succesfully... Begin collecting data ")
loop = read_interval
#Main Loop
while True: # Loop Continuously
    sleep(1)
    if loop == read_interval:
      loop = 0
      localtime = datetime.datetime.now()
      # %Y = YYYY %m = Month(mm) %d = Day(dd)
      reading_date = "{}-{}-{}".format(localtime.strftime("%Y"), localtime.strftime("%m"), localtime.strftime("%d"))
      reading_time = localtime.strftime("%X")

      humidity, temperature = read_temperature(temperature_pin)
      luminance = read_adc(adc_light_pin)
      store_readings() # store data from sensors
      print("Storing Data"),
      print (reading_date, reading_time, temperature, humidity, wind_speed, wind_direction, pressure, luminance)
    
    loop += 1
    
    
    
print ("Exiting...")
exit()
