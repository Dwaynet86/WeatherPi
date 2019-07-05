# Store all configuration settings here

# Database credentials

db_user     = "weathermonitor"
db_password = "weather"
db_name     = "weather"
db_host     = "localhost"


# User Options

read_interval = 300  # Sensor Read Interval Time in Seconds 300 = 5 minutes
outputpins = [22, 23, 24, 25]  # Specifiy a RPi GPIO Pin for each relay
