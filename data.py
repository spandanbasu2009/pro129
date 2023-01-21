import csv
data = []
with open("archive_dataset.csv","r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data.append(i)

headers = data[0]
planet_data = data[1:]
for datapoint in planet_data:
    datapoint[2] = datapoint[2].lower()

planet_data.sort(key = lambda planet_data:planet_data[2])
with open("sorted.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)