from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path_sitka = Path('weather_data/sitka_weather_2021_full.csv')
lines_sitka = path_sitka.read_text().splitlines()

reader_sitka = csv.reader(lines_sitka)
header_row_sitka = next(reader_sitka)

path_valley = Path('weather_data/death_valley_2021_full.csv')
lines_valley = path_valley.read_text().splitlines()

reader_valley = csv.reader(lines_valley)
header_row_valley = next(reader_valley)


dates, temp_high_sitka, temp_high_valley = [], [], []
for row in reader_sitka:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        temp = int(row[7])
    except ValueError:
        print(f"No data for {current_date}.")
    else:
        dates.append(current_date)
        temp_high_sitka.append(temp)


    print(temp_high_sitka)

for row in reader_valley:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        temp = int(row[6])
    except ValueError:
        print(f"No data for {current_date}.")
    else:
        temp_high_valley.append(temp)


    print(temp_high_valley)


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, temp_high_sitka, color='blue', alpha= .5)
ax.plot(dates, temp_high_valley, color='red', alpha=.5, label='Death Valley')

ax.set_title("High temp. Sitka vs Valley", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature', fontsize=16)
ax.tick_params(labelsize=16)
plt.show()