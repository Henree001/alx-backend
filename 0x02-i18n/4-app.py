#!/usr/bin/env python3
"""Basic Flask app """
from flask_babel import Babel
from flask import Flask, render_template, request


def get_locale() -> str:
    """Get locale from request"""
    if request.args.get("locale") in app.config["LANGUAGES"]:
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


app = Flask(__name__)


class Config:
    """Config for Flask app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)

# @babel.localeselector


@app.route("/")
def index() -> str:
    """Basic index page"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
