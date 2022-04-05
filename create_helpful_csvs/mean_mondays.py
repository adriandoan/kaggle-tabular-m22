import csv
import pandas as pd

# create and add up each congestion that corresponds to each spot...(they line up)


# this is to create a blank submission file
f = open('submission_mean.csv', 'w')

doit = csv.writer(f)

for i in range(848835, 851175):
    doit.writerow([i, 0])

f.close()


# get the list of lines
f = open('submission_mean.csv', 'r')

r = csv.reader(f)
lines = list(r)

f.close()


# iterate through only_mondays and sum each corresponding congestion
totaldays = 0
linenumber = 0
with open('only_mondays.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        congestion = pd.to_numeric(row[5])
        if linenumber == 2340:
            linenumber = 0
            lines[linenumber][1] = int(lines[linenumber][1]) + int(congestion)
            linenumber += 1
            totaldays += 1
        else:
            lines[linenumber][1] = int(lines[linenumber][1]) + int(congestion)
            linenumber += 1


# divide by the total days for each congestion sum for average
for line in lines:
    line[1] = float(line[1])/totaldays


# write in the new submission lines
f = open('submission_mean.csv', 'w')
writer = csv.writer(f)
writer.writerow(["row_id", "congestion"])
writer.writerows(lines)

f.close()