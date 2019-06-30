# Main program for weather monitoring

# Import any needed files

from config import *
from time import sleep # Import sleep Module for timing


# define 

def read_sensors():
  # read temp
  
  # read hum
  
def store_readings():
  # store readings in db for history
  
def open_db  

#Main Loop
while True: # Loop Continuously
    
    read_sensors() # poll sensor data
    store_readings() # store data from sensors
    
    sleep(10)
