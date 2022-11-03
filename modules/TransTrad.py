from random import randint
import modules.DictionaryGEN as dictGEN  # Sinon ce code est impossible à lire
import modules.Logsave as log

"""
ERRORS LIST:
1 = erreur dans RNA_GEN() : manque un codon d'initiation ou/et un codon stop
2 = erreur dans DNA_RNA() : le format de l'ADN entré n'existe pas
3 = erreur dans RNA_DNA() : le format de l'ARNm entré n'existe pas
"""

RANDOMSIZE = 100 # Permet de modifier la taille de la string générée par randomDNA() et randomRNA()



def tochunk(m):
  """Transforme un texte ou une liste en groude de 3 de ces éléments

  Args:
      m (str or list): éléments à fragmenter en groupe de 3

  Returns:
      list: la liste contenant les éléments 3 par 3
  """
  return [(m[x] + m[x + 1] + m[x + 2]) for x in range(0, len(m) - 2, 3)]


def stringifyGEN(GEN):  # Permet d'enlever la liste pour la remplacer par les protéines séparées par des virgules
  """Transforme une liste en string séparant par des virgules les différents éléments

  Args:
      GEN (list): éléments à rassembler en string

  Returns:
      str: éléments dans une string séparés par des virgules
  """
  try:
    return ", ".join(GEN)
  except:  # Si GEN est vide
    return GEN


def randomDNA():
  DNA = ['A', 'T', 'C', 'G']
  return "".join([DNA[randint(0, len(DNA) - 1)] for _ in range(RANDOMSIZE)])


def randomRNA():
  RNA = ['G', 'C', 'A', 'U']
  return "".join([RNA[randint(0, len(RNA) - 1)] for _ in range(RANDOMSIZE)])


def DNA_RNA(DNA):
  DNA_RNA = {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'U'}
  try:
    return "".join([DNA_RNA[x] for x in DNA])
  except KeyError:
    return 2


def RNA_DNA(RNA):
  RNA_DNA = {'G': 'C', 'C': 'G', 'A': 'T', 'U': 'A'}
  try:
    return "".join([RNA_DNA[x] for x in RNA])
  except KeyError:
    return 3


def RNA_GEN(staticRNA):
  """Trouve les acides aminés dans l'ARNm

  Args:
      staticRNA (str): ARNm d'où nous voulons trouver les acides aminés

  Returns:
      list: liste contenant les acides aminés
  """
  RNAlist = []
  for frame in range(3):  # Cherche pour chaque alignement, par exemple "AAUGA" aura une recherche sur ['AAU','GA'], ['AUG','A'] et ['UGA']
    RNA = staticRNA[frame:]  # on décale en supprimant les premières valeurs
    RNA = tochunk(RNA)
    dict = dictGEN.trad2GEN() # On récupère l'énorme dictionnaire
    RNA = [dict[x] for x in RNA] # On fait la traduction avec l'ARNm
    startPOS = [x for x in range(len(RNA)) if RNA[x] == 'Met'] # Positions de tous les codons-start
    endPOS = [x for x in range(len(RNA)) if RNA[x] == 'STO'] # Positions de tous les codons-stop

    maxend = -1
    for start in startPOS:
      if maxend < start:  # Pour empêcher d'avoir des acides aminés dans des acides aminés (AUGAUGUGA)
        for end in endPOS:
          if end > start:
            RNAlist.append("".join(RNA[start:end])) # On à trouver un acide aminés de pos "start" à "stop" que l'on enregistre dans RNAlist
            maxend = end
            break
  if RNAlist == []:  # Rien n'a été trouvé : erreur
    return 1
  else:
    return RNAlist


def DNA_GEN(DNA):
  return RNA_GEN(DNA_RNA(DNA))  # plus simple que de recoder une autre fonction


def autoData(value, type):
  """Fournit directement quoi afficher sur la page à partir de la valeur et si elle est DNA ou RNA
     si value = 'None' alors elle sera générée aléatoirement

  Args:
      value (str): la string à traduire et transcrire
      type (str): le type de value fournit (soit 'DNA' ou 'RNA')

  Returns:
      list: liste contenant [ADN, ARNm, acide aminés]
  """
  try:
    if type == 'DNA':
      DNA = value
      if DNA == 'None':
        DNA = randomDNA()
      data = [DNA, DNA_RNA(DNA), stringifyGEN(DNA_GEN(DNA))]
    elif type == 'RNA':
      RNA = value
      if RNA == 'None':
        RNA = randomRNA()
      data = [RNA_DNA(RNA), RNA, stringifyGEN(RNA_GEN(RNA))]
    if 1 in data:  # Si la traduction de l'ARN est impossible
      data[2] = 'Aucune protéine complète trouvée'
    log.logwrite(data)  
  except:
    log.logwrite('Did not work') # L'utilisateur à entrer une valeur impossible
    data = None # il sera redirigé sur / avec un message d'alerte
  return data
