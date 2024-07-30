#!/usr/bin/env python3
"""Module for task 2
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for the Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages.

    :return: Best match locale.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index.html template.

    :return: Rendered HTML for the index page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    """
    Run the Flask application.
    """
    app.run(host='0.0.0.0', port=5000)
