import json


with open('states.json') as file:
    data = json.load(file)

# for state in data['states']:
#     print(state['name'], state['abbreviation'])

for state in data['states']:
    del state['area_codes']


with open('new_states.json', 'w') as new_file:
    json.dump(data, new_file, indent=2)



