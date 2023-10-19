import requests
import json

# Get your IP address
ip = requests.get('https://api.ipify.org').text

# Get your location from your IP address
url = 'https://ipinfo.io/' + ip + '/json'
response = requests.get(url)
data = json.loads(response.content)

# Print your location
print('Your location is:', data['city'], data['region'], data['country'])
