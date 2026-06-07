from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, prcp = [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        precip = float(row[5])
    except ValueError:
        print(f"No data for {current_date}.")
    else:
        dates.append(current_date)
        prcp.append(precip)


    print(prcp)

for index, column_header in enumerate(header_row):
    print(index, column_header)
print(header_row)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcp, color='blue', alpha= .5)

ax.set_title("MM rain per day - 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('MM fall', fontsize=16)
ax.tick_params(labelsize=16)
plt.show()