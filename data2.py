import csv
dataset1 = []
dataset2 = []
with open("final.csv","r") as f:
    csv_reader = csv.reader(f)
    for j in csv_reader:
        dataset1.append(j)

with open("sorted.csv","r") as f:
    csv_reader = csv.reader(f)
    for m in csv_reader:
        dataset2.append(m)

header1 = dataset1[0]
planet_data1 = dataset1[1:]
header2 = dataset2[0]
planet_data2 = dataset2[1:]
headers = header1 + header2
# print(headers)
planet_data = []
for index,data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

merged_dataset = []
with open("merged_dataset.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)  