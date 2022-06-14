"""The Revenue Model File."""
from app.extensions import db


class Revenue(db.Model):
    """Basic revenue model."""

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(150), nullable=False)
    accrual_date = db.Column(db.Date, nullable=False)
    transaction_date = db.Column(db.Date, nullable=False)
    invoice_id = db.Column(db.Integer, nullable=True)
    category_id = db.Column(
        db.Integer, db.ForeignKey("revenue_category.id"), nullable=False
    )
    category = db.column("RevenueCategory")
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    customer = db.relationship("Customer")


class RevenueCategory(db.Model):
    """Basic revenue category model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
