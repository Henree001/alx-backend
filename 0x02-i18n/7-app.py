#!usr/bin/python3
"""Basic Flask app """
from flask_babel import Babel
from flask import Flask, render_template, request, g
import pytz
from typing import Union, Dict


def get_locale() -> str:
    """Get locale from request"""
    locale_param = request.args.get("locale")
    if locale_param and locale_param in app.config["LANGUAGES"]:
        return locale_param

    if (
        hasattr(g, "user")
        and g.user
        and g.user.get("locale") in app.config["LANGUAGES"]
    ):
        return g.user["locale"]

    # Check request headers for preferred locale
    request_locale = request.headers.get("Accept-Language")
    if request_locale:
        # Extract the first language tag from the Accept-Language header
        request_locale = (
            request_locale.split(",")[0].strip().split(";")[0].split("-")[0]
        )
        if request_locale in app.config["LANGUAGES"]:
            return request_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


app = Flask(__name__)


class Config:
    """Config for Flask app"""

    LANGUAGES = ["en", "es", "de", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# @babel.localeselector
def get_user(user_id: int) -> Union[Dict[str, Union[str, None]], None]:
    """Get user from request"""
    return users.get(user_id)


def get_timezone() -> str:
    """Get timezone from request"""
    time_param = request.args.get("timezone")
    if time_param and time_param in pytz.timezone:
        return time_param
    if hasattr(g, "user") and g.user and g.user.get("timezone"):
        return g.user["timezone"]
    return app.config["BABEL_DEFAULT_TIMEZONE"]


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
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(debug=True)
