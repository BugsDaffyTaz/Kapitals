import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

\
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Temperature (°C)": [30, 32, 31, 29, 28, 42, 32],
    "Humidity (%)": [70, 65, 68, 72, 75, 80, 65],
    "Wind Speed (m/s)": [5.1, 3.4, 4.2, 2.8, 3.6, 4.1, 3.8]
}

climate_data = pd.DataFrame(data)


temp_array = np.array(climate_data["Temperature (°C)"])
humidity_array = np.array(climate_data["Humidity (%)"])
wind_speed_array = np.array(climate_data["Wind Speed (m/s)"])


avg_temp = np.mean(temp_array)
min_temp = np.min(temp_array)
max_temp = np.max(temp_array)

avg_humidity = np.mean(humidity_array)
min_humidity = np.min(humidity_array)
max_humidity = np.max(humidity_array)

avg_wind_speed = np.mean(wind_speed_array)
max_wind_speed = np.max(wind_speed_array)
min_wind_speed = np.min(wind_speed_array)

print("Climate Data Statistics:")
print(f"Average Temperature: {avg_temp:.2f}°C, Min: {min_temp}°C, Max: {max_temp}°C")
print(f"Average Humidity: {avg_humidity:.2f}%, Min: {min_humidity}%, Max: {max_humidity}%\n")
print(f"Average Wind Speed: {avg_wind_speed:.2f} m/s")
print(f"Max Wind Speed: {max_wind_speed:.2f} m/s, Min Wind Speed: {min_wind_speed:.2f} m/s\n")


print("Climate Data:")
print(climate_data)


plt.figure(figsize=(14, 7))

plt.plot(climate_data["Day"], climate_data["Temperature (°C)"], label="Temperature (°C)", marker="s", color="pink")
plt.plot(climate_data["Day"], climate_data["Humidity (%)"], label="Humidity (%)", marker="o", color="green")


plt.title("Temperature and Humidity over a week in Mumbai")
plt.xlabel("Day")
plt.ylabel("Values")
plt.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 7))

plt.bar(climate_data["Day"], climate_data["Wind Speed (m/s)"], color="purple", alpha=0.7, label="Wind Speed (m/s)")

plt.title("Wind Speed Over the Week")
plt.xlabel("Day")
plt.ylabel("Wind Speed (m/s)")
plt.legend()
plt.grid(axis="y")
plt.tight_layout()
plt.show()