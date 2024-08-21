from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import openpyxl

url = "https://flip.ro/magazin/?category=laptop"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, "html.parser")

telefon = soup.find_all("div", class_="relative flex min-[991px]:flex-col gap-2 h-full")

specificatii_MAC = []
#nume
#pret
#link
#memorie si stare


for i in telefon:
    nume = i.find("span", class_="block").text
    # print(nume)
    pret = i.find("span", {"data-cy": "phone-price", "class":
        "font-bold text-sm leading-[1.2] min-[991px]:text-[18px] text-red"}).text
    link = i.find("div", class_ = "flex items-center justify-center").img["srcset"]
    # print(link)
    memorie_si_stare = i.find_all("span", class_ = "block")[1].text
    dictionar_MAC = {
        "Nume": nume,
        "Pret": pret,
        "Link": link,
        "Memorie & Stare": memorie_si_stare

    }
    specificatii_MAC.append(dictionar_MAC)

with open("specificatii_MAC.txt", "w+") as file:
    json.dump(specificatii_MAC,file, indent = 1)

df = pd.DataFrame(specificatii_MAC)
df.to_excel("specificatii_telefon.xlsx", index=False)
df.to_csv("specificatii_telefon.csv", index=False)






