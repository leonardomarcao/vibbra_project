"""The Customer Schema File."""
from app.models import Customer
from app.extensions import ma, db


class CustomerSchema(ma.SQLAlchemyAutoSchema):
    """The Customer Schema."""

    id = ma.Int(dump_only=True)
    legal_name = ma.String(required=True)
    commercial_name = ma.String(required=True)
    cnpj = ma.String(required=True)

    class Meta:
        """The Customer Meta Schema."""

        model = Customer
        sqla_session = db.session
        load_instance = True
