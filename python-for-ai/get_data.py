import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Djibouti weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=11.58901&longitude=43.14503&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"

response = requests.get(url)
data = response.json()
print(data)


#-------------------------------


# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min'],
    'rainfall_mm': daily_data['precipitation_sum']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)

#-------------------------------

# Create the plot
plt.figure(figsize=(10, 6))

# Temperature lines
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp (°C)')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp (°C)')

plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Djibouti Weather - Past 7 Days')
plt.xticks(rotation=45)

# Second axis for rainfall
ax2 = plt.twinx()
ax2.bar(df['date'], df['rainfall_mm'], alpha=0.3, label='Rainfall (mm)')
ax2.set_ylabel('Rainfall (mm)')

plt.tight_layout()
plt.show()

import os

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/kampala_weather_with_rainfall.csv', index=False)
print("Data saved to data/kampala_weather_with_rainfall.csv")