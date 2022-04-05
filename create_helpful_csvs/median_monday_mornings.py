import csv
import pandas as pd
import numpy as np

# create and add up each congestion that corresponds to each spot...(they line up)


# this is to create a blank submission file
f = open('monday_morning_medians.csv', 'w')

doit = csv.writer(f)

for i in range(846495, 848835):
    doit.writerow([i, 0])

f.close()


# get the list of lines
f = open('monday_morning_medians.csv', 'r')

r = csv.reader(f)
lines = list(r)

f.close()

# list of lists of all numbers to find median at the end
biglst = []
for i in range(0, 2340):
    biglst.append([])

# iterate through only_mondays and sum each corresponding congestion
totaldays = 0
idx = 0
with open('only_mondays_morning.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        congestion = pd.to_numeric(row[5])
        if idx == 2340:
            idx = 0
            biglst[idx].append(int(congestion))
            idx += 1
            totaldays += 1
        else:
            biglst[idx].append(int(congestion))
            idx += 1

# find median at each index
for i in range(0, 2340):
    biglst[i] = np.median(biglst[i])
    

for i in range(0, len(lines)):
    lines[i][1] = biglst[i]

x = open('train.csv', 'r')

r = csv.reader(x)
actualday = list(r)

x.close()

for i in range(0, len(lines)):
    lines[i].append(abs(pd.to_numeric(actualday[846496+i][5]) - lines[i][1]))
        #get the absolute value difference between the value here and the actual.)


# write in the new submission lines
f = open('monday_morning_medians.csv', 'w')
writer = csv.writer(f)
writer.writerow(["row_id", "congestion", "|difference|"])
writer.writerows(lines)

f.close()