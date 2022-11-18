
from art import tprint
import csv

tprint(text="CSV")

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        ("user_name", "user_address")
    )

users_data = [
    ["user1", "address1"],
    ["user2", "address2"],
    ["user3", "address3"],
]

with open("data.csv", "a", encoding="utf-8", newline="") as file: #a + append
    writer = csv.writer(file)
    writer.writerows(users_data)

