import csv

season_reader = csv.reader(open("Averages.csv", "r"))
QB_reader = open("QB_Data/input.txt", "r")
QBs = QB_reader.readlines()

for qb in QBs:
    pass
