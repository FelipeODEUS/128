from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

pages = requests.get(url)
soup = bs(pages.text,"html.parse")

star_table = soup.find_all('table', {"class":"wikitable sortable"})
total_table = len(star_table)
temp_list = []

table_rows = star_table[1].find_all('tr')
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_name = []
Distance = []
Mass = []
Radiuns = []

print(temp_list)
for i in range(1, len(temp_list)):
    Star_name.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radiuns.append(temp_list[i][8])

headers = ['Star_name','Distance','Mass','Radius']
df2 = pd.DataFrame(list(zip(Star_name,Distance,Mass,Radiuns,)),columns=['Star_name','Distance','Mass','Radius'])
df2.to_csv('dwarf_stars.csv', index=True, index_label="id")

