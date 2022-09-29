from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blog_posts=all_posts)


@app.route("/post/<num>")
def post(num):
    num = int(num)
    post = [p for p in all_posts if p["id"] == num][0]
    title = post["title"]
    body = post["body"]
    subtitle = post["subtitle"]
    return render_template("post.html", title=title, body=body, subtitle=subtitle)


if __name__ == "__main__":
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    app.run(debug=True)
