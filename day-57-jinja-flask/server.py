from urllib import response
from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", random_number=random_number, year=datetime.now().year)


@app.route("/guess/<name>")
def guess(name):
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    gender = requests.get(f"https://api.genderize.io/?name={name}").json()["gender"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", all_posts=all_posts, num=int(num))


if __name__ == "__main__":
    app.run(debug=True)
