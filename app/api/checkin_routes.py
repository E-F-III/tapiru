from flask import Blueprint, jsonify, request
from app.models import db, Checkin, Drinks, Toppings, User
from app.forms import CheckInForm
from flask_login import current_user, login_required
from .auth_routes import validation_errors_to_error_messages

checkin_routes = Blueprint("checkins", __name__, url_prefix="/checkins")

@checkin_routes.route("/", methods=["POST"])
@login_required
def create_checkin():
    '''
    Function that creates a new checkin
    '''
    form = CheckInForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    drink = Drinks.query.get(form.data["item_id"])

    # Check if drink exists
    if not drink:
        return {'errors': ['Drink not found']}, 401

    if form.validate_on_submit():
        new_checkin = Checkin(
            user_id = current_user.id,
            item_id = form.data["item_id"],
            ice_level = form.data["ice_level"],
            sugar_level = form.data["sugar_level"],
        )
        db.session.add(new_checkin)

        # Add toppings to checkin
        for topping in form.data["toppings"]:

            # Check if toppings exist
            if not Toppings.query.get(topping):
                return {'errors': ['Topping not found']}, 401

            # Add topping to checkin
            new_checkin.toppings.append(Toppings.query.get(topping))

        db.session.commit()
        return jsonify(new_checkin.to_dict()), 200

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@checkin_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_checkin(id):
    '''
    Function that deletes a checkin
    '''
    checkin = Checkin.query.get(id)

    # Check if checkin exists
    if not checkin:
        return {'errors': ['Checkin not found']}, 404

    # Check if user is authorized to delete checkin
    if checkin.user_id != current_user.id:
        return {'errors': ['Unauthorized']}, 401

    db.session.delete(checkin)
    db.session.commit()
    return jsonify(checkin.to_dict()), 200
