from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/3817572.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and precipitation levels.
dates, prcp_readings = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        prcp_reading = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}.")
    else:
        dates.append(current_date)
        prcp_readings.append(prcp_reading)

# Plot the precipitation levels.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcp_readings, color='blue')

# Format plot.
ax.set_title("Daily Precipitation Levels in Severn Maryland, January 2 - October 2 2024", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()