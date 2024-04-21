import influxdb_client, time
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "sensors"
org = "BVP"
token = "FOxPmFk6mKxzuqlWUC5AKwWZzXl1L8LIQ3wFhqL2l3DAMrSxPkAoB11vkfpijHGzhtDCZY4tsd3pvGxOjQFGMA=="
url="http://localhost:8086"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)
for i in range(10):
    p = influxdb_client.Point("sensors").field("temperature", (25.3 + i) * (i + 1))
    write_api.write(bucket=bucket, org=org, record=p)
    time.sleep(10)
