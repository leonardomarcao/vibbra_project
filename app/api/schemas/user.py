"""The User Schema File."""
from app.models import User
from app.extensions import ma, db


class UserSchema(ma.SQLAlchemyAutoSchema):
    """The User Schema."""

    id = ma.Int(dump_only=True)
    password = ma.String(load_only=True, required=True)

    class Meta:
        """The User Schema Meta."""

        model = User
        sqla_session = db.session
        load_instance = True
        exclude = ("_password",)
