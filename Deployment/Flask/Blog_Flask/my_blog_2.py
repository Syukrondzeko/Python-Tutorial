"""
Points:
1. Add home page as same as with main url
2. Add separate html templates
3. Add posts data
4. Add title on the about page
5. Add bootstrap
"""

from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {'author': 'James Harden',
     'title': 'How to do step back',
     'content': 'First post content',
     'date_posted': 'November 16, 2023',
     'img_url': 'image/harden.jpg'
     },
    {'author': 'Kevin Durant',
     'title': 'How to get MVP awards',
     'content': 'Second post content',
     'date_posted': 'November 17, 2023',
     'img_url': 'image/durant.jpg'
     },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

if __name__ == '__main__':
    app.run(debug=True)


