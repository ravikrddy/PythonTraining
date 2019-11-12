import csv

with open('MyQualtricsDownload/Customer Service APAC.csv') as f:
    reader = csv.reader(f)
    fulllist = list(reader)
    for row in range(3,len(fulllist)-2380):
        print(fulllist[row])
