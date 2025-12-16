"""
App.py for main flask controller
"""

from flask import Flask

app = Flask(__name__)

@app.route('/Team05backend')
def hello():
    """
    Function returns hello, woo hoo
    """
    return "Hello from the backend!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
