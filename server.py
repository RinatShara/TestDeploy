import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


@app.route('/yes')
def yes():
    return 'Say Yes'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
