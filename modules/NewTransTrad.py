from random import randint
from DictionaryGEN import trad2GEN # Sinon ce code est impossible à lire

"""
ERRORS LIST:
1 = erreur dans RNA_GEN() : manque un cordon d'initiation ou/et un cordon stop
2 = erreur dans DNA_RNA() : le format de l'ADN entré n'existe pas
3 = erreur dans RNA_DNA() : le format de l'ARNm entré n'existe pas
"""


def tochunk(m):
  return [(m[x] + m[x + 1] + m[x + 2]) for x in range(0, len(m) - 2, 3)]


def randomDNA():
  DNA = ['A', 'T', 'C', 'G']
  return "".join([DNA[randint(0, len(DNA) - 1)] for _ in range(100)])


def randomRNA():
  RNA = ['G', 'C', 'A', 'U']
  return "".join([RNA[randint(0, len(RNA) - 1)] for _ in range(100)])


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
  RNAlist = []
  for align in range(3): # Cherche pour chaque alignement, par exemple "AAUGA" aura une rechere sur ['AAU','GA'], ['AUG','A'] et ['UGA']
    RNA = staticRNA[align:] # on décale en supprimant les premières valeurs
    RNA = tochunk(RNA)
    dict = trad2GEN()
    RNA = [dict[x] for x in RNA]
    startPOS = [x for x in range(len(RNA)) if RNA[x] == 'Met']
    endPOS = [x for x in range(len(RNA)) if RNA[x] == 'STO']
  
    maxend = -1
    for start in startPOS:
      if maxend < start: # Pour empêcher d'avoir des acides aminés dans des acides aminés (AUGAUGUGA)
        for end in endPOS:
          if end > start:
            RNAlist.append("".join(RNA[start:end]))
            maxend = end
            break
  if RNAlist == []: # Rien n'a été trouvé : erreur
    return 1
  else:
    return RNAlist

def DNA_GEN(DNA):
  return RNA_GEN(DNA_RNA(DNA)) # plus simple que de recoder une autre fonction
