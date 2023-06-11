from flask import Flask, render_template
import requests
import sys


app = Flask(__name__)
r = requests.get("https://api.npoint.io/d408122d639032c0cd85")
posts = []
if (r.status_code == 200):
    posts = r.json()


@app.route('/')
def index():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact_us():
    return render_template('contact.html')


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
