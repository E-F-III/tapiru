from flask import Blueprint, request, jsonify
from app.models import db, Menu, Business, Toppings
from ..forms.menu_form import MenuForm
from flask_login import current_user, login_required
from .auth_routes import validation_errors_to_error_messages

topping_routes = Blueprint("toppings", __name__, url_prefix="/toppings")

# Create topping for menu
@topping_routes.route("/", methods=["POST"])
@login_required
def create_toppings():
    form = ToppingForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_topping = Toppings(
          name = form.name.data,
          menu_id = form.menu.data,
          price = form.price.data
        )
        db.session.add(new_topping)
        db.session.commit()
        return jsonify(new_topping.to_dict()), 200
    else:
        return {"error": validation_errors_to_error_messages(form.errors)}, 401

# Delete topping
