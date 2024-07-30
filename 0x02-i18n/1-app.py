#!/usr/bin/env python3
from flask import Flask, render_template
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


@app.route('/')
def index():
    """
    Render the index.html template.
    
    :return: Rendered HTML for the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    """
    Run the Flask application.
    """
    app.run(host='0.0.0.0', port=5000)
