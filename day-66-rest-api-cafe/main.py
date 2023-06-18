from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Record


@app.route("/random")
def random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars()
    cafe = random.choice(list(cafes))
    print(cafe)
    return jsonify(cafe=cafe.to_dict())


@app.route("/all")
def all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc")
    cafe = db.session.execute(db.select(Cafe).where(
        Cafe.location == query_location)).scalar()
    return jsonify(cafe=cafe.to_dict())


@app.route("/cafe")
def get_cafe():
    cafe_id = request.args.get("id")
    cafe = db.session.execute(
        db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    return jsonify(cafe=cafe.to_dict())

# HTTP POST - Create Record


@app.route("/add", methods=["POST"])
def add_cafe():
    print(request.args)
    data = request.args
    parsed_data = {
        "name": data.get("name"),
        "map_url": data.get("map_url"),
        "img_url": data.get("img_url"),
        "location": data.get("location"),
        "seats": data.get("seats"),
        "has_toilet": bool(data.get("has_toilet")),
        "has_wifi": bool(data.get("has_wifi")),
        "has_sockets": bool(data.get("has_sockets")),
        "can_take_calls": bool(data.get("can_take_calls")),
    }
    print(parsed_data)
    cafe = Cafe(**parsed_data)
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.execute(
        db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."})

# HTTP DELETE - Delete Record


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != "TopSecretAPIKey":
        return jsonify(error={"Not Found": "Sorry that's not allowed. Make sure you have the correct api_key."}), 403
    cafe = db.session.execute(
        db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully deleted the cafe."})


if __name__ == '__main__':
    app.run(debug=True)
