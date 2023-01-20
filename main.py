import json
import datetime
import base64

def getUUID(s):
  return s.split('uuid:', 1)[1].split(',', 1)[0]
  

with open('./data/data.json', 'r') as inputfile:
  input_object = json.load(inputfile)

current_time = datetime.datetime.now()
current_unix = int(datetime.datetime.timestamp(current_time))

value_sum = 0
uuid_array = []

for device in input_object['Devices']:
  if current_unix <= int(device['timestamp']):
    value_sum += int.from_bytes(base64.b64decode(device['value']), 'big')
    uuid = getUUID(device['Info'])
    uuid_array.append(uuid)

output_dictionary = {
  "ValueTotal": value_sum,
  "UUIDS": uuid_array
}

json_object = json.dumps(output_dictionary, indent=4)

with open('./output/result.json', 'w') as outputfile:
  outputfile.write(json_object)
    