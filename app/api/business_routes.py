from flask import Blueprint, jsonify, session, request
from app.models import Business, db
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required

business_routes = Blueprint('business', __name__)

@busines_route.route("/<int:id>")
def get_business_by_id(businessId):

    business = Business.query.get(businessId)

    return business.to_dict()
