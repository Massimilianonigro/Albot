import os
import json
import csv

srcpath = "."
chat_path = "./chat"
chatless_path = "./chatless"
print("CHATLESS:")
headers = [
    "name",
    "first part total clicks",
    "first part object clicks",
    "first part scale clicks",
    "first part chat messages",
    "second part total clicks",
    "second part object clicks",
    "second part scale clicks",
    "second part guessing errors",
    "seconnd part chat messages",
]
writer = csv.writer(open("albot_click_messages_count.csv", "w+"))
writer.writerow(headers)
for root, subfolders, files in os.walk(chatless_path):
    for file in files:
        data = []
        current_dict = json.load(open(chatless_path + "/" + file, "r"))
        data = [
            current_dict["name"],
            current_dict["first_part_total_click_count"],
            current_dict["first_part_click_count"],
            current_dict["first_part_guessed_count"],
            0,
            current_dict["second_part_total_click_count"],
            current_dict["second_part_click_count"],
            current_dict["second_part_guessed_count"],
            current_dict["second_part_error_count"],
            0,
        ]
        writer.writerow(data)

for root, subfolders, files in os.walk(chat_path):
    for file in files:
        data = []
        current_dict = json.load(open(chat_path + "/" + file, "r"))
        data = [
            current_dict["name"],
            current_dict["first_part_total_click_count"],
            current_dict["first_part_click_count"],
            current_dict["first_part_guessed_count"],
            current_dict["first_part_text_count"],
            current_dict["second_part_total_click_count"],
            current_dict["second_part_click_count"],
            current_dict["second_part_guessed_count"],
            current_dict["second_part_error_count"],
            current_dict["second_part_text_count"],
        ]
        writer.writerow(data)
