import csv
import pandas as pd

f = open('submission_median.csv', 'r')

r = csv.reader(f)
lines = list(r)

f.close()

for i in range(1, len(lines)):
    lines[i][1] = int(pd.to_numeric(lines[i][1]))


f = open('submission_median_ints.csv', 'w')

writer = csv.writer(f)
#writer.writerow(["row_id", "congestion"])
writer.writerows(lines)

f.close()