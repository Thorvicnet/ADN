import time
from datetime import datetime


def logwrite(text):
  f = open('adn.log', 'r')
  logs = f.readlines()
  f.close()
  f = open('adn.log', 'w')
  text = '\n\n' + datetime.fromtimestamp(
    time.time()).strftime("%d-%m-%Y, %H:%M:%S") + str(text)
  logs.append(text)
  f.writelines(logs)
  f.close()
