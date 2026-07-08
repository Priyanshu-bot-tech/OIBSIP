import requests

api_key = 'afd3e50b2e3bb0204772bf70f0c53f6c'

location_input=input("Enter a location(city or pin code):")

if location_input.strip() == '':
    print('Error: Location cannot be empty.')
    exit()

# print("Fetching weather data for", location_input)

try:
    weather_data= requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location_input}&appid={api_key}&units=metric', timeout=6)
except requests.exceptions.Timeout:
    print('Error: Request timed out. Check your internet connection.')
    exit()
except requests.exceptions.ConnectionError:
    print('Error: Could not connect. Check your internet connection.')
    exit()

if weather_data.status_code == 401:
    print('Error: Invalid API key.')
    exit()

# print(weather_data.status_code)

# print(weather_data.json())



if weather_data.json()['cod'] == '404':
    print('Invalid Location')
else:
    weather = weather_data.json()['weather'][0]['description']
    temperature = round(weather_data.json()['main']['temp'])
    cel_to_far= round((temperature*(9/5))+32)
    wind_speed= round(weather_data.json()['wind']['speed'])*3.6
    humidity= round(weather_data.json()['main']['humidity'])



    print('The weather in',location_input,'is',weather)
    print('The temperature in',location_input,'is',temperature,'Celcius or',cel_to_far,'Fahrenheit')
    print('The wind speed in',location_input,'is',wind_speed,'km/hr')
    print('The humidity in',location_input,'is',humidity,'%')