import requests
import pandas as pd
import statistics

weather_api = "https://api.open-meteo.com/v1/forecast?latitude=50.4547&longitude=30.5238&hourly=temperature_2m,wind_speed_10m&timezone=auto"
response = requests.get(weather_api)
data = response.json()
print(data.keys())

dates = data['hourly']['time']
temperature = data['hourly']['temperature_2m']
wind_speed= data['hourly']['wind_speed_10m']


df = pd.DataFrame({
    'date': pd.to_datetime(dates),
    'temperature (°C)': temperature,
    'wind_speed': wind_speed,
})

print(df)


data = df.head(72) #обираємо наступні 3 дні з таблиці(72 години)
min_temp = float(data['temperature (°C)'].min())
max_temp = float(data['temperature (°C)'].max())
mean_temp = statistics.fmean(data['temperature (°C)'].tolist()) #перетворюємо на лист для знаходження середнього
print(f"Мінімальна температура за 3 дні: {min_temp} °C, максимальна тепература за 3 дні: {max_temp} °C, середня температура за 3 дні: {round(mean_temp)} °C")


def wind_estimation(df):
    mean_wind = statistics.fmean(df['wind_speed'].tolist())
    hours = df[df['wind_speed'] > mean_wind]
    return len(hours)
print(f"Кількість годин коли швидкість вітру перевищує загальну середню швидкість вітру: {wind_estimation(df)} год")