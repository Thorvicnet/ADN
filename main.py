from flask import Flask, render_template
from DNAGeneration import run

app = Flask(__name__)


@app.route('/')
def index():
  data = run()
  return render_template('index.html', generationdata = data)


app.run(host='0.0.0.0', port=81, debug=True)
