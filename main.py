from flask import Flask, render_template, url_for, redirect, request, flash
from modules.DNAGeneration import run

app = Flask(__name__)

app.config.update( # used for flash() (no idea y)
  TESTING=True,
  SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

@app.route('/')
def home():
  return render_template('home.html')


@app.route('/', methods=['POST'])
def index_post():
  text = request.form['text']
  return redirect(url_for('results', text=text))


@app.route('/results')
def results():
  text = request.args['text']
  data = run(text)
  if data is None:
    print('The text did not work')
    flash('L\'ADN que vous avez rentré est incorrecte...'
          )  # Est affiché dans home.html
    return redirect(url_for('home'))
  else:
    return render_template('results.html', generationdata=data)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
