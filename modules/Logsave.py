import time
from datetime import datetime


def logwrite(text):
  try:
    with open('adn.log', 'r') as f:
      logs = f.readlines()  # On ouvre les logs et on les enregistrent
    f = open(
      'adn.log', 'w'
    )  # On ouvre les logs et on rajoute la date et les données nécessaires
    text = '\n\n' + datetime.fromtimestamp(
      time.time()).strftime("%d-%m-%Y, %H:%M:%S") + ' ' + str(text)
    logs.insert(0, text)
    f.writelines(logs)
    f.close()
  except:  # Si le fichier n'existe pas : le créer ("x")
    f = open("adn.log", "x")
    f.close()
    logwrite(text)
