from modules.TransTrad import gen_adn, traduction, transcription

ADN = ['A', 'T', 'C', 'G']

def run():
  brin_ADN = gen_adn(ADN)
  if transcription(brin_ADN) is False:
    run()
  else:
    ARN_start, ARN = transcription(brin_ADN)
    GEN = traduction(ARN_start)
    print('ADN :\n' + brin_ADN + '\n\nARNm :\n' + ARN + '\n\nARNm_START :\n' +
          ARN_start + '\n\nProtéine :\n' + GEN)


if __name__ == '__main__':
  run()