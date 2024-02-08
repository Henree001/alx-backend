#!/usr/bin/env python3
"""Basic Flask app """
from flask_babel import Babel
from flask import Flask, render_template, request, g
from typing import Dict, Union


app = Flask(__name__)


class Config:
    """Config for Flask app"""

    LANGUAGES = ["en", "es", "de", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """Get locale from request"""
    if request.args.get("locale") in app.config["LANGUAGES"]:
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user(user_id: int) -> Union[Dict[str, Union[str, None]], None]:
    """Get user from request"""
    return users.get(user_id)


# Define before_request function
@app.before_request
def before_request():
    """Before request function"""
    user_id = request.args.get("login_as")
    print(user_id)
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None


@app.route("/")
def index() -> str:
    """Basic index page"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
