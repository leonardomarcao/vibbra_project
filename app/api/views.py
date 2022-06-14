"""The View App File."""
from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from app.extensions import apispec
from app.api.resources import (
    UserResource,
    UserList,
    CustomerResource,
    CustomerList,
    RevenueResource,
    RevenueList,
    RevenueCategoryResource,
    RevenueCategoryList,
    ReportTotalRevenue,
    ReportRevenueByMonth,
    ReportRevenueByCustomer,
)
from app.api.schemas import (
    UserSchema,
    CustomerSchema,
    RevenueSchema,
    RevenueCategorySchema,
    ReportSchema,
)


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)

# Users Resource
api.add_resource(UserResource, "/users/<int:user_id>", endpoint="user_by_id")
api.add_resource(UserList, "/users", endpoint="users")
# Customer Resource
api.add_resource(CustomerResource, "/customers/", endpoint="customer_by_id")
api.add_resource(CustomerList, "/customers", endpoint="customers")
# Revenue Resource
api.add_resource(
    RevenueResource, "/revenues/<int:revenue_id>", endpoint="revenues_by_id"
)
api.add_resource(RevenueList, "/revenues", endpoint="revenues")
# Revenue Category Resource
api.add_resource(
    RevenueCategoryResource,
    "/revenues-categories/<int:revenue_category_id>",
    endpoint="revenues_categories_by_id",
)
api.add_resource(
    RevenueCategoryList, "/revenues-categories", endpoint="revenue_categories"
)
# Reports Resource
api.add_resource(ReportTotalRevenue, "/reports/total-revenue")
api.add_resource(ReportRevenueByMonth, "/reports/revenue-by-month")
api.add_resource(ReportRevenueByCustomer, "/reports/revenue-by-customer")


@blueprint.before_app_first_request
def register_views():
    """Register views."""
    apispec.spec.components.schema("UserSchema", schema=UserSchema)
    apispec.spec.components.schema("CustomerSchema", schema=CustomerSchema)
    apispec.spec.components.schema("RevenueSchema", schema=RevenueSchema)
    apispec.spec.components.schema(
        "RevenueCategorySchema", schema=RevenueCategorySchema
    )
    apispec.spec.components.schema("ReportSchema", schema=ReportSchema)
    apispec.spec.path(view=UserResource, app=current_app)
    apispec.spec.path(view=UserList, app=current_app)
    apispec.spec.path(view=CustomerResource, app=current_app)
    apispec.spec.path(view=CustomerList, app=current_app)
    apispec.spec.path(view=RevenueResource, app=current_app)
    apispec.spec.path(view=RevenueList, app=current_app)
    apispec.spec.path(view=RevenueCategoryResource, app=current_app)
    apispec.spec.path(view=RevenueCategoryList, app=current_app)
    apispec.spec.path(view=ReportTotalRevenue, app=current_app)
    apispec.spec.path(view=ReportRevenueByMonth, app=current_app)
    apispec.spec.path(view=ReportRevenueByCustomer, app=current_app)


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400
