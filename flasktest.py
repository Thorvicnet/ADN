from flask import Flask
from main import run

app = Flask(__name__)


@app.route('/')
def index():
  return run()


app.run(host='0.0.0.0', port=81, debug=True)
