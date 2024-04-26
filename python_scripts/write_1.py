import influxdb_client
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from time import sleep
import random as rand

import RPi.GPIO as GPIO
#For GPIO pin number
pin = 17
HIGH = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN)
print("Running")
bucket = "suresh"
org = "BVP"
token = "FOxPmFk6mKxzuqlWUC5AKwWZzXl1L8LIQ3wFhqL2l3DAMrSxPkAoB11vkfpijHGzhtDCZY4tsd3pvGxOjQFGMA"

url = "http://192.168.146.69:8000"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

write_api =  client.write_api(write_options = SYNCHRONOUS)

while(True):
    output = GPIO.input(pin)
    point = (
        influxdb_client.Point("sensors")
        .tag("username","suresh")
        .field("Loudness", 1 if output == GPIO.HIGH else 0)
    )
    write_api.write(bucket=bucket,org=org,record = point)
    sleep(1)
