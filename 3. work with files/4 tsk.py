import csv

with open("table.csv", "r") as file:
    rows = csv.reader(file, delimiter=';')
    data = []
    for row in rows:
        data.append(row)
data.insert(4,[0,0,0,0,0,0])
for i in range(len(data)):
    data[i].insert(4,0)
with open("table_updated.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(data)