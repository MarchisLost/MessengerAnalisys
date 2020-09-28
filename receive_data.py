import pandas as pd

# import matplotlib.pyplot as plt
# from createdataset import *
import numpy as np
from bs4 import BeautifulSoup as bs
import csv

# Fixo
filename = open("message_1.html", "r", encoding="utf8")

soup = bs(filename, "lxml")
text = soup.select("div.uiBoxWhite")
textMsg = soup.find_all("div", {"class": "_3-96 _2let"})

# Get data
dates = []
for i in text:
    date = i.select("div")[-1].text
    date = "".join(date.split(",")[:-1])
    dates.append(date)
    #print("date:", date)
#print(dates)    

#Write on csv
with open("dates.csv", mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Date'])
    for i in dates:
        writer.writerow([i])

# Get messages
for j in textMsg:
    msg = j.text
    msg = msg.replace("\n", "")
    msg = msg.replace("  ", "")
    #print('msg:', msg)

""" df = pd.read_csv('chatdata.csv')
df.groupby(df.date).size().to_csv("count.csv", header=True)
ab = pd.read_csv('count.csv')
ab['date'] = pd.to_datetime(ab.date)
ab.sort_values('date').to_csv("sorted.csv", header=True) """
