from modules.TransTrad import gen_adn, traduction, transcription

ADN = ['A', 'T', 'C', 'G']


def run(
    brin_ADN=None):  # Aucune idée pourquoi des fois il lance pas avec argument
  if brin_ADN == 'None' or brin_ADN is None:
    brin_ADN = gen_adn(ADN)
  if transcription(brin_ADN) is False:
    return run()
  else:
    ARN_start, ARN = transcription(brin_ADN)
    GEN = traduction(ARN_start)
    return [brin_ADN, ARN, ARN_start, GEN]
