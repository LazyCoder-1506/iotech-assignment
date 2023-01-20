# IOTech Systems Exercise 02 Submission - Pranayan Metiya

## [Task](https://github.com/IOTechSystems/exercises)
- Parse the data from `data/data.json`
- Discard the devices where the `timestamp` value is before the current time. The timestamps are in `UNIX` format
- Get the total of all `value` entries, values are `base64` strings containing integer values
- Parse the uuid from the `info` field of each entry
- Output the values total and the list of uuids in the format described by the JSON schema. Write this data to a file

## Setup
1. Clone the repository using `git clone https://github.com/LazyCoder-1506/iotech-assignment.git`
2. Navigate to the root folder. This should be the same folder that contains `main.py` file
3. Run `python3 main.py`. If this does not work, try `python main.py`. The results will be contained in `output/result.json`

### Note
- To test with different set of input, modify the file `data/data.json`
- Python v3 should be available. I haven't tested the code on Python v2