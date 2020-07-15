import pandas as pd
#import matplotlib.pyplot as plt
#from createdataset import *
import numpy as np
from bs4 import BeautifulSoup as bs
import csv

#Fixo
filename = open("message_1.html", 'r', encoding='utf8')

#Portatil
""" filename = codecs.open("D:/Apps/Google Drive/Code/Python/MessengerAnalysis/facebook-davidmarch15/messages/inbox/antoniosousa_kajqqq3bvq/message_1.html", 'r') """

soup = bs(filename, 'lxml')
text = soup.select('div.uiBoxWhite')
textMsg = soup.find_all('div', {'class' : '_3-96 _2let'})

#Save Logs
#file= open("chatdata.txt","a")

#Get data
for i in text:
  date = i.select('div')[-1].text
  date = ''.join(date.split(',')[:2])
  #TODO: meter tudo num array ou algo assim e depois mandar esse array pro file
  df = pd.DataFrame([date], columns=['Date'])
  df.to_csv('dates.csv')
  print('date:', date)

#Get messages
for j in textMsg:
  msg = j.text
  msg = msg.replace('\n\n', '')
  msg = msg.replace('  ', '')
  #print('msg:', msg) 


""" df = pd.read_csv('chatdata.csv')
df.groupby(df.date).size().to_csv("count.csv", header=True)
ab = pd.read_csv('count.csv')
ab['date'] = pd.to_datetime(ab.date)
ab.sort_values('date').to_csv("sorted.csv", header=True) """