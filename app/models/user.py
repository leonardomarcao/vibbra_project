"""The user model file."""
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

from app.extensions import db, pwd_context


class User(db.Model):
    """Basic user model."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    _password = db.Column("password", db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)

    @hybrid_property
    def password(self):
        """Getter password."""
        return self._password

    @password.setter
    def password(self, value):
        """Setter password."""
        self._password = pwd_context.hash(value)

    def __repr__(self):
        return "<User %s>" % self.username
