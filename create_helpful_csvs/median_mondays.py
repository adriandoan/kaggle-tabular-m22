import csv
import pandas as pd
import numpy as np

# create and add up each congestion that corresponds to each spot...(they line up)


# this is to create a blank submission file
f = open('submission_median.csv', 'w')

doit = csv.writer(f)

for i in range(848835, 851175):
    doit.writerow([i, 0])

f.close()


# get the list of lines
f = open('submission_median.csv', 'r')

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
with open('only_mondays.csv', 'r') as csv_file:
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


# write in the new submission lines
f = open('submission_median.csv', 'w')
writer = csv.writer(f)
writer.writerow(["row_id", "congestion"])
writer.writerows(lines)

f.close()