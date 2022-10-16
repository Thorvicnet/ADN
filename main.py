from flask import Flask, render_template, url_for
from modules.DNAGeneration import run

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/results')
def results():
  data = run()
  return render_template('results.html', generationdata=data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
