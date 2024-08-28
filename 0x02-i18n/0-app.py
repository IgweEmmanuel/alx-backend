#!/usr/bin/env python3
from flask import Flask, render_template
"""flask language translation"""


app = Flask(__name__)

@app.route('/')
def index():
    """render 0-index"""
    return render_template("0-index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="localhost")
