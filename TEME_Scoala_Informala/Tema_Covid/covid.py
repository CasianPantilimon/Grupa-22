import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find("table", {"id": "example2"}).find("tbody").find_all("tr")

country_list = []

for row in rows:
    my_dict = {}
    my_dict["Country"] = row.find_all("td")[1].text
    my_dict["Population"] = row.find_all("td")[2].text
    # if we want an integer we can do: .replace(",","")
    my_dict["Area km2"] = row.find_all("td")[6].text
    my_dict["Density /km2"] = row.find_all("td")[5].text

    country_list.append(my_dict)

# print(country_list[0])


df = pd.DataFrame(country_list)
df.to_excel("Tema_Covid.xlsx", index=False)
df.to_csv("Tema_Covid.csv", index=False)