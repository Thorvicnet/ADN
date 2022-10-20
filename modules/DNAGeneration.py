from modules.TransTrad import gen_adn, traduction, transcription
from .Logsave import logwrite

ADN = ['A', 'T', 'C', 'G']


def run(
    brin_ADN=None):  # Aucune idée pourquoi des fois il lance sans argument
  given = False
  if brin_ADN == 'None' or brin_ADN is None:
    brin_ADN = gen_adn(ADN)
  else:
    given = True # Dans ce cas on ne veut pas générer aléatoirement lorsque cela ne fonctionne pas
  if transcription(brin_ADN) is False:
    if given:
      return None # L'ADN donné n'est pas possible
    else:
      logwrite('regénération')
      return run()
  else:
    ARN_start, ARN = transcription(brin_ADN)
    GEN = traduction(ARN_start)
    logwrite([brin_ADN, ARN, ARN_start, GEN])
    return [brin_ADN, ARN, ARN_start, GEN]
