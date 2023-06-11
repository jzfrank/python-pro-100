from flask import Flask, render_template, request
import requests
import sys
import smtplib


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


@app.route('/contact', methods=["GET", "POST"])
def contact_us():
    submitted = False
    if request.method == "POST":
        data = request.form
        print(data, file=sys.stderr)
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        submitted = True
    return render_template('contact.html', submitted=submitted)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == '__main__':
    server = smtplib.SMTP("localhost", 1052)
    server.set_debuglevel(1)
    fromaddr = "frankjinzhang@gmail.com"
    toaddrs = ["frankjinzhang@gmail.com"]
    msg = "Test"
    server.sendmail(fromaddr, toaddrs, msg)
    app.run(debug=True)
