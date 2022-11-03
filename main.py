from flask import Flask, render_template, url_for, redirect, request, flash
from modules.TransTrad import autoData
from flask_mobility import Mobility
from secrets import token_hex
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Mobility(app)  # Pour détecter les mobiles

app.config.update(
  TESTING=True,
  SECRET_KEY=token_hex(20)  # aléatoire pour ne pas avoir le secret sur github
)
'''
# Après réflexion on a réalisé que la database ne servait pas à grand chose donc
# voici son cadavre

# config de la database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  data = db.Column(db.String(200), nullable=False)

  def __repr__(self):  # représentation des données
    return f"User('{self.username}', '{self.password}')"


@app.route('/login', methods=['POST', 'GET'])
def login():
  if request.method == 'POST':  # si le serveur recoit une requete POST on le redirige vers la page utilisateur
    session.permanent = True
    user = request.form["username"]
    flash(f"Bienvenue {user} !", 'success')
    return redirect(url_for('profile'))
  else:  # si le serveur recoit GET, il retourne le page de login
    if "user" in session:
      user = session["user"]
      flash(f"Vous êtes déjà connecté en tant que {user}.", 'info')
      return redirect(url_for('profile'))
    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
  session.permanent = True
  if request.method == 'POST' and "user" not in session:
    user = request.form["username"]
    session["user"] = user  # on sauvegarde le nom dans la session
    flash(f"Bienvenue {user} !", 'success')
    return redirect(url_for('profile'))
  elif request.method == 'POST':
    user = session["user"]
    flash(f'Vous êtes déjà connecté en tant que {user}.', 'info')
    return render_template('profile.html')
  elif "user" in session:
    return redirect(url_for('profile'))
  else:
    return render_template('signup.html')


@app.route('/logout')
def logout():
  if "user" in session:  # on flash uniquement si l'utilisateur a réellement été deconnecté
    user = session["user"]
    session.pop("user", None)  # session etant un dictionnaire, on y enleve l'utilisateur.
    flash(f"{user}, vous avez bien été déconnecté.", 'info')
  else:
    flash("Aucun compte n'était connecté.", 'info')
  return redirect(url_for('login'))


@app.route('/user')
def profile():
  if "user" in session:
    user = session["user"]
    return render_template("user.html", user=user)
  else:
    return redirect(url_for("login"))
'''


@app.route('/', methods=['GET'])
def home():
  if request.MOBILE == True:  # Si l'utilisateur est sur téléphone
    return render_template('mobile.html')
  else:
    return render_template('home.html')


@app.route('/', methods=['POST'])
def index_post():
  try:
    DNA = request.form['DNA'].upper()
    return redirect(url_for('results', input=DNA, type='DNA'))
  except:
    pass
  try:
    RNA = request.form['RNA'].upper()
    return redirect(url_for('results', input=RNA, type='RNA'))
  except:
    pass


@app.route('/results')
def results():
  text = request.args['input']
  type = request.args['type']
  data = autoData(text, type)
  if data is None or 2 in data or 3 in data:  # Si l'ARN ou l'ADN rentré est incorrecte ou autre probleme, NE PAS CHANGER l'ordre des conditions sinon erreur ¯\_(ツ)_/¯
    #print('The text did not work')
    flash('Vous avez rentré une valeur incorrecte...',
          'danger')  # Est affiché dans home.html
    return redirect(url_for('home'))
  else:
    return render_template('results.html', generationdata=data)


@app.route('/logs')
def logs():
  try:
    with open('adn.log', 'r') as f:
      logs = "".join(f.readlines()[:30])
  except FileNotFoundError:
    with open('adn.log', 'x') as f:
      logs = ""
  return render_template('logs.html', logs=logs)

if __name__ == '__main__':  # Montre que c'est le fichier principal
  app.run(host='0.0.0.0', port=443, debug=True)
