import enum

from extensions import db
from .mixins import TimestampMixin

class GameStatus(enum.Enum):
    PLAYING = "PLAYING"
    FOR_PLAY = "FOR_PLAY"
    FINISHED = "FINISHED"

class UserGame(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    igdb_id = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=False)
    status = db.Column(db.Enum(GameStatus), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 