from bs4 import BeautifulSoup as soup
from urllib.request import *
import sys
import csv

for i in range(1960, 2020):
    url = "https://www.pro-football-reference.com/years/" + str(i) + "/passing.htm"
    content = urlopen(url).read()
    urlopen(url).close()
    
    souper = soup(content, "html.parser")
    
    output = open("Season_Data/"+str(i)+".csv", "w")
    writer = csv.writer(output)
    for tr in souper.table("tr"):
        writer.writerow([tr("th")[th].text for th in range(1, len(tr("th")))])
        writer.writerow([tr("td")[td].text for td in range(len(tr("td")))])
    output.close()
