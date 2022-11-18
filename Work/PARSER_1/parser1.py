from email import header
from itertools import count
import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import json
import csv

# url = "https://health-diet.ru/base_of_food/food_24529/"

# headers = {
#     "accept": "*/*",
#     "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 Mobile Safari/537.36",
# }

# req = requests.get(url, headers=headers)
# scr = req.text
# print(req.content.decode('utf-8'))

# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(scr)

with open("index.html", encoding="utf8") as file:
    scr = file.read()

soup = BeautifulSoup(scr, "lxml")
data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")
print(data)

table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")

# with open(f"table_fast_food.csv", "w", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         (
#             product,
#             calories,
#             proteins,
#             fats,
#             carbohydrates
#         )
#     )

product_info = []

for i in data:
    tds = i.find_all("td")

    title = tds[0].find("a").text
    calories = tds[1].text
    proteins = tds[2].text
    fats = tds[3].text
    carbohydrates = tds[4].text

    # product_info.append(
    #     {
    #         "Название": title,
    #         "Калории": calories,
    #         "Белки": proteins,
    #         "Жиры": proteins,
    #         "Углеводы": carbohydrates,
    #     }
    # )

#     with open(f"table_fast_food.csv", "a", encoding="utf-8", newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             (
#                 title,
#                 calories,
#                 proteins,
#                 fats,
#                 carbohydrates
#             )
#         )

# with open("DATA_FAST_FOOD.json", "a", encoding="utf-8") as file:
#     json.dump(product_info, file, indent=4, ensure_ascii=False)