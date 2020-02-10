import pandas as pd
import matplotlib.pyplot as plt
from createdataset import *
import numpy as np
from bs4 import BeautifulSoup as bs
import codecs

filename = codecs.open("D:/Apps/Google Drive/Code/Python/mesengerAnalysis/facebook-davidmarch15/messages/inbox/antoniosousa_kajqqq3bvq/message_1.html", 'r')

soup = bs(filename, 'lxml')
text = soup.find_all('div', {'class' : '_3-96 _2let'})

#Save Logs
file= open("D:/Apps/Google Drive/Code/Python/mesengerAnalysis/chatdata.txt","a")


for i in text:
  msg = i.text
  msg = msg.replace('\n\n', '')
  msg = msg.replace('  ', '')
  file.write(str(msg) + '\n')
  print(msg)