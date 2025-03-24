import requests
url = 'http://api.weatherapi.com/v1/current.json?key=994ef3960e6842ddbf503013252403&q=53042&aqi=no'
response = requests.get(url)
weather_json = response.json()

print(weather_json)

temp = weather_json.get('current').get('temp_f')
condition = weather_json.get('current').get('condition').get('text')


print("today's weather is", condition, "with a temperature of", temp, "F")


