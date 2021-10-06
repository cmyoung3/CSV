import matplotlib.pyplot as plt
import csv
from os import write
from datetime import datetime

sitka = open("sitka_weather_2018_simple.csv", "r")
dv = open("death_valley_2018_simple.csv", "r")


def sitka_weather(sitka):
    

    csv_file = csv.reader(open_file,delimiter=",")

    header_row = next(csv_file)

    print(type(header_row))

    for index, column_header in enumerate(header_row):
    print(index, column_header)



    dates = []

    #for row in csv_file:
    #    dates.append(datetime(int(row[2])))

    #print(dates)

    highs = []
    lows = []

#x stands for rows in the csv
for x in csv_file:
    try:
        the_date = datetime.strptime((x[2]), '%Y-%m-%d')
        high = int(x[5])
        low = int(x[6])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs.append(int(x[5]))
        lows.append(int(x[6]))
        dates.append(the_date)

  

#print(highs)
#print(dates)
#print(lows)

'''
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

'''

#(2,1,1) 2 rows, 1 column, 1 index (top graph)
plt.subplot(2,1,1)
plt.plot(dates, highs, c="red", alpha=.5)
plt.plot(dates, lows, c="blue", alpha =.5)
plt.title("SITKA AIRPORT, AK US")
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=.1)
open_file.close()


open_file = open("death_valley_2018_simple.csv", "r")
csv_file = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)


for x in csv_file:
    try:
        the_date = datetime.strptime((x[2]), '%Y-%m-%d')
        high = int(x[4])
        low = int(x[5])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs.append(int(x[4]))
        lows.append(int(x[5]))
        dates.append(the_date)

plt.subplot(2,1,2)
plt.plot(dates, highs, c="red", alpha=.5)
plt.plot(dates, lows, c="blue", alpha =.5)
plt.title("DEATH VALLEY, CA US")
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=.1)

plt.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US")

plt.show()
