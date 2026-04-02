import requests
from bs4 import BeautifulSoup
import csv
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

with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["No", "Judul"])

    for i, item in enumerate(data, start=1):
        writer.writerow([i, item["judul"]])

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Data berhasil disimpan ke data.json")
