"""
This is a Flask web application that implements various routes and displays different messages when accessed.
"""

from flask import Flask, render_template

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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route handler for the '/c/<text>' URL.
    Args:
        text (str): The text parameter extracted from the URL.
    Returns:
        str: The message "C " followed by the value of the text variable (with underscores replaced by spaces).
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route handler for the '/python/' and '/python/<text>' URLs.
    Args:
        text (str): The text parameter extracted from the URL.
    Returns:
        str: The message "Python " followed by the value of the text variable (with underscores replaced by spaces).
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<float:n>', strict_slashes=False)
def number(n):
    """
    Route handler for the '/number/<n>' URL.
    Args:
        n (float): The number extracted from the URL.
    Returns:
        str: The message "<n> is a number" if n is an integer, otherwise returns a 404 error.
    """
    if n.is_integer():
        return '{} is a number'.format(int(n))
    else:
        return '404 Not Found', 404


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route handler for the '/number_template/<n>' URL.
    Args:
        n (int): The number extracted from the URL.
    Returns:
        str: An HTML page with the number displayed in an H1 tag.
    """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
