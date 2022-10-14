def transcription(ADN):
  toARN = {
    'C': 'G',
    'G': 'C',
    'T': 'A',
    'A': 'U',
  }
  ARN = "".join([toARN[x] for x in ADN])
  # aucun sens ce que j'ai tapé,
  # ARN[:x] te donne ce qu'il y'a avant l'index x on est d'accord ?
  # je sais plus comment slicer je me fait avoir à chaque fois
  # string = slice(6)   => les 6 premiers caracteres  (jcrois) ok
  ARN_start = 'AUG' + ARN.split('AUG', 1)[1]
  return ARN_start, ARN


#TODO rajouter utilisation STOP
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
    "AUU": "lle",
    "AUC": "lle",
    "AUA": "lle",
    "AUG": "Met",
    "GUU": "val",
    "GUC": "Val",
    "GUA": "Var",
    "GUG": "Var",
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
  return "".join([
    trad[ARN_start[x] + ARN_start[x + 1] + ARN_start[x + 2]]
    for x in range(0,
                   len(ARN_start) - 2, 3)
  ])
# Bon je vais arrêter je pense
# Je t'ai invité au github