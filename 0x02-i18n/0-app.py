#!/usr/bin/env python3
"""Module for task 0
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    Render the index.html template.

    :return: Rendered HTML for the index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    """
    Run the Flask application.
    """
    app.run(host='0.0.0.0', port=5000)
