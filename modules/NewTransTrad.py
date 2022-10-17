from random import randint, sample

def randomDNA():
  DNA = ['A', 'T', 'C', 'G']
  return "".join([DNA[randint(0, len(DNA) - 1)] for _ in range(99)]) # 99 because we don't want to loose data while grouping by 3

def DNA_RNA(DNA):
  DNA_RNA = {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'U'}
  return [DNA_RNA[x] for x in DNA]

def findstartRNA(RNA):
  RNA = RNA.split('AUG',1)[1]
  return [RNA[x] + RNA[x+1] + RNA[x+2] for x in range(0,len(RNA)-2,3)].insert("AUG") # element 3 par 3

def findstopRNA(RNA):
  RNA = RNA.index('')
  return RNA

def correctRNA(RNA):
  try:
    return findstopRNA(findstartRNA(RNA))
  except:
    return None

print(DNA_RNA(randomDNA()))