from flask import Blueprint, request, jsonify
from app.models import db, Menu, Business, Drinks, Toppings
from ..forms.menu_form import MenuForm
from flask_login import current_user, login_required
from .auth_routes import validation_errors_to_error_messages

menu_routes = Blueprint("menus", __name__, url_prefix="/menus")

#Get All Menus
@menu_routes.route("")
def all_menus():
    menus = Menu.query.all()
    return {"menus": [m.to_dict() for m in menus]}

# Get drinks + toppings, needs to be tested
@menu_routes.route("")
def all_drinks_toppings():
    drinks = Drinks.query.all()
    toppings = Toppings.query.all()
    return {
        "drinks": [d.to_dict() for d in drinks],
        "toppings": [t.to_dict() for t in toppings]
            }

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
        return jsonify(new_menu.to_dict()), 201
    else:
        return {"error": validation_errors_to_error_messages(form.errors)}, 401

#Update Menu, needs to be tested
@menu_routes.route("/", methods=["PUT"])
@login_required
def update_menu():
    form = MenuForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        menu = Menu.query.get(id)
        menu.name = form.name.data
        menu.description = form.description.data
        menu.toppings = form.toppings.data

        db.session.commit()
        return jsonify(menu.to_dict()), 200
    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}, 401

#Delete menu
@menu_routes.route("/<int:menu_id>", methods=["DELETE"])
@login_required
def delete_menu(menu_id):
    menu = Menu.query.filter(Menu.id == menu_id).first()
    db.session.delete(menu)
    db.session.commit()
    return (
        jsonify({"message": "Menu successfully deleted", "status-code": 200}),
        200
    )
