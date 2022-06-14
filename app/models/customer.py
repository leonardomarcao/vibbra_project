"""The Customer File."""
from app.extensions import db


class Customer(db.Model):
    """Basic customer model."""

    id = db.Column(db.Integer, primary_key=True)
    legal_name = db.Column(db.String(80), nullable=False)
    commercial_name = db.Column(db.String(80), nullable=False)
    cnpj = db.Column(db.String(15), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<Customer %s>" % self.legal_name
