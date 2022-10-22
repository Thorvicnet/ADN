from random import randint
import modules.DictionaryGEN as dictGEN  # Sinon ce code est impossible à lire
import modules.Logsave as log
"""
ERRORS LIST:
1 = erreur dans RNA_GEN() : manque un codon d'initiation ou/et un codon stop
2 = erreur dans DNA_RNA() : le format de l'ADN entré n'existe pas
3 = erreur dans RNA_DNA() : le format de l'ARNm entré n'existe pas
"""


def tochunk(m):
  return [(m[x] + m[x + 1] + m[x + 2]) for x in range(0, len(m) - 2, 3)]


def stringifyGEN(
  GEN
):  # Permet d'enlever la liste pour la remplacer par les protéines séparées par des virgules
  try:
    return ", ".join(GEN)
  except:  # Si GEN est vide
    return GEN


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
  for frame in range(
      3
  ):  # Cherche pour chaque alignement, par exemple "AAUGA" aura une recherche sur ['AAU','GA'], ['AUG','A'] et ['UGA']
    RNA = staticRNA[frame:]  # on décale en supprimant les premières valeurs
    RNA = tochunk(RNA)
    dict = dictGEN.trad2GEN()
    RNA = [dict[x] for x in RNA]
    startPOS = [x for x in range(len(RNA)) if RNA[x] == 'Met']
    endPOS = [x for x in range(len(RNA)) if RNA[x] == 'STO']

    maxend = -1
    for start in startPOS:
      if maxend < start:  # Pour empêcher d'avoir des acides aminés dans des acides aminés (AUGAUGUGA)
        for end in endPOS:
          if end > start:
            RNAlist.append("".join(RNA[start:end]))
            maxend = end
            break
  if RNAlist == []:  # Rien n'a été trouvé : erreur
    return 1
  else:
    return RNAlist


def DNA_GEN(DNA):
  return RNA_GEN(DNA_RNA(DNA))  # plus simple que de recoder une autre fonction


def autoData(value, type):
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
    log.logwrite('Did not work')
    data = None
  return data
