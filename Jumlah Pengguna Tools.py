import requests

api_visitor = 'https://api.api-ninjas.com/v1/counter?id=test_id&hit=true'
key_visitor = 'UTnxMDmQX2fBhcHugBBqXA==zudW593apWlxqRpK'

# Mengirim permintaan GET ke API
response = requests.get(api_visitor, headers={'X-Api-Key': key_visitor})

# Mengurai respons JSON
data = response.json()

# Menampilkan angka dari 'value'
print("data['value'])
