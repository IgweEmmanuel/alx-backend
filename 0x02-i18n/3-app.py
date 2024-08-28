#!/usr/bin/env python3
"""Flask language translation"""

from flask import Flask, render_template
from flask_babel import Babel, _

# Initialize the Flask application
app = Flask(__name__)

# Define the Config class with the necessary settings
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Apply the configuration to the Flask app
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)

@app.route('/')
def index():
    """Render 0-index"""
    # Use gettext to translate messages
    home_title = _("home_title")
    home_header = _("home_header")
    return render_template("3-index.html", home_title=home_title, home_header=home_header)  # noqa

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="localhost")

