from flask import Blueprint, request, jsonify
from app.models import db, Menu, Business, Toppings, Drinks
from ..forms.drink_form import DrinkForm
from flask_login import current_user, login_required
from .auth_routes import validation_errors_to_error_messages

drink_routes = Blueprint("drinks", __name__, url_prefix="/drinks")

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
