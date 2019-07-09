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
from time import sleep # Import sleep from time Module 
import datetime # Import time
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
  try:
    localtime = datetime.datetime.now()
    
    reading_date = localtime.strftime("%x")
    reading_time = localtime.strftime("%X")
    
    print ("{} {}".format(reading_time, reading_date))
    
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
        
        if result:  # Show that the database does exsist
          print ("Found database {}".format(db_name))
        elif not result:
          print ("Database not found... Creating database {} now".format(db_name))
          curs.execute("CREATE DATABASE IF NOT EXISTS {}".format(db_name))          
      except Exception as ex: # Database does not exsist lets create it
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
          print ("Found exsiting data..")
        else:
          print ("Building tables")
          curs.execute("CREATE TABLE {}.weather_data "
               "(id INT(11) UNSIGNED AUTO_INCREMENT, PRIMARY KEY (id),"
               " timestamp TIMESTAMP NOT NULL,"
               " reading_date DATE NOT NULL,"
               " reading_time TIME NOT NULL,"
               " temperature INT(3) NOT NULL,"
               " humidity INT(2) NOT NULL,"
               " wind_speed INT(3) NOT NULL,"
               " wind_direction INT(3) NOT NULL,"
               " pressure INT(3) NOT NULL,"
               " luminance INT(3) NOT NULL);".format(db_name))
  
          print ("Created table weather_data")
      except Exception as ex:
        print ("Error creating table: {}".format(ex))
      
     
      
create_database()     
conn, curs = open_database_connection()
create_table()
close_database_connection(conn, curs)

print ("Weather Station started... Begin sensor reading ")
loop = 0
#Main Loop
while True: # Loop Continuously
    
    #read_sensors() # poll sensor data
    store_readings() # store data from sensors
    loop += 1
    if loop == 10: break
    #print ("Reading sensors {}".format(loop))
    sleep(1)
    
print ("Exiting...")
exit()
