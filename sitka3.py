import matplotlib.pyplot as plt
import csv
from os import write
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

    #testing to convert date from string
mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')

print(mydate)

dates = []

#for row in csv_file:
#    dates.append(datetime(int(row[2])))

#print(dates)

highs = []
lows = []

#x stands for rows in the csv
for x in csv_file:
    highs.append(int(x[5]))
    the_date = datetime.strptime((x[2]), '%Y-%m-%d')
    dates.append(the_date)
    lows.append(int(x[6]))

#print(highs)
#print(dates)
print(lows)

fig = plt.figure()

plt.title("Daily Temperatures, July 2018", fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature",fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.plot(dates, highs, c="red", alpha=.5)
plt.plot(dates, lows, c="blue", alpha =.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=.1)


fig.autofmt_xdate()

plt.show()
