from random import randint

# generateur du brin d'ADN
def gen_adn(ADN):
  brin_ADN = "".join([ADN[randint(0, len(ADN) - 1)] for _ in range(100)])
  
  return brin_ADN

def transcription(brin_ADN):
  toARN = {
    'C': 'G',
    'G': 'C',
    'T': 'A',
    'A': 'U'
  }
  # si le codon d'initiation n'a pas été généré, on retourne False
  if 'TAC' in brin_ADN:  # 'TAC' equivalent a AUG avant la transcription
    pass
  else:
    print(f"Format du brin invalide (pas de codon d'initiation) : {brin_ADN}\n")
    print("Regénération du brin d'ADN...\n\n")
    return False
  # portions d'ADN génomique sont transcrites en ARN messager
  ARN = "".join([toARN[x] for x in brin_ADN])
  ARN_start = 'AUG' + ARN.split('AUG', 1)[1]  # AUG : START (Met)
  
  return ARN_start, ARN


def traduction(ARN_start):
  trad = {
    "UUU": "Phe",
    "UUC": "Phe",
    "CUU": "Leu",
    "CUC": "Leu",
    "CUA": "Leu",
    "CUG": "Leu",
    "UUA": "Leu",
    "UUG": "Leu",
    "AUU": "Ile",
    "AUC": "Ile",
    "AUA": "Ile",
    "AUG": "Met",
    "GUU": "Val",
    "GUC": "Val",
    "GUA": "Val",
    "GUG": "Val",
    "UCU": "Ser",
    "UCC": "Ser",
    "UCA": "Ser",
    "UCG": "Ser",
    "AGU": "Ser",
    "AGC": "Ser",
    "CCU": "Pro",
    "CCC": "Pro",
    "CCA": "Pro",
    "CCG": "Pro",
    "ACU": "Thr",
    "ACC": "Thr",
    "ACA": "Thr",
    "ACG": "Thr",
    "GCU": "Ala",
    "GCC": "Ala",
    "GCA": "Ala",
    "GCG": "Ala",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
    "UAU": "Tyr",
    "UAC": "Tyr",
    "CAU": "His",
    "CAC": "His",
    "CAA": "Gin",
    "CAG": "Gin",
    "AAU": "Asn",
    "AAC": "Asn",
    "AAA": "Lys",
    "AAG": "Lys",
    "GAU": "Asp",
    "GAC": "Asp",
    "GAA": "Glu",
    "GAG": "Glu",
    "UGU": "Cys",
    "UGC": "Cys",
    "UGG": "Trp",
    "CGU": "Arg",
    "CGC": "Arg",
    "CGA": "Arg",
    "CGG": "Arg",
    "AGA": "Arg",
    "AGG": "Arg",
    "GGU": "Gly",
    "GGC": "Gly",
    "GGA": "Gly",
    "GGG": "Gly"
  }
  GEN = "".join([
    trad[ARN_start[x] + ARN_start[x + 1] +
         ARN_start[x +
                   2]]  # parcourir ARN_start de 3 par 3 et comparer la valeur
    for x in range(
      0,  # correspondante avec trad
      len(ARN_start) - 2,
      3)
  ])
  return GEN.split('STOP', 1)[0]
