from flask import Flask, render_template, url_for, redirect, request, flash
from modules.TransTrad import autoData

app = Flask(__name__)

app.config.update(  # used for flash() (no idea y)
  TESTING=True,
  SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)


@app.route('/', methods=['GET'])
def home():
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
  if data is None:
    print('The text did not work')
    flash('Vous n\'avez pas rentré une valeur correcte...'
          )  # Est affiché dans home.html
    return redirect(url_for('home'))
  else:
    return render_template('results.html', generationdata=data)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
