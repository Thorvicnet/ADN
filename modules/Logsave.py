import time
from datetime import datetime


def logwrite(text):
  """Ecrit un texte dans les adn.log avec devant la date et heure

  Args:
      text (str): texte à écrire dans les logs
  """
  try:
    with open('adn.log', 'r') as f:
      logs = f.readlines()  # On ouvre les logs et on les écrits dnas logs
    f = open(
      'adn.log', 'w'
    )  # On ouvre les logs en mode d'écriture
    text = '\n\n' + datetime.fromtimestamp(
      time.time()).strftime("%d-%m-%Y, %H:%M:%S") + ' ' + str(text) # On rajoute au texte la date et heure
    # time.time() nous donne la time stamp
    # datetime.fromtimestamp() la traduit en valeur compréhensible
    # strftime(format) la transforme dans le format voulu, ici "day-month-year, hour:minutes:seconds"
    logs.insert(0, text) # On rajoute la nouvelle entrée dans les logs
    f.writelines(logs) # On écrit les logs au fichier
    f.close() # On ferme le fichier
  except:  # Si le fichier n'existe pas : le créer ("x")
    f = open("adn.log", "x")
    f.close()
    logwrite(text) # Et on réessaye
