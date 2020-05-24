import json

data = {}
data['people'] = []

data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})

data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})

data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

# with open('output.json', mode='w') as outfile:
    # json.dump(data, outfile)

with open('output.json', mode='r') as json_file:
    file_data = json.load(json_file)
    print(file_data)
