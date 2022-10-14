def transcription(ADN):
  toARN = {
    'C': 'G',
    'G': 'C',
    'T': 'A',
    'A': 'U',
  }
  ARN = "".join([toARN[x] for x in ADN])
  ARN_start = [
    x for x in range(len(ARN)) if ARN[x] + ARN[x + 1] + ARN[x + 2] == "AUG"
  ]
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
    for x in range(0, len(ARN_start), 3)
  ])
