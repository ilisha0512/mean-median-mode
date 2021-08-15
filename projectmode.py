from collections import Counter
import csv
with open ("SOCR-HeightWeight (1).csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
newdata = []
for i in range(len(file_data)):
    n = file_data[i][1]
    newdata.append(float(n))
data = Counter(newdata)
for height, occurence in data.items():
    if (occurence == max(list(data.values()))):
        print(height)