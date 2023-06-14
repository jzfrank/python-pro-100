from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


with app.app_context():
    db.create_all()


def read_all():
    all_books = []
    with app.app_context():
        all_books = db.session.execute(db.select(Book)).scalars()
        all_books = list(all_books)
    print(all_books)
    return all_books


def add_book(title, author, rating):
    new_book = Book(title=title, author=author, rating=rating)
    with app.app_context():
        db.session.add(new_book)
        db.session.commit()


all_books = read_all()


@app.route('/')
def home():
    all_books = read_all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        add_book(title, author, rating)
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    all_books = read_all()
    if request.method == "POST":
        rating = request.form["rating"]
        book_to_update = db.session.execute(
            db.select(Book).where(Book.id == id)).scalar()
        if book_to_update:
            book_to_update.rating = rating
        db.session.commit()
        return redirect(url_for("home"))
    # find the book
    book = None
    for b in all_books:
        if b.id == id:
            book = b
            break
    return render_template("edit.html", book=book)


@app.route("/delete/<int:id>", methods=["POST", "GET"])
def delete(id):
    book_to_update = db.session.execute(
        db.select(Book).where(Book.id == id)).scalar()
    if book_to_update:
        db.session.delete(book_to_update)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/generate")
def generate():
    if len(read_all()) == 0:
        # C: Create Dummy Data
        # primary key is optional
        new_book1 = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
        new_book2 = Book(title="Small Talk", author="Debra", rating=8.5)
        with app.app_context():
            db.session.add(new_book1)
            db.session.add(new_book2)
            db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
