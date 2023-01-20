import json
from datetime import datetime
from base64 import b64decode
import os
from sys import exit

def getUUID(s):
  return s.split('uuid:', 1)[1].split(',', 1)[0]
  
input_path = './data/data.json'
if os.path.isfile(input_path) == False:
  exit('No input file found')
with open(input_path, 'r') as inputfile:
  input_object = json.load(inputfile)

current_time = datetime.now()
current_unix = int(datetime.timestamp(current_time))

value_sum = 0
uuid_array = []

for device in input_object['Devices']:
  if current_unix <= int(device['timestamp']):
    value_sum += int.from_bytes(b64decode(device['value']), 'big')
    uuid = getUUID(device['Info'])
    uuid_array.append(uuid)

output_dictionary = {
  "ValueTotal": value_sum,
  "UUIDS": uuid_array
}

json_object = json.dumps(output_dictionary, indent=4)

with open('./output/result.json', 'w') as outputfile:
  outputfile.write(json_object)
    