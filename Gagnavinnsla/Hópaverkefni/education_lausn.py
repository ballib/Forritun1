import csv
import sys

f = open('test_csv.csv')
data = {}
reader = csv.reader(f, delimiter=",")

for header in reader:
    data[header[0]] = []
    data[header[2]] = []
    data[header[3]] = []
    data[header[4]] = []
    break

for x in reader:
    data["Year"].append(int(x[0]))
    data["Age"].append(float(x[2]))
    data["Total"].append(int(x[3]))
    data["Percentage"].append(float(x[4]))

avg_16_19 = []
total_16_19 = []
avg_20_24 = []
total_20_24 = []
avg_25_29 = []
total_25_29 = []
for ix, x in enumerate(data["Age"]):
    if x == 16:
        avg_16_19.append((data["Percentage"][ix] + data["Percentage"][ix+1] + data["Percentage"][ix+2] + data["Percentage"][ix+3]) / 4)
        total_16_19.append(data["Total"][ix] + data["Total"][ix+1] + data["Total"][ix+2] + data["Total"][ix+3])
    if x == 20:
        avg_20_24.append((data["Percentage"][ix] + data["Percentage"][ix + 1] + data["Percentage"][ix + 2] + data["Percentage"][ix + 3] + data["Percentage"][ix + 4]) / 5)
        total_20_24.append(data["Total"][ix] + data["Total"][ix + 1] + data["Total"][ix + 2] + data["Total"][ix + 3] + data["Total"][ix + 4])
    if x == 25:
        avg_25_29.append((data["Percentage"][ix] + data["Percentage"][ix + 1] + data["Percentage"][ix + 2] + data["Percentage"][ix + 3] + data["Percentage"][ix + 4]) / 5)
        total_25_29.append(data["Total"][ix] + data["Total"][ix + 1] + data["Total"][ix + 2] + data["Total"][ix + 3] + data["Total"][ix + 4])

orig_stdout = sys.stdout
fout = open('education_group.csv', 'w+')
sys.stdout = fout

year = 1999
print("Year, Age, Total, Average")
for i in range(len(avg_16_19)):
    print(f"{year+i}, 16-19, {total_16_19[i]}, {avg_16_19[i]:.3f}")
    print(f"{year+i}, 20-24, {total_20_24[i]}, {avg_20_24[i]:.3f}")
    print(f"{year+i}, 25-29, {total_25_29[i]}, {avg_25_29[i]:.3f}")

sys.stdout = orig_stdout
fout.close()