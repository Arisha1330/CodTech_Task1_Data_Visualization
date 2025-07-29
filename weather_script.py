import requests
import seaborn as sns
import matplotlib.pyplot as plt

API_KEY = "your_API_Key_here"  # Replace this
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

cities = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"]
temperatures = []

for city in cities:
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)

    print(response.status_code, response.json())
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        temperatures.append(temp)
        print(f"{city}: {temp}°C")
    else:
        print(f"❌ Failed to get data for {city}: {response.status_code}")
        temperatures.append(0)  # or skip appending if you prefer

# Plot

sns.set(style="whitegrid")

# Create a simple DataFrame to use hue (Seaborn prefers this style)
import pandas as pd
df = pd.DataFrame({
    'City': cities,
    'Temperature': temperatures
})

sns.barplot(data=df, x='City', y='Temperature', hue='City', palette='coolwarm', legend=False)
plt.title("Temperature in Indian Cities")
plt.ylabel("Temperature (°C)")
plt.xlabel("City")
plt.show()
