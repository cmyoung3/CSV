import matplotlib.pyplot as plt
import csv
from os import write
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

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
        high = int(x[4],)
        low = int(x[5])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs.append(int(x[4]))
        lows.append(int(x[5]))
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


plt.subplot(2,1,1)
plt.plot(dates,highs,c="red")
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates,lows,c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()
'''