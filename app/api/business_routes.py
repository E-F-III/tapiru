from flask import Blueprint, jsonify, session, request
from app.models import Business, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms.business_form import BusinessForm
from app.api.auth_routes import validation_errors_to_error_messages

business_routes = Blueprint('business', __name__)

@business_routes.route("/<int:id>")
def get_business_by_id(businessId):
    """
    Query for a business by id and return it as a dictionary
    """
    business = Business.query.get(businessId)

    return business.to_dict()


@business_routes.route("/", methods=["POST"])
@login_required
def create_business():
    """
    Function to create a new business
    """
    form = BusinessForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_business = Business(
            name=form.data.name,
            street_address=form.data.street_address,
            city=form.data.city,
            region=form.data.region,
            postal_code=form.data.postal_code,
            country=form.data.country,
            website=form.data.website,
            telephone=form.data.telephone,
            timezone=form.data.timezone,
            currency=form.data.currency,
            about_location=form.data.about_location,
            owner_id=current_user.id
        )
        db.session.add(new_business)
        db.session.commit()
        return new_business.to_dict(), 201
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@business_routes.route("/", methods=["PUT"])
@login_required
def edit_business(businessId):
    """
    Function to edit an existing business (get business by their id)
    """
    form = BusinessForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    business_to_edit = Business.query.get(businessId)

    if form.validate_on_submit():

        business_to_edit.owner_id = current_user.id

        business_to_edit.name = form.data['name']
        business_to_edit.street_address = form.data['street_address']
        business_to_edit.city = form.data['city']
        business_to_edit.region = form.data['region']
        business_to_edit.postal_code = form.data['postal_code']
        business_to_edit.country = form.data['country']
        business_to_edit.website = form.data['website']
        business_to_edit.telephone = form.data['telephone']
        business_to_edit.timezone = form.data['timezone']
        business_to_edit.currency = form.data['currency']
        business_to_edit.about_location = form.data['about_location']

        db.session.add(new_business)
        db.session.commit()
        return new_business.to_dict(), 201

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
