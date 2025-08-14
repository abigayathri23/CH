import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
df = pd.read_csv('weather_data.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

if 'temp_max' in df.columns and 'temp_min' in df.columns:
    df['Temperature'] = (df['temp_max'] + df['temp_min']) / 2
    print(df['Temperature'].mean())

if 'date' in df.columns and 'Temperature' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    plt.figure(figsize=(10, 5))
    plt.plot(df['Temperature'], color='blue')
    plt.title('Average Temperature Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("temperature_plot.png")
    plt.show()

if 'wind' in df.columns:
    plt.figure(figsize=(10, 5))
    plt.plot(df['wind'], color='green')
    plt.title('Wind Speed Over Time')
    plt.xlabel('Index')
    plt.ylabel('Wind Speed')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("wind_plot.png")
    plt.show()