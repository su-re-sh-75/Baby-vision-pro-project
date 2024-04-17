import influxdb_client
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "store_sample"
org = "BabyMonitoringApp"
token = "RrvK5MU_w3I9fCn6VbEDlPc5DMVz-SKGfRKIwHFPAxkd-D-Wl8B__GudbqHh_ZkxBgEIjAjj0jaY7j8tZyKEtQ=="

url = "http://192.168.143.69:7000"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

query_api =  client.query_api()

query = """
from(bucket:"store_sample") 
|> range(start:-30d)
|> group(columns: ["_time", "_measurement"])
"""

tables = query_api.query(query,org=org)
print(tables)
for table in tables:
    for row in table:
        print(row["_measurement"],row["_field"],row["_value"])
        


