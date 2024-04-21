import influxdb_client
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

# Query script
query_api = client.query_api()

query = 'from(bucket:"sensors")\
|> range(start: -30d)\
|> filter(fn:(r) => r._measurement == "sensors")\
|> filter(fn:(r) => r.location == "Prague")\
|> filter(fn:(r) => r._field == "temperature")'

result = query_api.query(org=org, query=query)
sensors = {'temperature':[]}
for table in result:
    for record in table.records:
        sensors['temperature'].append((record.get_time(), record.get_value()))

for i in sensors['temperature']:
    print(i[0], i[1])
# print(results)
# print(result)
# print(result[0].records)
# print(result[0].records[0].values)
# utc_time = result[0].records[0].get_time()
# print(utc_time)

# The Flux object provides the following methods for accessing your data:

# get_measurement(): Returns the measurement name of the record.
# get_field(): Returns the field name.
# get_value(): Returns the actual field value.
# values: Returns a map of column values.
# values.get("<your tag>"): Returns a value from the record for given column.
# get_time(): Returns the time of the record.
# get_start(): Returns the inclusive lower time bound of all records in the current table.
# get_stop(): Returns the exclusive upper time bound of all records in the current table.