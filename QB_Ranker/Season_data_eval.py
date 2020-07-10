import csv
from statistics import median

writer = csv.writer(open("Averages.csv", "w"))
writer.writerow(["Year", "Cmp %", "TD %", "Int %", "YPA", "AYPA", "YPG"])

for val in range(1960, 2020):
    data = open("Season_Data/"+str(val)+".csv", "r")
    reader = csv.reader(data)

    #cmp_per = row[9]
    #td_per = row[11]
    #int_per = row[13]
    #ypa = row[15]
    #aypa = row[16]
    #ypg = row[18]

    final_data = []
    
    cmp_pers = []
    td_pers = []
    int_pers = []
    ypas = []
    aypas = []
    ypgs = []

    for row in reader:
        try:
            if int(val) < 1994 and int(row[8]) > 150:
                cmp_pers.append(float(row[9]))
                td_pers.append(float(row[12]))
                int_pers.append(float(row[14]))
                ypas.append(float(row[16]))
                aypas.append(float(row[17]))
                ypgs.append(float(row[19]))
            elif int(val) >= 1994 and int(row[8]) > 150:
                cmp_pers.append(float(row[9]))
                td_pers.append(float(row[12]))
                int_pers.append(float(row[14]))
                ypas.append(float(row[17]))
                aypas.append(float(row[18]))
                ypgs.append(float(row[20]))
        except:
            pass
    
    cmp_per = median(cmp_pers)
    td_per = median(td_pers)
    int_per = median(int_pers)
    ypa = median(ypas)
    aypa = median(aypas)
    ypg = median(ypgs)
    
    final_data.append(val)
    final_data.append(cmp_per)
    final_data.append(td_per)
    final_data.append(int_per)
    final_data.append(ypa)
    final_data.append(aypa)
    final_data.append(ypg)
    
    writer.writerow(final_data)
