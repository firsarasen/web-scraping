import requests
from bs4 import BeautifulSoup
import json

url = "https://www.kompas.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

data = []
quotes = soup.find_all("h1", class_="hlTitle")

for item in quotes:
    data.append({
        "judul": item.text.strip()
    })

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=True)

print("Data berhasil disimpan ke data.json")