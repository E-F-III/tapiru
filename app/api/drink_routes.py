from flask import Blueprint, request, jsonify
from app.models import db, Menu, Business, Toppings, Drinks
from ..forms.drink_form import DrinkForm
from flask_login import current_user, login_required
from .auth_routes import validation_errors_to_error_messages

drink_routes = Blueprint("drinks", __name__, url_prefix="/drinks")

# Get all drinks + toppings, needs to be tested
@drink_routes.route("")
def all_drinks_toppings():
    drinks = Drinks.query.all()
    toppings = Toppings.query.all()
    return {
        "drinks": [d.to_dict() for d in drinks],
        "toppings": [t.to_dict() for t in toppings]
            }

# Create drink
@drink_routes.route("/", methods=["POST"])
@login_required
def create_drink():
    form = DrinkForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_drink = Drinks(
          name = form.name.data,
          type = form.type.data,
          description = form.description.data,
          menu_id = form.menu_id.data,
          image = form.image.data
        )
        db.session.add(new_drink)
        db.session.commit()
        return jsonify(new_drink.to_dict()), 200
    else:
        return {"error": validation_errors_to_error_messages(form.errors)}, 401

# Update drink, needs to be test
@drink_routes.route("/", methods=["PUT"])
@login_required
def update_drink():
    form = DrinkForm
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        drink = Drinks.query.get(id)
        drink.name = form.name.data
        drink.type = form.type.data
        drink.description = form.type.data
        drink.image = form.image.data

        db.session.commit()
        return jsonify(drink.to_dict()), 200
    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}, 401

#Delete drink
@drink_routes.route("<int:drink_id>", methods=["DELETE"])
@login_required
def delete_drink(drink_id):
    drink = Drinks.query.filter(Drinks.id == drink_id).first()
    db.session.delete(drink)
    db.session.commit()
    return (
        jsonify({"message": "Drink successfully deleted", "status-code": 200}),
        200
    )
