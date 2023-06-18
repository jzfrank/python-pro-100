from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"
db = SQLAlchemy(app)
Bootstrap(app)

with app.app_context():
    db.create_all()


class RatingForm(FlaskForm):
    rating = StringField(
        label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), unique=True, nullable=False)


def get_all():
    return Movie.query.all()


def get_movie_by_id(id):
    movie = None
    with app.app_context():
        movie = db.session.execute(
            db.select(Movie).filter_by(id=id)).scalar_one()
    return movie


def update_movie_rating(id, rating, review):
    with app.app_context():
        movie = db.session.execute(
            db.select(Movie).filter_by(id=id)).scalar_one()
        movie.rating = rating
        movie.review = review
        db.session.commit()
    update_ranking()


def delete_movie(id):
    with app.app_context():
        movie = db.session.execute(
            db.select(Movie).filter_by(id=id)).scalar_one()
        db.session.delete(movie)
        db.session.commit()
    update_ranking()

# # Add initial data
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle.",
#     rating=7.3,
#     ranking=10,
#     review="Great Movie",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()


def update_ranking():
    all_movies = get_all()
    all_movies.sort(key=lambda x: x.rating if x.rating else -1, reverse=True)
    for i in range(len(all_movies)):
        all_movies[i].ranking = i + 1
        db.session.commit()


@app.route("/")
def home():
    all_movies = get_all()
    print(all_movies)
    all_movies = sorted(all_movies, key=lambda x: x.rating if x.rating else -1)
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_rating(id):
    form = RatingForm()
    movie = get_movie_by_id(id)
    print(movie)
    if form.validate_on_submit():
        print("True")
        print(form.rating.data, form.review.data)
        update_movie_rating(id, form.rating.data, form.review.data)
        return redirect(url_for("home"))
    movie_title = movie.title if movie else "Movie Not Found"
    return render_template("edit.html", movie_title=movie_title, form=form)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    delete_movie(id)
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        print("True")
        print(form.title.data)
        title = form.title.data
        url = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=en-US&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZWM5NmY2MmRiY2ZmMGZjZWRiNTFmZWU5ZjhhYjBhNSIsInN1YiI6IjYzMjgzOTE3MjBhZjc3MDA3YmZjZWFlZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Cj8RKbhYcdQ8FVG1YGivD-OZelCkivVp_ZISVvjFHNk"
        }
        response = requests.get(url, headers=headers)
        res = response.json()
        return render_template("select.html", movies=res['results'])
    return render_template("add.html", form=form)


@app.route("/add_movie_by_id/<int:movie_id>", methods=["GET", "POST"])
def add_movie_by_id(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZWM5NmY2MmRiY2ZmMGZjZWRiNTFmZWU5ZjhhYjBhNSIsInN1YiI6IjYzMjgzOTE3MjBhZjc3MDA3YmZjZWFlZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Cj8RKbhYcdQ8FVG1YGivD-OZelCkivVp_ZISVvjFHNk"
    }
    response = requests.get(url, headers=headers)
    res = response.json()
    title = res['title']
    img_url = f"https://image.tmdb.org/t/p/w500/{res['poster_path']}"
    year = res['release_date'].split('-')[0]
    description = res['overview']
    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        img_url=img_url)
    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()
    movie = db.session.execute(
        db.select(Movie).filter_by(title=title)).scalar_one()
    update_ranking()
    id = movie.id
    return redirect(url_for("edit_rating", id=id))


if __name__ == '__main__':
    app.run(debug=True)
