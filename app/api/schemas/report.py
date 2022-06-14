"""The Report Schema File."""
from app.extensions import ma


class ReportSchema(ma.SQLAlchemyAutoSchema):
    """The Report Schema."""

    fiscal_year = ma.Int(required=True)

    class Meta:
        """The Report Meta Schema."""

        name = "Report"
