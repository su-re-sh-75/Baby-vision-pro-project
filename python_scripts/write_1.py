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
bucket = "PiData"
org = "BabyMonitoringApp"
token = "RrvK5MU_w3I9fCn6VbEDlPc5DMVz-SKGfRKIwHFPAxkd-D-Wl8B__GudbqHh_ZkxBgEIjAjj0jaY7j8tZyKEtQ=="

url = "http://192.168.146.69:8000"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

write_api =  client.write_api(write_options = SYNCHRONOUS)

MOISTURE = 90 
TEMPERATURE = 30
LOUDNESS = 0
MOVEMENT = 1
while(True):
    output = GPIO.input(pin)
    point = (
        influxdb_client.Point("PI_TEST")
        .tag("PI","0")
        .field("Loudness", 1 if output == GPIO.HIGH else 0)
    )
    write_api.write(bucket=bucket,org=org,record = point)
    sleep(1)