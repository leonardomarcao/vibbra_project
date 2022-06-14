"""The Revenue Schema File."""
from app.models import Revenue, RevenueCategory
from app.extensions import ma, db
from marshmallow import validate


class RevenueSchema(ma.SQLAlchemyAutoSchema):
    """The Revenue Schema."""

    id = ma.Int(dump_only=True)
    amount = ma.Float(required=True)
    accrual_date = ma.Date(required=True)
    transaction_date = ma.Date(required=True)
    description = ma.String(
        required=True,
        validate=validate.Length(
            max=150, error="Description is too long, max length: 150"
        ),
    )
    invoice_id = ma.Integer(required=False)
    category_id = ma.Integer(required=True)
    customer_id = ma.Integer(required=True)

    class Meta:
        """The Revenue Meta Schema."""

        model = Revenue
        sqla_session = db.session
        load_instance = True


class RevenueCategorySchema(ma.SQLAlchemyAutoSchema):
    """The Revenue Category Schema."""

    id = ma.Int(dump_only=True)
    name = ma.String(
        required=True,
        validate=validate.Length(
            max=50, error="Name of category is too log, max length: 50"
        ),
    )

    class Meta:
        """The Revenue Category Meta Schema."""

        model = RevenueCategory
        sqla_session = db.session
        load_instance = True
