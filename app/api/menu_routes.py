from flask import Blueprint, request, jsonify
from app.models import db, Menu, Business
from ..forms.menu_form import MenuForm
from flask_login import current_user, login_required
from .auth_routes import validation_errors_to_error_messages

menu_routes = Blueprint("menus", __name__, url_prefix="/menus")

# GET ALL Menus
@menu_routes.route("")
def all_menus():
    menus = Menu.query.all()
    return {"menus": [m.to_dict() for m in menus]}
