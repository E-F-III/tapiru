from flask import Blueprint, request, jsonify
from app.models import db, Menu, Business
from ..forms.menu_form import MenuForm
from flask_login import current_user, login_required
from .auth_routes import validation_errors_to_error_messages

menu_routes = Blueprint("menus", __name__, url_prefix="/menus")

#Get All Menus
@menu_routes.route("")
def all_menus():
    menus = Menu.query.all()
    return {"menus": [m.to_dict() for m in menus]}

#Create Menu
@menu_routes.route("/", methods=["POST"])
@login_required
def create_menu():
    form = MenuForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_menu = Menu(
            name = form.name.data,
            business_id = form.business.data,
            description = form.description.data,
            toppings = form.toppings.data
        )
        db.session.add(new_menu)
        db.session.commit()
        return jsonify(new_menu.to_dict()), 200
    else:
        return {"error": validation_errors_to_error_messages(form.errors)}, 401

