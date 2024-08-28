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
app.url_map.strict_slashes = False
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """return loclae selector for language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """return 2-index"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
