from extensions import db
from utils.hash import generate_password
from .mixins import TimestampMixin

class User(TimestampMixin, db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(200),
        nullable=False,
    )

    games = db.relationship(
        'UserGame',
        backref='user',
        lazy=True
    )

    def set_password(self, password):
        self.password = generate_password(password)

    def __repr__(self):
        return '<User %r>' % self.username