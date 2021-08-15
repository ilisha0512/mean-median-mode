import csv
with open ("SOCR-HeightWeight (1).csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
newdata = []
for i in range(len(file_data)):
    n = file_data[i][1]
    newdata.append(float(n))
l = len(newdata)
newdata.sort()
if(l%2==0):
    median1 = float(newdata[l//2])