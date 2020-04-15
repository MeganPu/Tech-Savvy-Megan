import urllib.request
import json
import pprint

APIKEY = 'b05f16d2a80cb31bdf8dff023a23f661'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint.pprint(response_data)

print(type('main'))
pprint.pprint(response_data['main'])
print(response_data['main']['temp'])



