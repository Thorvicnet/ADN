from modules.TransTrad import traduction, transcription

ADN = input(' > Entrez L\'ADN : ')
ARN_start, ARN = transcription(ADN)
GEN = traduction(ARN_start)
print('ADN :\n' + ADN + '\n\nARNm :\n' + ARN + '\n\nARNm_START :\n' +
      ARN_start + '\n\nProtéine :\n' + GEN)
