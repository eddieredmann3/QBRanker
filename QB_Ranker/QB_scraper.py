import csv

QBs = []

fileData = open("QB_Data/input.txt","w")
for i in range(1960, 2020):
    with open("Season_Data/"+str(i)+".csv") as csvData:
        reader = csv.reader(csvData, delimiter=",")
        for row in reader:
            if row != [] and row[0] not in QBs and row[0][len(row[0])-1] != "*" and row[0][len(row[0])-1] != "+":
                try:
                    if int(row[8]) > 150:
                        fileData.write(row[0]+"\n")
                        QBs.append(row[0])
                except:
                    pass

