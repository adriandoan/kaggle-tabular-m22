import csv
import pandas as pd

f = open('train.csv', 'r')
r = csv.reader(f)

newf = open('only_mondays_morning.csv', 'w')
writer = csv.writer(newf)

#april 29
#may 27
#july 22
#september 2

outliers = ["1991-04-29", "1991-05-27", "1991-07-22", "1991-09-02"]

for row in r:
    if row[0]!= "row_id": # and row[1].split(" ")[0] not in outliers:
        date = pd.Timestamp(row[1].split(" ")[0])
        dayname = date.day_name()
        time = row[1].split(" ")[1].split(":")[0]
        if dayname == "Monday" and 12 > int(time):
            writer.writerow(row)


newf.close()
f.close()
