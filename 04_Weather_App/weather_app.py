import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

data = response.json()

temperature = data['current_condition'][0]['temp_C']
humidity = data['current_condition'][0]['humidity']
condition = data['current_condition'][0]['weatherDesc'][0]['value']

print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Condition: {condition}")