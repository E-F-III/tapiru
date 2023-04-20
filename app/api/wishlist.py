from flask import Blueprint, request, jsonify
from app.models import db, Menu, Business, Topping, Wishlist, Drink
from app.forms import WishlistForm
from flask_login import current_user, login_required
from .auth_routes import validation_errors_to_error_messages

wishlist_routes = Blueprint("wishlist", __name__, url_prefix="/wishlists")

# Create a wishlist
@wishlist_routes.route("/", methods=["POST"])
@login_required
def create_wishlist():
    form = WishlistForm()
    if form.validate_on_submit():
        if not Drink.query.get(form.drink_id.data):
            return {"error": "Drink not found with the provided ID"}, 404
        new_wishlist = Wishlist(
            drink_id = form.drink_id.data,
            user_id = current_user.id
        )
        db.session.add(new_wishlist)
        db.session.commit()
        return jsonify(new_wishlist.to_dict()), 201
    else:
        return {"error": validation_errors_to_error_messages(form.errors)}, 401
    

