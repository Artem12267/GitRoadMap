
from email import header
import requests
from bs4 import BeautifulSoup
import json
import csv

# url = "https://tolyatti.streetfoot.ru/catalog/zhenskie-krossovki/?filtering=1&filter_gender=man#content"

# # #def get_data(url):
# headers = {
# "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.114 YaBrowser/22.9.1.1095 Yowser/2.5 Safari/537.36"
# }

# req = requests.get(url, headers) 
# scr = req.text


# #get_data("https://tolyatti.streetfoot.ru/catalog/zhenskie-krossovki/?filtering=1&filter_gender=man#content")

# with open("Sneakers.html", "w", encoding="utf-8") as file:
#     file.write(scr)

with open("Sneakers.html", encoding="utf8") as file:
    scr = file.read()

soup = BeautifulSoup(scr, "lxml")
data = soup.find(class_="site-main").find_all(class_="products")

items_info = []

# with open("Sneakers.csv", "w", encoding="utf-8", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         (
#             "title",
#             "price",
#             "href"
#         )
#     )
    

for i in data[0]:
    tds = i.find_all("li")
    print(tds)
    link = soup.find_all('a', class_='woocommerce-LoopProduct-link')[0]

    title = tds[0].find("a").find("h3").text
    price = tds[0].find("a").find(class_="price").text
    href = "https://tolyatti.streetfoot.ru" + link.get("href")

    # with open("Sneakers.csv", "a", encoding="utf-8", newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(
    #         (
    #             title,
    #             price,
    #             href
    #         )
    #     )

    # items_info.append(
    #     {
    #         "Название" : title,
    #         "Цена" : price,
    #         "Ссылка" : href
    #     }
    # )

    # print(items_info)
