from flask import Flask, render_template, url_for, redirect, request
from modules.DNAGeneration import run

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
  text = request.form['text']
  return redirect(url_for('results', text=text))


@app.route('/results')
def results():
  text = request.args['text']
  data = run(text)
  return render_template('results.html', generationdata=data)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
