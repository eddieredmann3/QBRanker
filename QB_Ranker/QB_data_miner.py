from bs4 import BeautifulSoup as soup
from urllib.request import *
import csv

QBs = []

inputData = open("QB_Data/input.txt", "r")
for qb in inputData.readlines():
    qbName = qb.split()

    url = "https://www.pro-football-reference.com/players/"+qbName[1][0]+"/"+qbName[1][0:4]+ qbName[0][0:2]+"00.htm"
    try:
        content = urlopen(url).read()
        urlopen(url).close()
    
        mySoup = soup(content, "html.parser")

        output = open("QB_Data/"+str(qb)+".csv", "w")
        writer = csv.writer(output)
        for tr in mySoup.table("tr"):
            writer.writerow([tr("th")[th].text for th in range(1, len(tr("th")))])
            writer.writerow([tr("td")[td].text for td in range(len(tr("td")))])
        output.close()
        print("Found for: " + str(qb))
    except:
        msg = "Failed for: " + str(qb) + "\n"
        snowflakes = open("QB_Data/snowflakes.txt", "w")
        snowflakes.write(msg)
        print(msg)
