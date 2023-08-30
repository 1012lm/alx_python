"""
This is a simple Flask web application that displays different messages when accessed.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL.
    Returns:
        str: The message "Hello HBNB!".
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the '/hbnb' URL.
    Returns:
        str: The message "HBNB".
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
