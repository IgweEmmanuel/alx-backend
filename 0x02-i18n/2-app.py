#!/usr/bin/env python3
"""How to use localeselector"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config:
    """language setup"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app, local_selector=get_locale)

@babel.localeselector
def get_locale():
    """return loclae selector for language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """return 2-index"""
    return render_template("2-index")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
