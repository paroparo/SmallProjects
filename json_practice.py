import json

test_string = '''
{
    "people" : [
        {
            "name": "name_a",
            "phone": "111-111-1111",
            "email": "test@email",
            "license": false
        },
        {
            "name": "name_b",
            "phone": "222-222-2222",
            "email": "test2@email",
            "license": true
        }
    ]
}
'''

data = json.loads(test_string)

# print(data)
# print(data['people'])
for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

