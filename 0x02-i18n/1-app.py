#!/usr/bin/env python3
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """config for babel language"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

@app.route('/')
def index():
    """render 1-index"""
    return render_template("1-index.html")

babel = Babel(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
