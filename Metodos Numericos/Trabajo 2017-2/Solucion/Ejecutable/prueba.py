import csv

vv = []
vv.append(11)
vv.append(20)

with open('len.csv', 'w', newline='') as dataCSV:
    writer = csv.writer(dataCSV, dialect='excel')
    writer.writerows([vv])
