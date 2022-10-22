from flask import Flask, render_template, url_for, redirect, request, flash
from modules.TransTrad import autoData
from flask_mobility import Mobility
from secrets import token_hex

app = Flask(__name__)
Mobility(app)  # Pour détecter les mobiles

app.config.update(  # used for flash() (no idea y)
  TESTING=True,
  SECRET_KEY=token_hex(20) # aléatoire pour ne pas avoir le secret dans le github
)


@app.route('/', methods=['GET'])
def home():
  if request.MOBILE == True:  # Si l'utilisateur est sur téléphone
    return render_template('mobile.html')
  else:
    return render_template('home.html')


@app.route('/', methods=['POST'])
def index_post():
  try:
    DNA = request.form['DNA']
    return redirect(url_for('results', input=DNA, type='DNA'))
  except:
    pass
  try:
    RNA = request.form['RNA']
    return redirect(url_for('results', input=RNA, type='RNA'))
  except:
    pass


@app.route('/results')
def results():
  text = request.args['input']
  type = request.args['type']
  data = autoData(text, type)
  if data is None or 2 in data or 3 in data:  # Si l'ARN ou l'ADN rentré est incorrecte ou autre probleme, NE PAS CHANGER l'ordre des conditions sinon erreur ¯\_(ツ)_/¯
    print('The text did not work')
    flash('Vous n\'avez pas rentré une valeur correcte...'
          )  # Est affiché dans home.html
    return redirect(url_for('home'))
  else:
    return render_template('results.html', generationdata=data)


@app.route('/logs')
def logs():
  with open('adn.log', 'r') as f:
    logs = "".join(f.readlines()[-30:])
  return render_template('logs.html', logs=logs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8443, debug=True)
