"""
Quick Start
Source: https://flask.palletsprojects.com/en/3.0.x/quickstart/
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, this is the home page!</p>"

# flask --app my_blog_1 run
# export FLASK_DEBUG=0

@app.route("/about")
def about():
    return "<p>This is the about page!</p>"

if __name__ == '__main__':
    app.run(debug=True)
