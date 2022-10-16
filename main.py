from flask import Flask, render_template
from modules.DNAGeneration import run

app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello'


@app.route('/results')
def results():
  data = run()
  return render_template('results.html', generationdata=data)


app.run(host='0.0.0.0', port=81, debug=True)
