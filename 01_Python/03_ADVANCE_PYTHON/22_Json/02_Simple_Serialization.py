# A Simple Serialization Example

import json

data = {
"president":{
"name": "Zaphod Beeblebrox",
"species": "Betelgeusian"
  }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)


# we could write it to a native Python str object.

json_string = json.dumps(data)

print(json_string)
