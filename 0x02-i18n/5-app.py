#!/usr/bin/env python3
"""Module for task 5
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    Determine the best match for supported languages
    or use the locale from the URL.

    :return: Best match locale or the one provided in the URL.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Mock function to get user information based on the login_as parameter

    :return: User dictionary or None if not found or not logged in.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """
    Set the global user based on the login_as parameter if provided.
    """
    g.user = get_user()


@app.route('/')
def index():
    """
    Render the index.html template with localized
    messages and user-specific information.

    :return: Rendered HTML for the index page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    """
    Run the Flask application.
    """
    app.run(host='0.0.0.0', port=5000)
