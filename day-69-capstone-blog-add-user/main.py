from flask import Flask, abort, render_template, redirect, url_for, flash
from functools import wraps
from flask import g, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_gravatar import Gravatar
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
import os
from dotenv import load_dotenv

load_dotenv()


def page_not_found(e):
    return render_template('404.html'), 404


login_manager = LoginManager()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
ckeditor = CKEditor(app)
login_manager.init_app(app)
app.register_error_handler(404, page_not_found)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# avatar
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    # Many to One Relationship
    author_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False)
    # One to Many Relationship
    comments = db.relationship("Comment", backref="blog_post")


# User Model
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(250))
    name = db.Column(db.String(250))
    # One to Many Relationship
    posts = db.relationship("BlogPost", backref="user")
    comments = db.relationship("Comment", backref="user")


# Comment Model
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    # Many to One Relationship
    author_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False)
    # One to Many Relationship
    blog_id = db.Column(db.Integer, db.ForeignKey(
        "blog_posts.id"), nullable=False)


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user is None or not hasattr(current_user, "id") or current_user.id != 1:
            flash(
                "You are not authorized to view this page. Please Log in as Admin User")
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


@ app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@ app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print("form submitted")
        # if user already exists
        if User.query.filter_by(email=form.email.data).first():
            # send flash message
            flash("You've already signed up with that email, log in instead!")
            # redirect to login page
            return redirect(url_for('login'))
        else:
            # create new user
            new_user = User(
                email=form.email.data,
                password=generate_password_hash(
                    form.password.data, method=os.getenv("ENCRYPT_METHOD"), salt_length=os.getenv("SALT_LENGTH")),
                name=form.name.data
            )
            # add new user to database
            db.session.add(new_user)
            db.session.commit()
            # log in user
            login_user(new_user)
            return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=form)


@ app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # check if user exists
        if User.query.filter_by(email=form.email.data).first():
            # check if password is correct
            user = User.query.filter_by(email=form.email.data).first()
            if check_password_hash(
                user.password,
                form.password.data
            ):
                # login user
                login_user(user)
                return redirect(url_for('get_all_posts'))
            else:
                flash("Password incorrect, please try again.")
                return redirect(url_for('login'))
        else:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
    return render_template("login.html", form=form)


@ app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@ app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    form = CommentForm()
    requested_post = BlogPost.query.get(post_id)
    comments = Comment.query.filter_by(blog_id=post_id).all()
    new_comments = []
    for comment in comments:
        user = User.query.get(comment.author_id)
        new_comments.append({
            "text": comment.text,
            "author": user.name
        })
    comments = new_comments
    if not requested_post:
        abort(404)
    if form.validate_on_submit():
        if current_user.is_authenticated:
            new_comment = Comment(
                text=form.comment.data,
                author_id=current_user.id,
                blog_id=post_id
            )
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('show_post', post_id=post_id))
        else:
            flash("You need to login or register to comment.")
            return redirect(url_for('login'))
    return render_template("post.html", post=requested_post, form=form, comments=comments)


@ app.route("/about")
def about():
    return render_template("about.html")


@ app.route("/contact")
def contact():
    return render_template("contact.html")


@ app.route("/new-post", methods=["GET", "POST"])
@ login_required
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user.name,
            date=date.today().strftime("%B %d, %Y"),
            author_id=current_user.id
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@ app.route("/edit-post/<int:post_id>")
@ admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@ app.route("/delete/<int:post_id>")
@ admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
