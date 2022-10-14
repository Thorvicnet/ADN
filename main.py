from modules.TransTrad import traduction, transcription

ADN = input(' > Entrez L\'ADN : ')
ARN_start, ARN = transcription(ADN)
GEN = traduction(ARN_start)
print(ARN, GEN)
