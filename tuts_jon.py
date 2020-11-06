import json

data = '{"var1": "Harry","var2": "56"}'

parsed = json.loads(data)
print(parsed)

print(parsed['var1'])

data2 ={
    "channel_name": "code with harry",
    "cars": ['bmx','audi','maruti'],
    "fridge": ('roti','chicken'),
    "isbad": False
}

jcom = json.dumps(data2)
print(jcom)

# json.load()
# what is sort_key parameter in dumps